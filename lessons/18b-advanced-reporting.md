---
layout: page
title: "Advanced Reporting: Automation with Quarto"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/18b-advanced-reporting/
---

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson</p>

## Module Objectives

- Understand how to automate report generation with Quarto
- Explore the structure and components of an example genomic surveillance report

---

## Slides

<iframe
  src="{{ site.baseurl }}/presentations/Presentation18b_Advanced_Reporting.html"
  width="100%"
  height="600px"
  frameborder="0"
  allowfullscreen>
</iframe>

<a href="{{ site.baseurl }}/presentations/Presentation18b_Advanced_Reporting.html" download>⬇ Download Slides</a>

---

## Example Report

Below is an example influenza genomic surveillance report generated using Quarto. The report is parameterized, meaning the same `.qmd` template can be reused across surveillance periods by updating a single config file.

<div style="border: 2px solid #015CAE; border-radius: 6px; overflow: hidden; margin-bottom: 1em;">
<iframe
  src="{{ site.baseurl }}/practical/advanced_reporting/genome_report.html"
  width="100%"
  height="700px"
  frameborder="0"
  allowfullscreen>
</iframe>
</div>

---

## How the Report Was Created

The report is rendered from a Quarto markdown file (`genome_report.qmd`) using a separate config file (`config.yml`) that supplies run-specific parameters such as the reporting period, input data paths, and narrative content. This separation allows the report template to remain static while only the config is updated each run.

### Report File Descriptions

The full set of files used to create this report can be found on [GitHub](https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/advanced_reporting/).

<pre><code>
├── config.yml              # Run-specific parameters (updated each run)
├── genome_report.qmd       # Quarto report template
├── genome_report.html      # Rendered HTML output
├── data/
│   ├── mira/
│   │   ├── mira_output-1.csv
│   │   └── mira_output-2.csv
│   ├── h1.nwk
│   └── samplesheet.csv
└── src/
    └── report/
        ├── __init__.py
        ├── config.py
        ├── data.py
        ├── display.py
        ├── io_ops.py
        ├── map.py
        ├── timeline.py
        └── tree.py
</code></pre>

| File / Directory | Description |
| - | - |
| <a href="../../practical/advanced_reporting/genome_report.html" target="_blank"><code>genome_report.html</code></a> | Rendered HTML output — the final report that would be distributed. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/advanced_reporting/genome_report.qmd" target="_blank"><code>genome_report.qmd</code></a> | Quarto report template containing markdown narrative, code chunks, and static front matter. Relies on `data/`, `src/`, and `config.yml`. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/advanced_reporting/config.yml" target="_blank"><code>config.yml</code></a> | Run-specific config file supplying parameters such as reporting period, input data paths, and narrative content. Updated each run and passed to Quarto via `-M config.yml`. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/advanced_reporting/data/" target="_blank"><code>data/</code></a> | Sample input data: samplesheet, MIRA output CSVs, and a phylogenetic tree file. These files are updated each reporting period. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/advanced_reporting/src/" target="_blank"><code>src/</code></a> | Custom Python module imported within `genome_report.qmd`. Contains helper functions for data loading, visualization, tree rendering, and display logic. |

### Render Command

<pre><code>
quarto render genome_report.qmd -M config.yml
</code></pre>

The `-M` flag merges the metadata in `config.yml` into the document's front matter at render time, overriding any matching keys defined in `genome_report.qmd`.