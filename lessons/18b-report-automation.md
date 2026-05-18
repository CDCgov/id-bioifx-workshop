---
layout: page
title: Report Automation with Quarto
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/18b-report-automation/
---

{: title}

---
<p style="color: #015CAE; font-size: 19px;">Content developed by Jared Johnson</p>

## Module Objectives

- Understand how Quarto can be used to automate routine reports

## What is Quarto?

[Quarto](https://quarto.org) is an open-source publishing system that extends Markdown with the ability to **execute code inside the document at render time**. A Quarto document (`.qmd`) is a Markdown file with embedded Python, R, or Bash chunks. When Quarto renders the document, it runs each chunk and inserts the computed output — summary statistics, tables, plots — directly into the report.

## Rendering Reports with Quarto

Quarto documents can be rendered through several tools depending on your workflow.

**VS Code** — The Quarto extension for VS Code provides a preview button and render command directly in the editor. You can preview the output in a side panel as you write and render to any format defined in the front matter without leaving the editor.

**RStudio** — RStudio has built-in Quarto support. A **Render** button appears at the top of the editor when a `.qmd` file is open, replacing the familiar Knit button from R Markdown. RStudio also provides a visual editor mode for Quarto documents if you prefer a word-processor-style interface.

**Command Line** — Any Quarto document can be rendered from the terminal using the `quarto render` command:

<pre><code class="language-bash">
quarto render document.qmd                  # renders to format(s) defined in front matter
quarto render document.qmd --to pdf         # override to a specific format
quarto render document.qmd --to html,pdf    # render multiple formats at once
</code></pre>

The command line approach is particularly useful for automation or when a GUI isn't available.

All three methods ultimately invoke the same rendering pipeline, so the output is identical regardless of which you use.

## Front Matter

Quarto builds on the front matter used by Pandoc. Additional features specific to Quarto include the ability to specify the document type(s) to create when the report is rendered, along with parameters that control how code blocks are executed. Below are examples of common front matter fields used in Quarto documents.

### Document Formatting

The example below shows how to use front matter to specify both global and format-specific parameters. The table of contents (`toc`) and callout appearance are specified for all formats (global), whereas the [cosmo](https://bootswatch.com/cosmo/) theme is specified for the HTML version and document class and margins are specified for the PDF version. When both `html` and `pdf` formats are included, a version of each document type is created upon rendering.

{% include tip.html content="Learn more about Quarto themes [here](https://quarto.org/docs/output-formats/html-themes.html)" %}

<pre><code class="language-yaml">
---
# applied to all formats (global)
toc: true                      # table of contents
callout-appearance: simple

# applied to specific formats
format:
  html:                        # create HTML document
    theme: cosmo
  pdf:                         # create PDF document
    documentclass: report
    margin-left: 1in
---
</code></pre>

### Code Chunk Execution

This example demonstrates how code chunk parameters can be specified globally in the front matter. These will be used as the default parameters unless overridden in an individual code block. These parameters are covered in a later section.

<pre><code class="language-yaml">
---
execute:
  echo: false
  warning: false
  cache: true
---
</code></pre>

### Custom Parameters

Quarto also supports custom parameters that can be specified in the front matter and referenced throughout the document — including in code chunks — using the `params` variable (e.g., `tree <- read,tree(params$tree_file)`). These can be overridden from the command line using the `--execute-params` flag (e.g., `--execute-params tree_file:/home/tree.nwk`). The example below demonstrates how to parameterize file paths used by a report.

<pre><code class="language-yaml">
---
params:
  tree_file: /path/to/tree.nwk
  mira_summary: /path/to/mira-summary.csv
---
</code></pre>

## Code Chunks

Code chunks are code blocks that Quarto can execute at render time. The output of a code chunk can be optionally inserted into the rendered document, which is extremely useful when creating reports that use different inputs each time they are rendered.

### Anatomy of a Code Chunk

The example below shows the general anatomy of a code chunk. The key difference between a **code block** and a **code chunk** is that the programming language is wrapped in curly brackets (`{}`) when specifying a **code chunk**. Code chunks also accept execution settings, which can be specified within the brackets or using the `#|` format, as shown below.

<pre><code class="language-markdown">
```{python}
#| echo: false
#| output: true

print("Bioinformaticians rule, epis drool!")
```
</code></pre>

Execution settings control how and when code chunks run in a document. They determine whether code is evaluated, whether output (results, warnings, messages) is displayed, and how figures are rendered. These settings can be applied _globally_ to affect the entire document or _locally_ to override behavior for individual chunks.

#### Common Execution Settings

| Option    | Behavior                    |
|-----------|-----------------------------|
| `eval`    | Run code                    |
| `echo`    | Show code                   |
| `output`  | Show code result            |
| `include` | Run code but hide all output |
| `warning` | Show code warnings          |
| `message` | Show code messages          |
| `error`   | Show code errors            |
| `cache`   | Cache execution result      |

In the example above, the result of code execution (`Bioinformaticians rule, epis drool!`) would be rendered, but the code itself (`print(...)`) would not.

### Execution Engines

Code chunks support multiple languages including `R`, `Python`, and `Bash`. R and Bash are executed by default using the [Knitr](https://yihui.org/knitr/) engine, whereas Python is executed using [Jupyter](https://jupyter.org). It is also possible to execute Python using Knitr via the [reticulate](https://rstudio.github.io/reticulate/) package. When using `reticulate`, objects can be shared between R and Python code chunks — see the example below:

<pre><code class="language-markdown">
```{r}
# Step 1. Create a dataframe object in R
df <- readr::read_csv("results.csv")
```

```{python}
# Step 2a. Preview the dataframe in Python (via reticulate — has access to df)
df.head()
```

```{python, python.reticulate = FALSE}
# Step 2b. This will fail — native Python mode has no access to the R df object
df.head()
```
</code></pre>

### Importing Software Packages and Modules

Software dependencies, including R packages and Python modules, can be imported within code chunks. Once imported, these dependencies are available to all subsequent code chunks in the report (applied globally). Consolidating all imports into a single code chunk can simplify dependency management. This "dependency chunk" can be configured to be excluded from the rendered output — see the example below:

<pre><code class="language-markdown">
```{python}
#| include: false
import numpy as np
import pandas as pd
```
</code></pre>

Note that Bash code chunks are executed as independent subprocesses. Any variables or dependencies defined in one Bash chunk will **not** be available to subsequent Bash chunks.

### Common Usage

The examples below demonstrate how code chunks can be used to automatically integrate data elements into a report — including tables, figures, and inline text — using R and Python.

#### Dataframes and Tables

Dataframes can be automatically rendered as Markdown tables using the `kable` function from the `knitr` package in R, or using the `pandas` module in Python. Additional styling can be applied to R tables using the `kableExtra` package.

_R Example_
<pre><code class="language-markdown">
```{r}
df <- read.csv("data.csv")
knitr::kable(df)
```
</code></pre>

_Python Example_
<pre><code class="language-markdown">
```{python}
import pandas as pd

df = pd.read_csv("data.csv")
df
```
</code></pre>

#### Figures

Figures can be automatically embedded in multiple ways. Many packages and modules support direct embedding from an object or variable, including the R `plot` and `ggplot2` packages and the Python `plotly` module. <br>

_R Example_
<pre><code class="language-markdown">
```{r}
plot(df$x, df$y)

ggplot(df, aes(x = x, y = y)) +
  geom_point()
```
</code></pre>

_Python Example_
<pre><code class="language-markdown">
```{python}
import plotly.express as px

fig = px.scatter(df, x="x", y="y")
fig.show()
```
</code></pre>

Alternatively, figures can be exported by a code chunk and then embedded by referencing the exported file using standard Markdown syntax — e.g., `![](/path/to/exported/figure.jpg)`.

#### Inline Text

Variables from code chunks can also be rendered within inline text. This is useful when integrating computed statistics into a narrative. In the example below, the `df` object contains 100 rows, where each row represents a unique sample.

_Python Example_
> This report includes \`{python} len(df)\` samples.

_R Example_
> This report includes \`r nrow(df)\` samples.

_Rendered Output_
> This report includes 100 samples.

Note that Python requires curly brackets when making inline references, whereas R does not.

## Example Report

An example report can be found [here](https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/report_automation/genome_report/). The files used to create this report are described below:

<pre><code class="language-bash">
├── _quarto.yml
├── data
│   ├── mira
│   │   ├── mira_example_mira_output_2_summary-2.csv
│   │   └── mira_example_mira_output_summary-2.csv
│   └── samplesheet.csv
├── genome_report.html
├── genome_report.qmd
└── src
    └── report
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
| <a href="../../practical/report_automation/genome_report/genome_report.html" target="_blank"><code>genome_report.html</code></a> | Rendered output of `quarto_report.qmd` in HTML format. This is the final report that would be shared. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/report_automation/genome_report/genome_report.qmd" target="_blank"><code>genome_report.qmd</code></a> | Quarto markdown file that contains the markdown and Quarto syntax used to create the rendered report. This file relies on information in `data/`, `src/`, and the `_quarto.yml` file. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/report_automation/genome_report/data/" target="_blank"><code>data/</code></a> | A directory containing sample data used to generate the report. This example includes a samplesheet containing sample information, MIRA output, and a tree file. This data would likely change each time the report was generated. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/report_automation/genome_report/src/" target="_blank"><code>src/</code></a> | A directory containing custom Python code. This code is imported as a standard module within the report script and executed within code chunks. |
| <a href="https://github.com/CDCgov/id-bioifx-workshop/blob/main/practical/report_automation/genome_report/_quarto.yml" target="_blank"><code>_quarto.yml</code></a> | A config file used to specify front matter parameters that should be updated each time the report is executed. This is separate from static front matter parameters that are hard coded within `genome_report.qmd`. This file can be used in the following manner: `quarto render genome_report.qmd --execute-params _quarto.yml`. |