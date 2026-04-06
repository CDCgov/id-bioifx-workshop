---
layout: page
title: Reporting with Quarto
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/18-reporting/
---

{: title}

---

## Module Objectives

- Understand the basics of Quarto
- Learning how to develop, automate, and share Quarto reports

---

## Quarto Overview

Quarto is an open-source scientific and technical publishing system built on Markdown and HTML. It lets you create reports using code, producing HTML, PDF, and Word documents from a single source using [`pandoc`](https://pandoc.org).

{% raw %}

<svg width="100%" viewBox="0 0 680 220">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<rect x="40" y="80" width="120" height="56" rx="8" fill="#0C447C" stroke="#0C447C" stroke-width="0.5" opacity="0.5"/>
<text x="100" y="101" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="750" fill="black" font-family="sans-serif">Source Code</text>
<text x="100" y="121" text-anchor="middle" dominant-baseline="central" font-size="12" fill="black" font-family="sans-serif">(.qmd)</text>

<path d="M160 108 L240 108 L240 56 L320 56" fill="none" stroke="black" stroke-width="2" marker-end="url(#arrow)"/>
<path d="M160 108 L320 110" fill="none" stroke="black" stroke-width="2" marker-end="url(#arrow)"/>
<path d="M160 108 L240 108 L240 164 L320 164" fill="none" stroke="black" stroke-width="2" marker-end="url(#arrow)"/>

<rect x="210" y="87" width="68" height="45" rx="11" fill="#0C447C" stroke="#0C447C" stroke-width="0.5"/>
<text x="244" y="100" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="750" fill="white" font-family="sans-serif">Quarto</text>
<text x="244" y="115" text-anchor="middle" dominant-baseline="central" font-size="9" font-weight="500" fill="white" font-family="sans-serif">(Pandoc)</text>

<rect x="320" y="34" width="110" height="44" rx="8" fill="#3B6D11" stroke="#3B6D11" stroke-width="0.5" opacity="0.5"/>
<text x="375" y="56" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="black" font-family="sans-serif">PDF</text>

<rect x="320" y="88" width="110" height="44" rx="8" fill="#702963" stroke="#702963" stroke-width="0.5" opacity="0.5"/>
<text x="375" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="black" font-family="sans-serif">HTML</text>

<rect x="320" y="142" width="110" height="44" rx="8" fill="#633806" stroke="#633806" stroke-width="0.5" opacity="0.5"/>
<text x="375" y="164" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="black" font-family="sans-serif">Word doc</text>

</svg>

{% endraw %}

Examples of the various document types that can be created by Quarto can be found in the [Quarto Gallery](https://quarto.org/docs/gallery/).

---

## Markdown Basics

Markdown is a lightweight text formatting language that serves as a simpler alternative to HTML. Quarto uses Pandoc under the hood to convert Markdown into HTML, PDF (via LaTeX), and other formats. The following section covers common Markdown syntax used in Quarto reports.

---

### Plain Text, Headers, and Lists

The example below shows how markdown can be used to structure a document.

#### Markdown

```markdown
# Influenza
## A / B
### Subtypes / Lineages
Flu A and B use different classification schemes:
- **Flu A** uses *subtypes* (e.g., H5N1)
- **Flu B** uses *lineages* (e.g., Yamagata).
```

**Plain text:**
Plain text is any content written without formatting symbols. In the example above, the sentence `Flu A and B use different classification schemes:` is plain text — it renders as a regular paragraph with no special styling.

**Headers:**
Headers are created using `#` symbols. A single `#` produces the largest heading (H1), `##` produces H2, and `###` produces H3. In the example, `# Influenza` is the document title, `## A / B` is a section heading, and `### Subtypes / Lineages` is a subsection heading.

**Lists:**
Unordered lists are created with a `-` at the start of each line. Items can contain inline formatting — in the example, `**Flu A**` renders as bold and `*subtypes*` renders as italic. Each `-` becomes a bullet point in the rendered output.

#### HTML

The equivalent code written in HTML format:

```html
<h1>Influenza</h1>
<h2>A / B</h2>
<h3>Subtypes / Lineages</h3>
<p>Flu A and B use different classification schemes:</p>
<ul>
  <li><strong>Flu A</strong> uses <em>subtypes</em> (e.g., H5N1)</li>
  <li><strong>Flu B</strong> uses <em>lineages</em> (e.g., Yamagata).</li>
</ul>
```

#### Rendered Output

<iframe srcdoc="
  <h1>Influenza</h1>
  <h2>A / B</h2>
  <h3>Subtypes / Lineages</h3>
  <p>Flu A and B use different classification schemes:</p>
  <ul>
    <li><strong>Flu A</strong> uses <em>subtypes</em> (e.g., H5N1)</li>
    <li><strong>Flu B</strong> uses <em>lineages</em> (e.g., Yamagata).</li>
  </ul>
" width="100%" style="border: 1px solid #ccc; border-radius: 6px;"
  onload="this.style.height = this.contentDocument.body.scrollHeight + 30 + 'px'">
</iframe>

---

### Tables & Figures

#### Markdown

```markdown
|  Species  | Subtype  |
|-----------|----------|
|Influenza A|  H1N1    |
|Influenza A|  H3N2    |
|Influenza B|Yamagata  |
|Influenza B|Victoria  |

![](https://www.cdc.gov/bird-flu/media/images/2024/05/flu-virus.jpg)
```

**Tables:**
Tables can be created using a combination of pipes (`|`) and dashes (`-`).

**Figures:**
Figures can be embedded by referencing a URL or relative path (e.g., `report/media/tree.jpg`). The general syntax is `![alt text](path/to/image.png)`, where `alt text` is the alternative text shown if the image fails to load and `path/to/image.png` is the image source.

#### HTML

The equivalent code written in HTML format:

```html
<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Subtype</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Influenza A</td><td>H1N1</td></tr>
    <tr><td>Influenza A</td><td>H3N2</td></tr>
    <tr><td>Influenza B</td><td>Yamagata</td></tr>
    <tr><td>Influenza B</td><td>Victoria</td></tr>
  </tbody>
</table>

<img src="https://www.cdc.gov/bird-flu/media/images/2024/05/flu-virus.jpg" alt="">
```

#### Rendered Output

<iframe srcdoc="
  <table>
    <thead>
      <tr>
        <th>Species</th>
        <th>Subtype</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Influenza A</td><td>H1N1</td></tr>
      <tr><td>Influenza A</td><td>H3N2</td></tr>
      <tr><td>Influenza B</td><td>Yamagata</td></tr>
      <tr><td>Influenza B</td><td>Victoria</td></tr>
    </tbody>
  </table>
  <img src='https://www.cdc.gov/bird-flu/media/images/2024/05/flu-virus.jpg' alt='Flu virus'>
" width="100%" style="border: 1px solid #ccc; border-radius: 6px;"
  onload="this.style.height = this.contentDocument.body.scrollHeight + 30 + 'px'">
</iframe>

---

### Block Quotes & Callouts

Block quotes and callouts can be used to distinguish and emphasize specific text.

#### Markdown

```markdown
<!-- Block Quote -->
> Influenza B Yamagata may be *extinct*!

<!-- Callout -->
::: {.callout-note}
Influenza B Yamagata may be *extinct*!
:::
```

**Block quote:**
Block quotes are denoted by a `>` at the start of a line. This renders as an indented, visually offset block — typically with a vertical bar on the left side.

**Callouts:**
Callouts are stylized blocks created in Quarto using fenced divs with a callout class. These are not standard Markdown but a specialized Quarto extension. There are five callout styles available: `.callout-note`, `.callout-tip`, `.callout-warning`, `.callout-important`, and `.callout-caution`.

#### HTML

The equivalent code written in HTML format:

```html
<!-- Block Quote -->
<blockquote style="
  border-left: 4px solid #ccc;
  margin: 1em 0;
  padding: 0.5em 1em;
  color: #555;
  font-style: italic;
">
  Influenza B Yamagata may be <em>extinct</em>!
</blockquote>

<!-- Callout -->
<div style="
  border: 1px solid #bee3f8;
  border-left: 4px solid #3b9ede;
  border-radius: 4px;
  padding: 0.75em 1em;
  margin: 1em 0;
  background-color: #ebf8ff;
">
  <div style="
    font-weight: 600;
    color: #2b6cb0;
    margin-bottom: 0.4em;
    display: flex;
    align-items: center;
    gap: 6px;
  ">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#3b9ede" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"/>
      <line x1="12" y1="8" x2="12" y2="12"/>
      <line x1="12" y1="16" x2="12.01" y2="16"/>
    </svg>
    Note
  </div>
  <div style="color: #2d3748;">
    Influenza B Yamagata may be <em>extinct</em>!
  </div>
</div>
```

#### Rendered Output

<iframe srcdoc="
  <blockquote style='
    border-left: 4px solid #ccc;
    margin: 1em 0;
    padding: 0.5em 1em;
    color: #555;
    font-style: italic;
  '>
    Influenza B Yamagata may be <em>extinct</em>!
  </blockquote>
  <div style='
    border: 1px solid #bee3f8;
    border-left: 4px solid #3b9ede;
    border-radius: 4px;
    padding: 0.75em 1em;
    margin: 1em 0;
    background-color: #ebf8ff;
  '>
    <div style='
      font-weight: 600;
      color: #2b6cb0;
      margin-bottom: 0.4em;
      display: flex;
      align-items: center;
      gap: 6px;
    '>
      <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='#3b9ede' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
        <circle cx='12' cy='12' r='10'/>
        <line x1='12' y1='8' x2='12' y2='12'/>
        <line x1='12' y1='16' x2='12.01' y2='16'/>
      </svg>
      Note
    </div>
    <div style='color: #2d3748;'>
      Influenza B Yamagata may be <em>extinct</em>!
    </div>
  </div>
" width="100%" style="border: 1px solid #ccc; border-radius: 6px;"
  onload="this.style.height = this.contentDocument.body.scrollHeight + 30 + 'px'">
</iframe>

---

### Code Blocks & Code Chunks

#### Markdown

````markdown
<!-- Code Block (Without Brackets) -->
```python
print("Bioinformaticians rule, epis drool!")
```

<!-- Code Chunk (With Brackets) -->
```{python}
print("Bioinformaticians rule, epis drool!")
```
````

**Code block:**
Code blocks are formatted, syntax-highlighted snippets of code displayed statically in the document, purely for presentation purposes; the code is not executed.

**Code chunk:**
Code chunks are executable blocks of code that Quarto runs at render time, with the output (tables, plots, printed results) embedded directly in the document alongside the code.

#### HTML

The equivalent code written in HTML format:

```html
<!-- Code Block (Without Brackets) -->
<pre><code class="language-python">print("Bioinformaticians rule, epis drool!")</code></pre>

<!-- Code Chunk (With Brackets) -->
<pre style="border: 1px solid #ccc; border-radius: 4px; padding: 1em; background-color: #f8f8f8;">
  <code class="language-python">print("Bioinformaticians rule, epis drool!")</code>
</pre>
<div style="
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 4px 4px;
  padding: 0.5em 1em;
  background-color: #f0f0f0;
  font-family: monospace;
  font-size: 0.9em;
  color: #555;
">
  Bioinformaticians rule, epis drool!
</div>
```

#### Rendered Output

<iframe srcdoc="
  <pre><code class='language-python'>print('Bioinformaticians rule, epis drool!')</code></pre>
  <pre style='border: 1px solid #ccc; border-radius: 4px; padding: 1em; background-color: #f8f8f8;'>
    <code class='language-python'>print('Bioinformaticians rule, epis drool!')</code>
  </pre>
  <div style='
    border: 1px solid #ccc;
    border-top: none;
    border-radius: 0 0 4px 4px;
    padding: 0.5em 1em;
    background-color: #f0f0f0;
    font-family: monospace;
    font-size: 0.9em;
    color: #555;
  '>
    Bioinformaticians rule, epis drool!
  </div>
" width="100%" style="border: 1px solid #ccc; border-radius: 6px;"
  onload="this.style.height = this.contentDocument.body.scrollHeight + 30 + 'px'">
</iframe>

---

## Code Chunks & Automation

Code chunks can be used to automate reporting processes, creating reproducible and efficient reporting templates. The content below describes general use of code chunks for automation purposes.

---

### Execution Settings

Execution settings control how and when code chunks run in a document. They determine whether code is evaluated, whether output (results, warnings, messages) is displayed, and how figures are rendered. These settings can be applied globally to affect the entire document or locally to override behavior for individual chunks.

#### Common Execution Settings

| Option | Behavior |
|---|---|
| `eval` | Run code |
| `echo` | Show code |
| `output` | Show code result |
| `include` | Run code but hide all |
| `warning` | Show code warnings |
| `message` | Show code messages |
| `error` | Show code errors |
| `cache` | Cache execution result |

#### Example Usage

````markdown
```{python}
#| echo: false
#| output: true

print("Bioinformaticians rule, epis drool!")
```
````

In this example, the result of the code execution (`Bioinformaticians rule, epis drool!`) would be rendered but the code (`print("Bioinformaticians rule, epis drool!")`) would not.

Execution settings can also be applied globally in the front matter under the `execute` field, which sets the default behavior for all chunks in the document:

```yaml
execute:
  echo: false
  warning: false
  message: false
```

Individual chunks can override global settings using the `#|` syntax shown above.

---

### Rendering Dataframes to Tables

Structured data can be rendered into formatted tables automatically by Quarto using R or Python. For R, this is handled using the `kable` function from the `knitr` package. For Python, this is handled by the `pandas` module. Examples of each are shown below.

#### R Dataframes with `kable`

````markdown
```{r}
df <- read.csv("results.csv")
knitr::kable(df)
```
````

#### Python Dataframes with `pandas`

````markdown
```{python}
import pandas as pd

df = pd.read_csv("results.csv")
df
```
````

By default, R renders dataframes as formatted HTML tables automatically via `knitr`. Python displays dataframes as plain text unless Jupyter is used, in which case they render as HTML tables. To align Python's default behavior with R's, the `html` dataframe display option can be set in the document's YAML front matter.

---

### Multi-language Reports

Multiple coding languages can be used in a single Quarto document, including Python, R, Bash, and SQL. By default, Quarto runs Python via R using the `reticulate` package, which allows objects created in an R chunk to be accessed in a subsequent Python chunk. To run Python natively without `reticulate`, set `python.reticulate = FALSE` in the chunk options — note that chunks running in native Python mode will not have access to objects created in R chunks.

````markdown
```{r}
<!-- Step 1. Create a dataframe object in R -->
df <- readr::read_csv("results.csv")
```

```{python}
<!-- Step 2a. Preview the dataframe in Python (via reticulate — has access to df) -->
df.head()
```

```{python, python.reticulate = FALSE}
<!-- Step 2b. This will fail — native Python mode has no access to the R df object -->
df.head()
```
````

---

## Front Matter

Front matter defines global document configuration and metadata at the start of a Quarto document using YAML syntax, delimited by `---` at the top of the file. It controls everything from document appearance to execution behavior.

{% raw %}
```markdown
---
title: "Influenza Report"
author:
  - name: Jane Doe
date: today
format:
  html:
    embed-resources: true
execute:
  echo: false
params:
  species: Influenza A
  subtype: H1N1
---

<!-- FRONT MATTER ENDS & REPORT BEGINS -->

# Overview
This report is about {{< meta params.species >}} {{< meta params.subtype >}} ...
```
{% endraw %}

Front matter fields fall into three categories:

- **Metadata** — fields like `title`, `author`, and `date` are automatically rendered at the top of the document.
- **Global configs** — fields like `format` and `execute` control how the document is rendered and how code chunks behave throughout.
- **Custom parameters** — the `params` field accepts user-defined values that can be referenced anywhere in the document using the {% raw %}`{{< meta params.field >}}`{% endraw %} shortcode syntax, making it easy to reuse the same template across different reporting scenarios.

---

## Report Rendering & Development

### Interactive Development Environments

IDEs are ideal for report development or for reports that require manual edits. Many options exist including RStudio, Positron, and Visual Studio Code (VS Code). All three support Quarto natively with features such as syntax highlighting, chunk execution, and live preview. The example below shows how you can edit and render Quarto reports in VS Code.

!["quarto-img01"](../../assets/images/quarto-img01.png)

---

### Basic Command-line Usage

While it is possible to render Quarto reports using a graphical user interface (GUI), rendering from the command line provides greater flexibility and is better suited for automation. The example below demonstrates the basic command for rendering a report from the command line.

```bash
quarto render \
    -o $(date +"%Y-%m-%d")_report.html \
    --execute-params params.yml \
    report.qmd
```

The flags used in this command are described below:

| Flag | Description |
|---|---|
| `-o` | Output file name |
| `--execute-params` | Path to a YAML file containing parameter values |

Parameters defined in the front matter can be overridden at render time using the `--execute-params` flag and a YAML file. This is useful for running the same template against different inputs without modifying the source document.

```yaml
# params.yml
params:
  input_file: "2026_results.csv"
```

The corresponding front matter and chunk that consumes the parameter:

```markdown
---
params:
  input_file: "results.csv"
---
```

````markdown
```{r}
df <- read_csv(params$input_file)
```
````

When rendered with `--execute-params params.yml`, the value `"2026_results.csv"` will override the default `"results.csv"` defined in the front matter.

---

### Sharing HTML Reports

It is necessary to embed resources when sharing HTML documents created with Quarto to ensure consistent formatting and render behavior. This can be accomplished using the `embed-resources` parameter, as shown below.

```yaml
---
format:
  html:
    embed-resources: true
---
```

Additionally, the rendered HTML file itself must be shared directly — not a localhost URL (e.g., `http://localhost:7779/genome_report.html`). Since the document is not hosted on a server, a localhost link will only work on the machine that rendered it and will be inaccessible to others.