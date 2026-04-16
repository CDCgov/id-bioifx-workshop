---
layout: page
title: Post Bioinformatics Workshop Expectations
sidebar: workshop_sidebar
topnav: topnav
permalink: /practical/end-to-end/
---

After the workshop, you are expected to apply the concepts and tools covered to your laboratory's real influenza sequencing data. This practical will walk you through repeating the entire workflow on a set of publicly available samples. You should complete the exercises in this practical using your institution's computational environment and resources. The goal is to gain confidence in executing the workflow end-to-end and to identify any gaps or challenges specific to your setup.

---

<span style="color: #0077B6;">**Post-workshop deliverables include completing the end-to-end workflow on your institution's influenza sequencing data and reporting the results back to CDC and APHL. We expect two reports during your country's upcoming influenza season, one mid-season and one post-season.**</span>

---

Each institution has a dedicated project tracker with milestones and issues that map directly to this practical. Find your institution's repository below:

| Institution | Repository |
|---|---|
| Instituto De Salud Pública De Chile (ISP) | [post-bfxwkshp-isp-chile](https://github.com/cdcent/post-bfxwkshp-isp-chile) |
| Laboratorio Nacional De Salud De Guatemala (LNS) | [post-bfxwkshp-lns-guatemala](https://github.com/cdcent/post-bfxwkshp-lns-guatemala) |
| Instituto de Diagnóstico y Referencia Epidemiológicos (InDRE) | [post-bfxwkshp-indre-mexico](https://github.com/cdcent/post-bfxwkshp-indre-mexico) |
| Ministerio De Salud Paraguay / Laboratorio Central De Salud Pública (LCSP) | [post-bfxwkshp-lcsp-paraguay](https://github.com/cdcent/post-bfxwkshp-lcsp-paraguay) |
| Instituto Nacional De Salud Peru (INS) | [post-bfxwkshp-ins-peru](https://github.com/cdcent/post-bfxwkshp-ins-peru) |
| Instituto Conmemorativo Gorgas de Estudios de la Salud (Gorgas) | [post-bfxwkshp-gorgas-panama](https://github.com/cdcent/post-bfxwkshp-gorgas-panama) |
| Secretaría Nacional de Ciencia y Tecnología (SENACYT) | [post-bfxwkshp-senacyt-panama](https://github.com/cdcent/post-bfxwkshp-senacyt-panama) |

---

## Step 1 — Download Test Data

Public sequencing data are available through NCBI's Sequence Read Archive (SRA). Your goal is to download paired-end FASTQ files for influenza samples under BioProject [**PRJNA1437047**](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1437047) that match the pattern `H1_*`.

**Suggested tools:** `sra-toolkit` (`prefetch`, `fasterq-dump`), Entrez Direct (`esearch`, `efetch`), [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA1437047&o=acc_s%3Aa)


## Step 2 — File Renaming and Directory Setup


Mira expects input files to follow a specific naming convention tied to a **samplesheet**. The SRA-downloaded files are named by run accession (e.g., `SRR12345678_1.fastq`), but Mira expects the more standard Illumina naming convention (`_R1`/`_R2`). You need to rename the files and prepare the directory structure Mira expects.

You also need to create the expected directory structure for Mira and the correctly formatted samplesheet.csv.

**Suggested tools:** bash loops (`while`, `for`), `mv`, I/O redirection (`>`, `>>`), `cut`


## Step 3 — Genome Assembly with Mira

{% include tip.html content="This section relates to <strong>Milestone 2: Setup &amp; Validation</strong> — <strong>Issue #9: Configure computational environment</strong> and <strong>Issue #10: Validate analysis pipeline</strong> in your institution's tracker repository." %}

[Mira-nf](https://github.com/CDCgov/MIRA-NF) is the CDC's influenza genome assembly and QC pipeline built on Nextflow. It can be run locally or on a cluster, and it uses containerized environments for reproducibility. For HPC environments, you may need to configure Nextflow profiles to specify resource requirements and execution parameters. CDC is here to help you configure it for your specific setup.



## Step 4 — Mira QC: Pass vs. Fail

{% include tip.html content="This section relates to <strong>Milestone 3: Operational Readiness</strong> — <strong>Issue #12: Define acceptance/rejection criteria</strong> and <strong>Milestone 1: Governance &amp; Operations</strong> — <strong>Issue #4: Implement continuous monitoring metrics</strong> in your institution's tracker repository." %}

Mira generates quality metrics for each assembled segment and determines whether the assembly passes or fails based on predefined thresholds. You need to review the QC summary output, understand the metrics reported and document them. You should be confident in explaining to your supervisors and colleagues why Mira's quality thresholds are set where they are, and how to interpret the results. You should also be able to identify any patterns in the QC failures that may indicate issues with specific segments or samples.

1. Locate and examine the QC summary output from Mira. What columns/metrics are reported? What does each metric tell you about assembly quality?

2. What thresholds does Mira use to define a "passing" assembly? Consider genome completeness, coverage depth, and ambiguous base counts. 

3. How many total reads did your negative control have and what percent of those reads matched influenza?

4. How many samples passed? How many failed? Are there any patterns in the failures (e.g., specific segments, low input material)?


## Step 5 — Extracting HA Sequences from Mira Output

{% include tip.html content="This section relates to <strong>Milestone 3: Operational Readiness</strong> — <strong>Issue #14: Develop SOPs</strong> in your institution's tracker repository." %}

The **HA (hemagglutinin)** segment is most commonly used for phylogenetic analysis. You need to extract the HA consensus sequences from samples that passed QC. HA is segment 4 for influenza A.

You should have a single FASTA file containing one HA consensus sequence per QC-passing sample.

**Suggested bash tools:** `grep`,`>>`

## Step 6 — Phylogenetic Analysis with Nextstrain

{% include tip.html content="This section relates to <strong>Milestone 2: Setup &amp; Validation</strong> — <strong>Issue #10: Validate analysis pipeline</strong> and <strong>Milestone 3: Operational Readiness</strong> — <strong>Issue #15: Implement automated workflows</strong> in your institution's tracker repository." %}

[Nextstrain](https://nextstrain.org/) provides tools for phylogenetic analysis and visualization of pathogen genomic data. The core command-line toolkit is [Augur](https://docs.nextstrain.org/projects/augur/), and interactive trees are viewed in [Auspice](https://auspice.us/).

**Suggested tools:** `augur` (align, tree, refine, ancestral, translate, export), `auspice`

1. Create a metadata TSV for your samples with strain names, collection dates, and geographic info.

2. Download a global reference dataset of H1 HA sequences from GISAID or GenBank to provide context for your samples.

3. Align your HA sequences against the reference using `augur align`.

4. Build a phylogenetic tree with `augur tree`, then refine it with temporal information using `augur refine --timetree`.

5. *(Optional)* Reconstruct ancestral sequences and translate mutations onto the tree with `augur ancestral` and `augur translate`.

6. Export the tree for visualization with `augur export` and view it in [Auspice](https://auspice.us/).

7. Explore the interactive tree. What relationships, clusters, or outliers do you see among your samples?


## Step 7 — Reporting with Quarto

{% include tip.html content="This section relates to <strong>Milestone 3: Operational Readiness</strong> — <strong>Issue #17: Define report templates</strong> in your institution's tracker repository." %}

1. Modify the provided Quarto report template to include your institution's name, logo, and any specific sections relevant to your reporting needs.

2. Populate the report with your analysis results, including a description of the samples analyzed and the phylogenetic tree visualizations.

## Milestone Reference Summary

The exercises in this practical map to the following milestones and issues in your institution's tracker repository (see the [Institution Tracker Repositories](#institution-tracker-repositories) table above):

### Milestone 1: Governance & Operations

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| #1 | Define turnaround time targets for analysis and reporting | Parts 3–7 (overall workflow timing) |
| #2 | Define sample prioritization criteria | Part 4 (QC pass/fail triage) |
| #3 | Define contingency plans for pipeline/infrastructure failure | Part 3 (pipeline execution) |
| #4 | Implement continuous monitoring metrics | Part 4 (QC metrics review) |
| #5 | Define metadata standards and change management for pipelines | Part 2 (file naming/metadata) |

### Milestone 2: Setup & Validation

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| #6 | Define computational infrastructure | Parts 1, 3 (tool setup) |
| #7 | Implement reproducible environments | Part 3 (Nextflow profiles, containers) |
| #8 | Establish version control | Part 2 (directory structure, traceability) |
| #9 | Configure computational environment | Part 3 (Mira setup) |
| #10 | Validate analysis pipeline | Parts 3–4 (assembly + QC validation) |

### Milestone 3: Operational Readiness

| Issue | Title | Practical Section |
|-------|-------|-------------------|
| #11 | Identify sequence data sources | Part 1 (SRA data acquisition) |
| #12 | Define acceptance/rejection criteria | Part 4 (QC pass/fail thresholds) |
| #13 | Establish target sample throughput and define reporting period | Parts 3–4 (batch processing) |
| #14 | Develop SOPs | Part 5 (HA extraction procedure) |
| #15 | Implement automated workflows | Part 6 (Nextstrain pipeline) |
| #16 | Develop submission SOPs | Part 7 (reporting deliverables) |
| #17 | Define report templates | Part 7 (Quarto report template) |
