import pandas as pd
from IPython.display import display, Markdown
from pathlib import Path
import re


from src.report import io_ops
from pathlib import Path
import pandas as pd

SAMPLESHEET_COLS = [
    "sample_id", "tested", "positive", "sequenced", "surviellance_type",
    "collection_date", "sample_type", "sample_medium", "sample_submitter",
    "geographic_location", "patient_age", "ct_value", "gisaid", "genbank"
]

MIRA_COLS = [
    "sample_id", "total_reads", "pass_qc", "reads_mapped",
    "reference", "percent_reference_coverage", "median_coverage",
    "count_minor_snv_at_or_over_5_pct", "pass_fail_reason", "subtype",
    "mira_module", "runid", "instrument", "clade", "short_clade", "subclade"
]


def _check_columns(df: pd.DataFrame, expected: list[str], source: Path) -> None:
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Columns missing from {source}: {missing}")


def load_samplesheet(path: Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Samplesheet not found: {path}")
    if not path.is_file():
        raise ValueError(f"Samplesheet path is not a file: {path}")

    df = io_ops.read_csv(path)
    _check_columns(df, SAMPLESHEET_COLS, path)

    df["collection_date"] = pd.to_datetime(df["collection_date"], errors="coerce")
    df["collection_year"] = df["collection_date"].dt.strftime("%Y")
    df["collection_period"] = df["collection_date"].dt.to_period("M").dt.to_timestamp()

    return df


def load_mira(mira_dir: Path) -> pd.DataFrame:
    mira_dir = Path(mira_dir)
    if not mira_dir.exists():
        raise FileNotFoundError(f"MIRA directory not found: {mira_dir}")
    if not mira_dir.is_dir():
        raise ValueError(f"MIRA path is not a directory: {mira_dir}")

    csv_files = sorted(mira_dir.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in MIRA directory: {mira_dir}")

    dfs = []
    for p in csv_files:
        df = io_ops.read_csv(p)
        _check_columns(df, MIRA_COLS, p)  # was incorrectly using SAMPLESHEET_COLS
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def load_inputs(params: dict) -> pd.DataFrame:
    samplesheet_path = params.get("samplesheet")
    mira_path = params.get("mira")

    if samplesheet_path is None:
        raise KeyError("'samplesheet' key missing from params")
    if mira_path is None:
        raise KeyError("'mira' key missing from params")

    df_sh = load_samplesheet(samplesheet_path)
    df_mira = load_mira(mira_path)

    df_joined = df_sh.merge(df_mira, on="sample_id", how="left")

    return df_joined
    
def uniq(df, col: str) -> list:
    s = df.get(col)
    if s is None:
        return []
    return sorted(s.dropna().astype(str).unique().tolist())

def range(df, col: str):
    s = df.get(col)
    if s is None:
        return [None, None]
    s = s.dropna()
    if s.empty:
        return [None, None]
    # If it's dates, ensure proper dtype
    if "date" in col:
        s = pd.to_datetime(s, errors="coerce").dropna()
        if s.empty:
            return [None, None]
        return [s.min().date().isoformat(), s.max().date().isoformat()]
        # Numeric-ish
        s = pd.to_numeric(s, errors="coerce").dropna()
    if s.empty:
        return [None, None]
    return [float(s.min()), float(s.max())]

def count_sample_ids(df: pd.DataFrame, col: str) -> int:
    """Filter to rows where col is True, then count unique sample_ids."""
    mask = df[col].fillna(False).astype(bool)
    return df.loc[mask, "sample_id"].nunique()

def dominant_values(df: pd.DataFrame, col: str, threshold: float = 0.5) -> list:
    """Return values that represent more than `threshold` of non-null entries in col."""
    counts = df[col].dropna().value_counts()
    return counts[counts > counts.sum() * threshold].index.tolist()

def parse_flua_clade(clade: str) -> dict:
    if not clade:
        return {}

    clade = clade.strip()

    parts = clade.split(".")

    result = {
        "virus_type": "A",
        "clade_root": parts[0],     # e.g., 6B or 3C
        "clade_levels": parts,      # full hierarchy
        "clade_depth": len(parts)
    }

    return result

def parse_flub_clade(clade: str) -> dict:
    if not clade:
        return {}

    clade = clade.strip()

    parts = clade.split(".")

    result = {
        "virus_type": "B",
        "clade_root": parts[0],      # e.g., V1A or Y3
        "clade_levels": parts,
        "clade_depth": len(parts)
    }

    return result


SEGMENTS = ["PB1", "PB2", "HA", "MP", "NA", "NP", "NS", "PA"]

SEGMENT_PATTERNS = {
    seg: re.compile(rf"^(A|B)_{seg}(_|$)", re.IGNORECASE)
    for seg in SEGMENTS
}

def count_complete_genomes(df: pd.DataFrame) -> int:
    """Count samples with all 8 segments present (passing QC)."""
    def has_all_segments(group):
        refs = group["reference"].dropna()
        return all(
            any(pat.match(r) for r in refs)
            for pat in SEGMENT_PATTERNS.values()
        )

    return (
        df.groupby("sample_id")
        .filter(has_all_segments)
        ["sample_id"]
        .nunique()
    )

def count_segment(df: pd.DataFrame, segment: str) -> int:
    """Count samples with a specific segment present."""
    if segment not in SEGMENT_PATTERNS:
        raise ValueError(f"Unknown segment: {segment!r}. Must be one of: {list(SEGMENT_PATTERNS)}")
    
    pat = SEGMENT_PATTERNS[segment]
    matched = df[df["reference"].str.match(pat.pattern, na=False)]
    return matched["sample_id"].nunique()