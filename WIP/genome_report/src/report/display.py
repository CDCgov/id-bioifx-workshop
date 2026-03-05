import pandas as pd
from IPython.display import HTML, display

from src.report import data


def _display_table(rows, cols: list[str] | None = None) -> str:
    df = pd.DataFrame(rows, columns=cols)
    return df.to_html(index=False, header=cols is not None, border=0)


def key_findings(df: pd.DataFrame) -> str:
    rows = [
        ["**Total Specimens**",            data.count_sample_ids(df, "tested")],
        ["**Influenza-positive specimens**", data.count_sample_ids(df, "positive")],
        ["**Viruses sequenced**",           data.count_sample_ids(df, "sequenced")],
        ["**Dominant clades/subclades:**",  data.dominant_values(df[df["short_clade"] != "Undetermined"], "short_clade")],
    ]
    return _display_table(rows)


def sample_collection(df: pd.DataFrame) -> str:
    age_min, age_max = data.range(df, "patient_age")
    rows = [
        ["**Surviellance Systems**",   data.uniq(df, "surviellance_type")],
        ["**Specimen types**",         data.uniq(df, "sample_type")],
        ["**Collection mediums**",     data.uniq(df, "sample_medium")],
        ["**Testing laboratories**",   data.uniq(df, "submitter")],
        ["**Age groups included**",    f"{age_min:.0f} - {age_max:.0f}"],
        ["**Geographic coverage**",    data.uniq(df, "geographic_location")],
    ]
    return _display_table(rows)


def total_specimens(df: pd.DataFrame) -> str:
    total = data.count_sample_ids(df, "tested")
    pos   = data.count_sample_ids(df, "positive")
    rows = [
        ["Total specimens tested",          total],
        ["Influenza-positive specimens",    pos],
        ["Influenza-negative specimens",    total - pos],  # was duplicating "positive" label
    ]
    return _display_table(rows, cols=["Metric", "Count"])


def subtype_summary(df: pd.DataFrame) -> str:
    passed = df[df["pass_fail_reason"] == "Pass"].copy()
    if passed.empty:
        return "<p>No passing samples found.</p>"

    passed["_flu_type"] = None
    passed.loc[passed["reference"].str.startswith("A_", na=False), "_flu_type"] = "A"
    passed.loc[passed["reference"].str.startswith("B_", na=False), "_flu_type"] = "B"
    passed = passed[passed["_flu_type"].notna()]

    unique = passed[["sample_id", "subtype", "_flu_type"]].drop_duplicates(subset="sample_id")
    total  = unique["sample_id"].nunique()
    if total == 0:
        return "<p>No Influenza samples found.</p>"

    rows = []
    for flu_type, label in [("A", "Influenza A"), ("B", "Influenza B")]:
        subset      = unique[unique["_flu_type"] == flu_type]
        type_total  = subset["sample_id"].nunique()
        if type_total == 0:
            continue
        rows.append((label, type_total, round(type_total / total * 100, 1)))
        for subtype, count in subset["subtype"].fillna("Other").value_counts().items():
            rows.append((f"└─ {subtype}", count, round(count / total * 100, 1)))

    rows.append(("Total influenza positive", total, 100.0))
    return pd.DataFrame(rows, columns=["Virus Type / Subtype", "Count", "Percentage (%)"]).to_html(index=False, border=0)


def sequencing_criteria(df: pd.DataFrame) -> str:
    subset = df[df["sequenced"]]
    age_min,  age_max  = data.range(subset, "patient_age")
    ct_min,   ct_max   = data.range(subset, "ct_value")
    time_min, time_max = data.range(subset, "collection_date")
    rows = [
        ["**Ct value range**",                          f"{ct_min:.1f} - {ct_max:.1f}"],
        ["**Geographic coverage**",                     data.uniq(subset, "geographic_location")],
        ["**Temporal distribution across season**",     f"{time_min} - {time_max}"],
        ["**Age groups included**",                     f"{age_min:.0f} - {age_max:.0f}"],
    ]
    return _display_table(rows)


def sequencing_output(df: pd.DataFrame) -> str:
    positive   = data.count_sample_ids(df, "positive")
    sequenced  = data.count_sample_ids(df, "sequenced")
    complete   = data.count_complete_genomes(df)
    ha         = data.count_segment(df, "HA")
    na         = data.count_segment(df, "NA")

    def pct(n, d):
        return f"{100 * n / d:.1f}" if d else "-"

    rows = [
        ["Influenza-positive specimens eligible for sequencing", positive,            "-"],
        ["Specimens successfully sequenced",                     sequenced,           pct(sequenced, positive)],
        ["Specimen with complete genomes (all 8 segments pass QC)", complete,         pct(complete, sequenced)],
        ["Specimen with incomplete genomes (< 8 segments)",      sequenced - complete, pct(sequenced - complete, sequenced)],
        ["Specimen with complete HA segments",                   ha,                  pct(ha, sequenced)],
        ["Specimen with complete NA segments",                   na,                  pct(na, sequenced)],
    ]
    return _display_table(rows, cols=["Metric", "Count", "Percentage (%)"])

def sequencing_qc(df: pd.DataFrame) -> str:
    COLS = {
        "percent_reference_coverage": "Reference Coverage (%)",
        "median_coverage":            "Median Coverage (x)",
        "count_minor_snv_at_or_over_5_pct": "Minor SNVs (≥5%)",
    }

    rows = []
    for col, label in COLS.items():
        s = df[col].dropna()
        rows.append([
            label,
            f"{s.min():.1f} - {s.max():.1f}",
            f"{s.mean():.1f} ± {s.std():.1f}",
            f"{s.median():.1f}",
        ])

    return _display_table(rows, cols=["Metric", "Range", "Mean ± SD", "Median"])

def clade_summary(df: pd.DataFrame) -> str:
    passed = df[df["pass_fail_reason"] == "Pass"].copy()
    if passed.empty:
        return "<p>No passing samples found.</p>"

    unique = (
        passed[["sample_id", "subtype", "short_clade"]]
        .drop_duplicates(subset="sample_id")
    )
    unique["short_clade"] = unique["short_clade"].fillna("Undetermined")

    html_parts = []
    for i, (subtype, group) in enumerate(unique.groupby("subtype"), start=1):
        total = group["sample_id"].nunique()

        clade_counts = (
            group["short_clade"]
            .value_counts()
            .sort_values(ascending=False)
        )

        rows = [
            (clade, count, round(count / total * 100, 1))
            for clade, count in clade_counts.items()
        ]
        rows.append(("Total", total, 100.0))

        table = pd.DataFrame(rows, columns=["Clade / Subclade", "Count", "Percentage (%)"]).to_html(index=False, border=0)
        html_parts.append(f"<h3>5.{i} Influenza {subtype}</h3>\n{table}")

    display(HTML("\n\n".join(html_parts)))