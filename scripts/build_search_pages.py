#!/usr/bin/env python3
"""Generate synthesised hidden HTML pages for Pagefind indexing.

After `jekyll build`, this script generates hidden HTML pages from extracted
text cache files so Pagefind can index the full text content of PDFs and
presentations alongside the visible site content.

Each generated page includes data-pagefind-body and data-pagefind-meta
attributes so Pagefind treats them as searchable content that links back
to the appropriate page.

Usage:
    python scripts/build_search_pages.py
"""

import sys
from html import escape
from pathlib import Path

# ---------------------------------------------------------------------------
# HTML template for synthesised pages
# ---------------------------------------------------------------------------

_PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
<div data-pagefind-body
     data-pagefind-filter="type:{doc_type}"
     style="display:none;">
<h1 data-pagefind-meta="title">{title}</h1>
<span data-pagefind-meta="url:{url}"></span>
<p>{text}</p>
</div>
</body>
</html>
"""

# Map from extracted file slug to a page URL and type
# Presentations that have corresponding lesson pages get linked there
_SLUG_URL_MAP = {
    "Presentation1_TrainingOverviewVCM": ("/lessons/02-overview-vcm/", "Presentation"),
    "Presentation2_ComputerOS": ("/lessons/03-computer-basics/", "Presentation"),
    "Presentation3_IntroBASH-FINAL": ("/lessons/05-cli-intro/", "Presentation"),
    "Presentation4_BifxProgramming": ("/lessons/07-bifx-programming/", "Presentation"),
    "Presentation5_APHL_computer_environments": ("/lessons/09-computer-environments/", "Presentation"),
    "Presentation6_Int_Flu_Workshop_Docker_Common-Software_LF": ("/lessons/10-containers-registries/", "Presentation"),
    "Presentation7_NGSPipelines": ("/lessons/11-genome-assembly/", "Presentation"),
    "Presentation10_QMS_BestPractices": ("/lessons/17-quality-management-systems/", "Presentation"),
    "Presentation10_QMS_CommonProblems": ("/lessons/17b-common-problems/", "Presentation"),
    "Presentation11_Intro_Quarto": ("/lessons/18-reporting/", "Presentation"),
    "Genomic_Epi": ("/lessons/16-genomic-epi/", "Presentation"),
    "phylogenetics": ("/lessons/15-phylogenetics/", "Presentation"),
    "Bash_Command_EncyclopediaV2": ("/lessons/05-cli-intro/", "Reference"),
    "Train_the_trainer": ("/presentations/Train_the_trainer.pdf", "Presentation"),
}


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    cache_dir = repo_root / "_search" / "cache"
    site_dir = repo_root / "_site"
    output_dir = site_dir / "_search_pages"

    # Read baseurl from _config.yml if available
    config_path = repo_root / "_config.yml"
    baseurl = ""
    if config_path.exists():
        import yaml
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        baseurl = config.get("baseurl", "").rstrip("/")

    if not site_dir.is_dir():
        print("ERROR: _site/ not found — run `jekyll build` first", file=sys.stderr)
        return 1

    if not cache_dir.is_dir():
        print("WARNING: _search/cache/ not found — run extract_local.py first",
              file=sys.stderr)
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    generated = 0

    for cache_file in sorted(cache_dir.glob("*.txt")):
        slug = cache_file.stem
        text = cache_file.read_text(encoding="utf-8").strip()
        if not text:
            continue

        # Look up URL and type from the mapping, or use a generic fallback
        if slug in _SLUG_URL_MAP:
            url, doc_type = _SLUG_URL_MAP[slug]
            url = baseurl + url
        else:
            # Fallback: link to the file itself
            url = f"{baseurl}/presentations/{slug}.pdf"
            doc_type = "Document"

        title = slug.replace("_", " ").replace("-", " ")

        html = _PAGE_TEMPLATE.format(
            title=escape(title),
            doc_type=escape(doc_type),
            url=escape(url),
            text=escape(text),
        )

        out_file = output_dir / f"{slug}.html"
        out_file.write_text(html, encoding="utf-8")
        generated += 1
        print(f"  generated: {slug}.html ({len(text)} chars)")

    print(f"\nDone: {generated} search pages generated in {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
