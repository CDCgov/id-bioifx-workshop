---
layout: page
title: Reporting with Markdown and Pandoc
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/18-reporting/
---

{: title}

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson and Ben Rambo-Martin</p>
## Module Objectives

- Understand the basics of Markdown
- Render Markdown documents to HTML and PDF using `pandoc`
- Include figures via relative image paths
- Understand how Quarto extends Markdown to automate reports

---

## Why Markdown?

Markdown is a lightweight plain-text formatting language that is easy to write,
easy to read in its raw form, and easy to convert into polished documents.
Because Markdown files are plain text, they work seamlessly with version
control (Git), diff nicely in pull requests, and can be edited in any text
editor. A single `.md` file can be rendered into HTML for the web, PDF for
sharing, and Word for collaborators — all without changing the source.

In bioinformatics, Markdown is a natural fit for surveillance reports, run
summaries, SOPs, and documentation that needs to be reproducible and
shareable.

> This workshop site itself is written almost entirely in Markdown. Every
> lesson you have worked through — including this one — is a `.md` file in
> the [workshop repository](https://github.com/cdcgov/id-bioifx-workshop/tree/main/lessons),
> rendered to HTML by a "static site generator." 

---

## Markdown Basics

The sections below cover the Markdown syntax you will use most often when
writing reports.

---

### Headers

Headers are created using `#` symbols. A single `#` produces the largest
heading (H1), `##` produces H2, `###` produces H3, and so on down to `######`
(H6).

```markdown
# Influenza
## Types A and B
### Subtypes and Lineages
```

---

### Paragraphs and Inline Formatting

Plain text written on consecutive lines forms a paragraph. Separate paragraphs
with a blank line. Inline formatting uses simple symbols:

```markdown
Flu A and B use different classification schemes:

**Flu A** uses *subtypes* (e.g., H5N1), while **Flu B** uses *lineages*
(e.g., Yamagata). You can also use `inline code` for filenames or commands.
```

| Syntax         | Rendered      |
|----------------|---------------|
| `**bold**`     | **bold**      |
| `*italic*`     | *italic*      |
| `` `code` ``   | `code`        |

---

### Lists

Unordered lists use `-` (or `*`) at the start of each line. Ordered lists use
numbers followed by a period. Indent with two spaces to create nested items.

```markdown
- Influenza A
  - H1N1
  - H3N2
- Influenza B
  - Victoria
  - Yamagata

1. Collect specimens
2. Extract RNA
3. Sequence
```

---

### Tables

Tables are built with pipes (`|`) and dashes (`-`). The row of dashes below
the header separates the header from the body. Colons in the separator row
control column alignment.

```markdown
| Species     | Subtype  | Count |
|-------------|----------|------:|
| Influenza A | H1N1     |   142 |
| Influenza A | H3N2     |    87 |
| Influenza B | Victoria |    31 |
```

---

### Block Quotes

Block quotes are prefixed with `>` and render as an indented, visually offset
block — useful for highlighting a caveat or quoting a source.

```markdown
> Influenza B Yamagata has not been detected in global surveillance since 2020
> and may be extinct.
```

---

### Code Blocks

Fenced code blocks are wrapped in triple backticks. Adding a language name
after the opening fence enables syntax highlighting.

````markdown
```bash
quarto render report.qmd
```

```python
print("Bioinformaticians rule!")
```
````

---

### Links and Images

Links and images share a similar syntax. The difference is a leading `!` for
images.

```markdown
[Quarto Gallery](https://quarto.org/docs/gallery/)

![Phylogenetic tree of A(H3N2) viruses.](media/tree.png)
```

The text in square brackets is the link text (or the image's *alt text*,
shown if the image fails to load). The value in parentheses is the
destination — a URL or a file path.

#### Relative Image Paths

When the image path is **relative**, it is resolved from the directory
containing the Markdown file. This is the recommended way to include figures
in a report, because the document and its figures travel together as a
self-contained folder:

```
genome-report/
├── genome-report.md
└── media/
    ├── tree.png
    └── coverage.png
```

In `genome-report.md`:

```markdown
![Phylogenetic tree of A(H3N2) viruses.](media/tree.png)

![Per-sample genome coverage.](media/coverage.png)
```

Pandoc (introduced below) will resolve these paths and either copy the files
into the HTML output directory or embed them directly into the PDF.

---

## Rendering Markdown with Pandoc

[Pandoc](https://pandoc.org) is a command-line tool that converts Markdown
into HTML, PDF, Word, and many other formats. It is the universal converter
that powers Quarto, RMarkdown, and Jupyter Book under the hood, and can be
used directly on its own.

### Installation

```bash
# macOS
brew install pandoc

# Ubuntu / Debian / WSL
sudo apt install pandoc

# For PDF output, a LaTeX engine is also required
sudo apt install texlive-xetex
```

### Rendering to HTML

```bash
pandoc genome-report.md \
  --standalone \
  --embed-resources \
  --toc \
  -o genome-report.html
```

The flags used above are described below:

| Flag                 | Description                                               |
|----------------------|-----------------------------------------------------------|
| `--standalone`       | Produce a complete HTML document (with `<html>` wrapper)  |
| `--embed-resources`  | Inline all images and CSS so the `.html` is self-contained |
| `--toc`              | Generate a table of contents from the headers             |
| `-o`                 | Output file name                                          |

`--embed-resources` is important when sharing the file: it produces a single
`.html` that can be emailed or dropped into a shared drive without any
accompanying `media/` folder.

### Rendering to PDF

```bash
pandoc genome-report.md \
  --pdf-engine=xelatex \
  --toc \
  -o genome-report.pdf
```

Because relative image paths are resolved from the location of the Markdown
file, the same `genome-report.md` that renders to HTML will also render to
PDF with no changes — Pandoc finds `media/tree.png` in both cases.

---

## Example: The Genome Report Template

A ready-to-use surveillance report template is provided for this workshop:

- Download: [genome-report.md]({{ site.baseurl }}/assets/templates/genome-report.md)

The template includes the sections you typically need in a national genomic
surveillance report — executive summary, specimen collection, subtype
distribution, sequencing output, clade distribution, resistance markers,
phylogenetic analysis, data sharing, limitations, and conclusions — all using
only the Markdown syntax covered above.

### Try It

1. Download `genome-report.md` into a new folder.
2. Create a `media/` subfolder and place a figure (e.g., `tree.png`) inside.
3. Fill in the placeholder values for your reporting period.
4. Render to HTML and PDF:

   ```bash
   pandoc genome-report.md --standalone --embed-resources --toc \
     -o genome-report.html

   pandoc genome-report.md --pdf-engine=xelatex --toc \
     -o genome-report.pdf
   ```

5. Open the resulting files and confirm the figure appears in both.

---

## Extending Markdown with Quarto

Everything above produces a *static* report: you fill in the numbers by hand
and re-render. That works well for one-off documents, but surveillance
reporting is repetitive — the same tables and figures are regenerated every
week, month, or season with fresh data.

[Quarto](https://quarto.org) is an open-source publishing system that extends
Markdown with the ability to **execute code inside the document at render
time**. A Quarto document (`.qmd`) is a Markdown file with embedded Python,
R, or Bash chunks. When Quarto renders the document, it runs each chunk and
inserts the computed output — summary statistics, tables, plots — directly
into the report.

For example, the manually filled subtype table from the template:

```markdown
| Type / Subtype      | Count | Percent |
|---------------------|------:|--------:|
| A(H1N1)pdm09        |    42 |   29.6% |
| A(H3N2)             |    87 |   61.3% |
| B/Victoria          |    13 |    9.2% |
```

...can be replaced in a Quarto document with an executable chunk that
computes the same table from a CSV every time the report is rendered:

````markdown
```{python}
import pandas as pd
df = pd.read_csv("data/specimens.csv")
summary = (df["subtype"].value_counts(normalize=False)
             .rename_axis("Subtype").reset_index(name="Count"))
summary["Percent"] = (summary["Count"] / summary["Count"].sum() * 100).round(1)
summary
```
````

With Quarto, the `genome-report.md` workflow extends naturally to an
automated reporting pipeline:

- **Parameterize** the report so the same template can be rendered against
  different countries, seasons, or input files.
- **Compute** counts, percentages, resistance frequencies, and QC metrics
  directly from data files — no manual copy-paste.
- **Regenerate** figures (phylogenetic trees, coverage plots) as part of the
  render.
- **Output** the same document as HTML, PDF, or Word without changing the
  source.

A fully automated Quarto version of the template (`genome_report.qmd`) is
available under `WIP/genome_report/` in this repository for reference.

Pandoc is the foundation; Quarto is what you reach for when the report needs
to run itself.
