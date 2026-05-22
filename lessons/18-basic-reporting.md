---
layout: page
title: "Basic Reporting: Markdown and Pandoc"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/18-basic-reporting/
---

{: title}

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson and Ben Rambo-Martin</p>

## Module Objectives

- Render Markdown documents to HTML and PDF using `pandoc`

## What is Pandoc?

<a href="https://pandoc.org" target="_blank"><code>Pandoc</code></a> is a command-line tool that converts documents between a wide range of formats — including Markdown, HTML, PDF, and Word. It is the universal converter that powers Quarto, RMarkdown, and Jupyter Book under the hood, and can be used directly on its own.

For routine reporting, Pandoc lets you write a report once in plain Markdown and render it to any format you need — without reformatting or copying content between tools.

## Anatomy of a Pandoc Markdown Report

A Pandoc Markdown report is a plain text file (`.md`) with two parts: 

### Front Matter
Front matter is a YAML block at the very top of the file, enclosed in triple dashes (`---`) that defines metadata used by Pandoc.

<pre><code class="language-yaml">
---
title: "Weekly Influenza Surveillance Report"
author: "Your Name"
date: "2025-01-01"
---
</code></pre>

### Markdown Content
The markdown content is the main report including the headers, paragraphs, tables, lists, code blocks, and images.

<pre><code class="language-markdown">
## Overview
This is a report for ...
</code></pre>

Below is an example of these two sections shown in the same report document:
<pre><code class="language-markdown">
---
title: "Weekly Influenza Surveillance Report"
author: "Your Name"
date: "2025-01-01"
---

## Overview
This is a report for ...
</code></pre>

## Rendering Markdown with Pandoc

### Installation
We will install Pandoc by installing a related tool called Quarto.
<pre><code class="language-bash">
# Create environment and install Quarto
micromamba create -n reports \
    -c conda-forge \
    quarto=1.4.550 librsvg=2.62.1 \
    -y

# Activate the environment
micromamba activate reports

# Install TinyTeX for PDF output
quarto install tinytex
</code></pre>

### Rendering to HTML

<pre><code class="language-bash">
pandoc genome-report.md \
  --standalone \
  --embed-resources \
  --toc \
  -o genome-report.html
</code></pre>

The flags used above are described below:

| Flag                 | Description                                               |
|----------------------|-----------------------------------------------------------|
| `--standalone`       | Produce a complete HTML document (with `<html>` wrapper)  |
| `--embed-resources`  | Inline all images and CSS so the `.html` is self-contained |
| `--toc`              | Generate a table of contents from the headers             |
| `-o`                 | Output file name                                          |

`--embed-resources` is important when sharing the file: it produces a single `.html` that can be emailed or dropped into a shared drive without any accompanying `media/` folder.

### Rendering to PDF

<pre><code class="language-bash">
pandoc genome-report.md \
  --pdf-engine=xelatex \
  --toc \
  -o genome-report.pdf
</code></pre>

Because relative image paths are resolved from the location of the Markdown file, the same `genome-report.md` that renders to HTML will also render to PDF with no changes — Pandoc finds `media/tree.png` in both cases.

## Example: The Genome Report Template

A ready-to-use surveillance report template is provided for this workshop:

- Download: [genome-report.md](https://raw.githubusercontent.com/CDCgov/id-bioifx-workshop/refs/heads/main/assets/templates/genome-report.md)

The template includes the sections you typically need in a national genomic surveillance report — executive summary, specimen collection, subtype distribution, sequencing output, clade distribution, resistance markers, phylogenetic analysis, data sharing, limitations, and conclusions — all using only the Markdown syntax covered above.

### Try It

1. Go to [https://nextstrain.org/seasonal-flu/h3n2/ha/2y](https://nextstrain.org/seasonal-flu/h3n2/ha/2y) and download figures as an SVG using **DOWNLOAD DATA** at the bottom of the page.
2. Create a new directory called `media/`.
3. Move the downloaded SVG into `media/` and rename it `tree.svg`.
4. Fill in the placeholder values for your reporting period.
5. Render to HTML and PDF:

<pre><code class="language-bash">
pandoc genome-report.md --standalone --embed-resources --toc \
  -o genome-report.html

pandoc genome-report.md --pdf-engine=xelatex --toc \
  -o genome-report.pdf
</code></pre>

6. Open the resulting files and confirm the figure appears in both.

## Extending Markdown with Quarto

Everything above produces a *static* report: you fill in the numbers by hand and re-render. That works well for one-off documents, but surveillance reporting is repetitive — the same tables and figures are regenerated every week, month, or season with fresh data.

[Quarto](https://quarto.org) is an open-source publishing system that extends Markdown with the ability to **execute code inside the document at render time**. A Quarto document (`.qmd`) is a Markdown file with embedded Python, R, or Bash chunks. When Quarto renders the document, it runs each chunk and inserts the computed output — summary statistics, tables, plots — directly into the report.

For example, the manually filled subtype table from the template:

<pre><code class="language-markdown">
| Type / Subtype      | Count | Percent |
|---------------------|------:|--------:|
| A(H1N1)pdm09        |    42 |   29.6% |
| A(H3N2)             |    87 |   61.3% |
| B/Victoria          |    13 |    9.2% |
</code></pre>

...can be replaced in a Quarto document with an executable chunk that computes the same table from a CSV every time the report is rendered:

<pre><code class="language-markdown">
```{python}
import pandas as pd
df = pd.read_csv("data/specimens.csv")
summary = (df["subtype"].value_counts(normalize=False)
             .rename_axis("Subtype").reset_index(name="Count"))
summary["Percent"] = (summary["Count"] / summary["Count"].sum() * 100).round(1)
summary
```
</code></pre>

With Quarto, the `genome-report.md` workflow extends naturally to an automated reporting pipeline:

- **Parameterize** the report so the same template can be rendered against different countries, seasons, or input files.
- **Compute** counts, percentages, resistance frequencies, and QC metrics directly from data files — no manual copy-paste.
- **Regenerate** figures (phylogenetic trees, coverage plots) as part of the render.
- **Output** the same document as HTML, PDF, or Word without changing the source.

A fully automated Quarto version of the template (`genome_report.qmd`) is available under `../../practical/report_automation/genome_report/` in this repository for reference.

Pandoc is the foundation; Quarto is what you reach for when the report needs to run itself.
