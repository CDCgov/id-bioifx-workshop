---
layout: page
title: End-to-End Practical
sidebar: workshop_sidebar
topnav: topnav
permalink: /practical/end-to-end/
---

## End-to-End Influenza Bioinformatics Practical

This hands-on practical challenges you to work through a complete influenza bioinformatics workflow — from downloading raw sequencing data through assembly, quality control, phylogenetic analysis, and reporting. Each section builds on skills learned in previous workshop lessons and maps to operational milestones defined in the [post-bfxwkshp-schema project](https://github.com/nbx0/post-bfxwkshp-schema/milestones).

You will **not** be given step-by-step commands. Instead, each part poses questions and challenges for you to solve using the skills and tools you've learned. Tool suggestions are provided where helpful.

### Learning Objectives

By the end of this practical, you will be able to:

- Download FASTQ data from NCBI SRA
- Manipulate filenames and organize a working directory using bash
- Run an influenza genome assembly pipeline
- Interpret QC results to separate passing and failing samples
- Extract specific gene segment sequences from assembly output
- Perform phylogenetic analysis and visualize results
- Generate a reproducible summary report

---

## Prerequisites

Before starting, ensure you have completed (or are comfortable with) these workshop modules:

| Skill Area | Lesson |
|---|---|
| Command line basics | [Intro to CLI]({{ site.baseurl }}/lessons/05-cli-intro/) |
| Bash scripting | [CLI Exercises]({{ site.baseurl }}/lessons/06-cli-intro-exercises/) |
| Environments & containers | [Computer Environments]({{ site.baseurl }}/lessons/09-computer-environments/) / [Containers]({{ site.baseurl }}/lessons/10-containers-registries/) |
| Genome assembly concepts | [Genome Assembly and MIRA-NF]({{ site.baseurl }}/lessons/11-genome-assembly/) |
| Phylogenetics concepts | [Phylogenetics]({{ site.baseurl }}/lessons/15-phylogenetics/) |
| Reporting | [Reporting with Quarto]({{ site.baseurl }}/lessons/18-reporting/) |
| Workflow pipelines | [Workflow Pipelines]({{ site.baseurl }}/lessons/19-workflow-pipelines/) |

---

## Part 1 — Data Acquisition

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/3'>Phase 2: Operational Readiness</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/11'>Issue #11: Identify sequence data sources</a>." %}

Public sequencing data are available through NCBI's Sequence Read Archive (SRA). Your goal is to download paired-end FASTQ files for influenza samples under BioProject **PRJNA1437047** that match the pattern `H1_*`.

**Suggested tools:** `sra-toolkit` (`prefetch`, `fasterq-dump`), Entrez Direct (`esearch`, `efetch`), [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/)

### Questions & Challenges

1. How can you identify which SRA run accessions belong to BioProject PRJNA1437047 and have sample names matching `H1_*`? Consider both browser-based and command-line approaches.

2. Once you have an accession list, how would you download paired-end FASTQ files for all of them? Think about what flag controls paired-end splitting.

3. How would you verify that every accession was successfully downloaded with both read files present?

{% include note.html content="Record the number of accessions found and the total number of FASTQ files downloaded. You will need these counts later." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> You should have two FASTQ files per SRA accession (forward and reverse reads). Confirm the count matches 2× the number of accessions in your list.
</div>

---

## Part 2 — File Renaming and Directory Setup

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/1'>Phase 0: Governance &amp; Operations</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/5'>Issue #5: Define metadata standards and change management for pipelines</a>." %}

MIRA-NF expects input files to follow a specific naming convention tied to a **samplesheet**. The SRA-downloaded files are named by run accession (e.g., `SRR12345678_1.fastq`), but your lab tracks samples with internal IDs. You need to rename the files and prepare the directory structure MIRA-NF expects.

**Suggested tools:** bash loops (`while`, `for`), `mv`, `read`, I/O redirection, `basename`, `realpath`

### Questions & Challenges

1. Design a mapping between SRA accessions and your desired sample IDs. What file format would be easy to parse in a bash loop? How would you structure it?

2. Write a bash loop that reads your mapping file and renames both the R1 and R2 FASTQ files for each accession. How can you handle the case where an expected file is missing?

3. After renaming, how would you confirm that no SRR-prefixed files remain and all files have the new names?

4. MIRA-NF requires a CSV samplesheet with columns `sample`, `fastq_1`, `fastq_2`. How would you generate this programmatically from your renamed files? Think about what path format (relative vs. absolute) the pipeline expects.

5. What directory layout does MIRA-NF expect? Set up the working directory accordingly.

{% include note.html content="Refer to the <a href='https://github.com/CDCgov/MIRA-NF'>MIRA-NF documentation</a> for samplesheet format requirements." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> Your samplesheet should list every sample with paths to both R1 and R2 FASTQ files. Each row should have three comma-separated fields.
</div>

---

## Part 3 — Genome Assembly with MIRA-NF

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/2'>Phase 1: Setup &amp; Validation</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/9'>Issue #9: Configure computational environment</a> and <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/10'>Issue #10: Validate analysis pipeline</a>." %}

[MIRA-NF](https://github.com/CDCgov/MIRA-NF) is the CDC's influenza genome assembly and QC pipeline built on Nextflow. It performs reference-based assembly and produces consensus sequences and quality metrics.

**Suggested tools:** `nextflow`, [MIRA-NF](https://github.com/CDCgov/MIRA-NF), container runtime (`docker` or `singularity`)

### Questions & Challenges

1. What are the prerequisites for running a Nextflow pipeline? Verify that the required tools are available in your environment.

2. What are the key input parameters MIRA-NF needs? How do you specify the samplesheet, output directory, and execution profile?

3. Run MIRA-NF on your samples. Which `-profile` is appropriate for your compute environment?

4. Once the pipeline completes, explore the output directory. What types of files were generated? Identify where the consensus sequences, QC metrics, and any summary reports are located.

{% include important.html content="Assembly may take several minutes per sample. Monitor pipeline progress as it runs." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> The pipeline should complete successfully for all samples. Note any samples that caused errors during execution.
</div>

---

## Part 4 — MIRA QC: Pass vs. Fail

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/3'>Phase 2: Operational Readiness</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/12'>Issue #12: Define acceptance/rejection criteria</a> and <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/4'>Issue #4: Implement continuous monitoring metrics</a>." %}

MIRA-NF generates quality metrics for each assembled segment. Your task is to determine which samples pass QC and which fail.

**Suggested tools:** `awk`, `grep`, `cut`, `sort`, standard bash text processing

### Questions & Challenges

1. Locate and examine the QC summary output from MIRA-NF. What columns/metrics are reported? What does each metric tell you about assembly quality?

2. What thresholds would you use to define a "passing" assembly? Consider genome completeness, coverage depth, and ambiguous base counts. Justify your choices.

3. Using bash text-processing tools, separate your samples into two lists: those that pass QC and those that fail. Save each list to a file.

4. How many samples passed? How many failed? Are there any patterns in the failures (e.g., specific segments, low input material)?

{% include warning.html content="The specific column layout of the QC summary depends on your MIRA-NF version. Inspect the header row before writing any filtering commands." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> You should have two files listing sample IDs — one for passing samples and one for failing samples. Record these counts for your final report.
</div>

---

## Part 5 — Extracting HA Sequences from MIRA Output

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/3'>Phase 2: Operational Readiness</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/14'>Issue #14: Develop SOPs</a>." %}

For phylogenetic analysis, you need only the **HA (hemagglutinin)** segment consensus sequences from samples that passed QC. HA is segment 4 for influenza A.

**Suggested tools:** `grep`, `awk`, `find`, FASTA-aware text parsing

### Questions & Challenges

1. How does MIRA-NF organize its consensus FASTA output — per-segment files, per-sample files, or a combined multi-segment FASTA? Explore the results directory to find out.

2. Examine the FASTA headers. What naming convention is used? How can you identify HA sequences from the headers?

3. Extract only the HA consensus sequences from QC-passing samples into a single FASTA file. Consider how to handle multi-line FASTA format when filtering by header.

4. Validate the extracted sequences. How many HA sequences do you have? What is the expected length for a full-length H1 HA coding sequence (~1,701 nt)? Are any sequences suspiciously short?

{% include note.html content="HA full-length coding sequences are approximately 1,701 nucleotides for H1. Sequences significantly shorter may indicate incomplete assembly." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> You should have a single FASTA file containing one HA consensus sequence per QC-passing sample.
</div>

---

## Part 6 — Phylogenetic Analysis with Nextstrain

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/2'>Phase 1: Setup &amp; Validation</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/10'>Issue #10: Validate analysis pipeline</a> and <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/3'>Phase 2: Operational Readiness</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/15'>Issue #15: Implement automated workflows</a>." %}

[Nextstrain](https://nextstrain.org/) provides tools for phylogenetic analysis and visualization of pathogen genomic data. The core command-line toolkit is [Augur](https://docs.nextstrain.org/projects/augur/), and interactive trees are viewed in [Auspice](https://auspice.us/).

**Suggested tools:** `augur` (align, tree, refine, ancestral, translate, export), `auspice`

### Questions & Challenges

1. **Metadata:** Nextstrain workflows require a metadata TSV. What fields are needed at minimum? Create a metadata file for your samples with appropriate strain names, collection dates, and geographic info.

2. **Reference sequence:** You need an HA reference for alignment. What is a suitable reference strain for H1N1pdm09? Where can you obtain the reference FASTA and GenBank annotation?

3. **Alignment:** Align your HA sequences against the reference. Which `augur` subcommand handles this? What options control gap handling?

4. **Tree building:** Generate a phylogenetic tree from the alignment. How do you build a raw tree and then refine it with temporal information? What does the `--timetree` option do?

5. **Annotation (optional):** Can you reconstruct ancestral sequences and translate mutations onto the tree? What additional inputs does this require?

6. **Export and visualization:** Export the tree for Auspice viewing. What is the output format? How do you launch Auspice locally, or alternatively, use the hosted viewer at [auspice.us](https://auspice.us/)?

7. Explore the interactive tree. What can you learn about the relationships between your samples? Are there any obvious outliers or clusters?

{% include important.html content="You will need an HA reference sequence and GenBank annotation file. For H1N1pdm09, a common reference is A/California/07/2009." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> You should be able to view an interactive phylogenetic tree of your H1 HA sequences with branch lengths, mutations, and metadata annotations.
</div>

---

## Part 7 — Reporting with Quarto

{% include tip.html content="This section relates to <a href='https://github.com/nbx0/post-bfxwkshp-schema/milestone/3'>Phase 2: Operational Readiness</a> — <a href='https://github.com/nbx0/post-bfxwkshp-schema/issues/17'>Issue #17: Define report templates</a>." %}

[Quarto](https://quarto.org/) is a scientific publishing system for rendering reproducible reports from markdown and code. Your goal is to produce an HTML report summarizing the entire analysis.

**Suggested tools:** `quarto`, `.qmd` format

### Questions & Challenges

1. Create a Quarto document (`.qmd`) that serves as your analysis report. What YAML front matter fields control the title, author, output format, and table of contents?

2. Your report should include sections covering:
   - **Data acquisition:** How many samples were downloaded? From which BioProject?
   - **Assembly:** What pipeline was used? What were the key parameters?
   - **QC summary:** How many passed/failed? Include a summary table.
   - **HA extraction:** How many HA sequences were obtained?
   - **Phylogenetics:** Describe the analysis and include a screenshot or embedded visualization of the tree.
   - **Conclusions:** Key findings, notable mutations, QC failure patterns, phylogenetic observations.

3. How do you include bash code chunks in a Quarto document? How do `echo` and `eval` options control what appears in the rendered output?

4. Render the report to HTML. Review and iterate on the content.

{% include note.html content="Quarto code chunks can be set to <code>eval: true</code> to execute live during rendering (requires all data to be present) or <code>eval: false</code> for a static template." %}

<div class="bs-callout bs-callout-info">
<strong>Checkpoint:</strong> You should have a rendered HTML report that documents the full end-to-end workflow and results.
</div>

---

## Milestone Reference Summary

The exercises in this practical map to the following milestones and issues in the [post-bfxwkshp-schema](https://github.com/nbx0/post-bfxwkshp-schema/milestones) project:

### [Phase 0: Governance & Operations](https://github.com/nbx0/post-bfxwkshp-schema/milestone/1)

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| [#1](https://github.com/nbx0/post-bfxwkshp-schema/issues/1) | Define turnaround time targets for analysis and reporting | Parts 3–7 (overall workflow timing) |
| [#2](https://github.com/nbx0/post-bfxwkshp-schema/issues/2) | Define sample prioritization criteria | Part 4 (QC pass/fail triage) |
| [#3](https://github.com/nbx0/post-bfxwkshp-schema/issues/3) | Define contingency plans for pipeline/infrastructure failure | Part 3 (pipeline execution) |
| [#4](https://github.com/nbx0/post-bfxwkshp-schema/issues/4) | Implement continuous monitoring metrics | Part 4 (QC metrics review) |
| [#5](https://github.com/nbx0/post-bfxwkshp-schema/issues/5) | Define metadata standards and change management for pipelines | Part 2 (file naming/metadata) |

### [Phase 1: Setup & Validation](https://github.com/nbx0/post-bfxwkshp-schema/milestone/2)

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| [#6](https://github.com/nbx0/post-bfxwkshp-schema/issues/6) | Define computational infrastructure | Parts 1, 3 (tool setup) |
| [#7](https://github.com/nbx0/post-bfxwkshp-schema/issues/7) | Implement reproducible environments | Part 3 (Nextflow profiles, containers) |
| [#8](https://github.com/nbx0/post-bfxwkshp-schema/issues/8) | Establish version control | Part 2 (directory structure, traceability) |
| [#9](https://github.com/nbx0/post-bfxwkshp-schema/issues/9) | Configure computational environment | Part 3 (MIRA-NF setup) |
| [#10](https://github.com/nbx0/post-bfxwkshp-schema/issues/10) | Validate analysis pipeline | Parts 3–4 (assembly + QC validation) |

### [Phase 2: Operational Readiness](https://github.com/nbx0/post-bfxwkshp-schema/milestone/3)

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| [#11](https://github.com/nbx0/post-bfxwkshp-schema/issues/11) | Identify sequence data sources | Part 1 (SRA data acquisition) |
| [#12](https://github.com/nbx0/post-bfxwkshp-schema/issues/12) | Define acceptance/rejection criteria | Part 4 (QC pass/fail thresholds) |
| [#13](https://github.com/nbx0/post-bfxwkshp-schema/issues/13) | Establish target sample throughput and define reporting period | Parts 3–4 (batch processing) |
| [#14](https://github.com/nbx0/post-bfxwkshp-schema/issues/14) | Develop SOPs | Part 5 (HA extraction procedure) |
| [#15](https://github.com/nbx0/post-bfxwkshp-schema/issues/15) | Implement automated workflows | Part 6 (Nextstrain pipeline) |
| [#16](https://github.com/nbx0/post-bfxwkshp-schema/issues/16) | Develop submission SOPs | Part 7 (reporting deliverables) |
| [#17](https://github.com/nbx0/post-bfxwkshp-schema/issues/17) | Define report templates | Part 7 (Quarto report template) |
