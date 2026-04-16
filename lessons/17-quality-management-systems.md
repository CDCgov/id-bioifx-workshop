---
layout: page
title: Quality Management Systems for Bioinformatics and Troubleshooting
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/17-quality-management-systems/
---

## Slides

<div id="pdf-viewer" style="text-align: center;">
  <canvas id="pdf-canvas" style="border: 1px solid #ccc; max-width: 100%;"></canvas>
  <div id="pdf-controls" style="margin-top: 10px;">
    <button id="prev-page" onclick="onPrevPage()" style="padding: 6px 16px; font-size: 16px; cursor: pointer;">&larr; Prev</button>
    <span style="margin: 0 12px; font-size: 16px;">Page <span id="page-num"></span> / <span id="page-count"></span></span>
    <button id="next-page" onclick="onNextPage()" style="padding: 6px 16px; font-size: 16px; cursor: pointer;">Next &rarr;</button>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<script>
  var pdfjsLib = window['pdfjs-dist/build/pdf'];
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

  var pdfDoc = null,
      pageNum = 1,
      pageRendering = false,
      pageNumPending = null,
      scale = 2,
      canvas = document.getElementById('pdf-canvas'),
      ctx = canvas.getContext('2d');

  function renderPage(num) {
    pageRendering = true;
    pdfDoc.getPage(num).then(function(page) {
      var viewport = page.getViewport({ scale: scale });
      canvas.height = viewport.height;
      canvas.width = viewport.width;
      var renderContext = { canvasContext: ctx, viewport: viewport };
      var renderTask = page.render(renderContext);
      renderTask.promise.then(function() {
        pageRendering = false;
        if (pageNumPending !== null) {
          renderPage(pageNumPending);
          pageNumPending = null;
        }
      });
    });
    document.getElementById('page-num').textContent = num;
  }

  function queueRenderPage(num) {
    if (pageRendering) {
      pageNumPending = num;
    } else {
      renderPage(num);
    }
  }

  function onPrevPage() {
    if (pageNum <= 1) return;
    pageNum--;
    queueRenderPage(pageNum);
  }

  function onNextPage() {
    if (pageNum >= pdfDoc.numPages) return;
    pageNum++;
    queueRenderPage(pageNum);
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') onPrevPage();
    if (e.key === 'ArrowRight') onNextPage();
  });

  pdfjsLib.getDocument('{{ site.baseurl }}/assets/pdfs/Presentation10_QMS_BestPractices_Troubleshooting_v2.pdf').promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    document.getElementById('page-count').textContent = pdfDoc.numPages;
    renderPage(pageNum);
  });
</script>

[Download slides (PDF)]({{ site.baseurl }}/assets/pdfs/Presentation10_QMS_BestPractices_Troubleshooting_v2.pdf)

---

## Objectives

- Describe quality management system (QMS) components
  - Reproducibility
  - Version control
  - Documentation
- Apply QMS principles to NGS workflows
  - Pre-analytical
  - Analytical
- Common troubleshooting

---

## Reproducibility

- **Same input + same methods = same results**
  - Core principle of computational (all) science
- Record software versions
  - Aligners, samtools, variant callers, workflow managers
- Track changes with version control
  - Git for scripts and pipeline development
- Document parameters and references
  - Primer schemes
  - Quality thresholds
- Identify test data to run through new versions and pipelines
- Use workflow managers
  - Snakemake, Nextflow for structured, repeatable runs
- Leverage containers
  - Docker or Singularity ensure consistent environments

---

## Documentation

- Explains how tools and pipelines work
  - Inputs, outputs, parameters, and assumptions
- Enables reproducibility
  - Others (and future you) can rerun the same analysis
- Reduces errors and misuse
  - Clear defaults and examples prevent incorrect runs
- Essential for collaboration
  - Shared understanding across labs, teams, and institutions

### Best Practices in Writing Documentation

- **README.md files** — Overview, requirements, and basic usage
- **Usage examples & command snippets** — Copy-pasteable starting points
- **Parameter descriptions** — What flags do, expected values, and defaults
- **Workflow diagrams** — Visualize steps, inputs, and outputs
- **Document data formats** — FASTQ, FASTA, BAM, reference versions
- **Record software versions** — Tools, containers, workflow managers
- **Include example datasets** — Small test cases to validate setup

### Best Practices in Using Documentation

- Start with the README
  - Understand the purpose, inputs, outputs, and limitations
- Check versions and dates
  - Ensure the documentation matches the tool or pipeline version you're using
- Follow the example first
  - Run the provided test or example before real data
- Read parameter descriptions carefully
  - Defaults may not match your experiment
- Verify input formats
  - FASTQ, FASTA, BAM, sample sheets, reference builds
- Look for expected outputs
  - Confirm files and directories match the documented results

---

## Git

Git is a **version control system** that tracks changes to files over time.

- Designed for collaboration
  - Multiple people can work on the same codebase
  - Think of it like a shared document (Microsoft Office, Google Docs)
- Keeps a history of your work
  - See what changed, when, why, and by whom
- Common in bioinformatics
  - Pipelines, scripts, documentation, and workflows
- GitLab and GitHub are the most used platforms

### Core Git Concepts

| Concept | Description |
|---------|-------------|
| **Repository (repo)** | A project tracked by Git |
| **Commit** | A saved snapshot of changes with a message |
| **Branch** | A parallel version of the code for development or testing |
| **Remote repository** | Shared copy on platforms like GitHub or GitLab |

### Common Git Commands

**Create or get a repository:**

- `git init` — start a repo
- `git clone <repo>` — copy an existing repo

**Track and save changes:**

- `git status` — see changes
- `git add <file>` — stage changes
- `git commit -m "message"` — save snapshot

**Sync with others:**

- `git pull` — get updates
- `git push` — share your changes

---

## Common Problems in Influenza Bioinformatics

### Failed MIRA QC: Low-Coverage / Incomplete Segment Coverage

- Not enough reads in your library — go back to the lab
  - Ct <= 28?
  - Gel image resolves segment bands cleanly?
  - Proper sample number on your flow cell?
- MIRA <= v2.0.0?
  - Reads are being subsampled

### Failed MIRA QC: Minor Variant Count > 10

- In standard *clinical* samples, we have never observed >6 minor alleles (>=5% frequency) with the majority having 1-3, per segment
- Cell cultures regularly have high genetic variability which can result in high counts
- Could be a co-infection (e.g., both H1N1 and H3N2 infection at the same time)
- **Most likely contamination!**

### Failed MIRA QC: Premature Stop-Codon

- ONT homopolymer issue may require manual correction
- DI particle induced alignment

### DI Particles

Defective interfering (DI) particles can interfere with NGS analysis:

- Common in polymerase segments
- Coverage shape can spike at the ends or show "bat ears" pattern
- Can create erroneous indel mutations at coverage dropoff points

### Frameshifts

- Prevalent in homopolymer regions of Oxford Nanopore Sequencing
- DAIS-Ribosome is frameshift-tolerant
  - Shows as (~) mutation
- Convert back to nucleotide space and add or remove a base to fix

---

## MIRA Demands High Quality Results

- Together we can stop the "Garbage In" side of the data analysis mantra: **"Garbage In, Garbage Out"**
- Built-in thresholds are for standardizing QC
- Amended consensus gives us extra information from a single sequence
  - A mixed site may be under active or balancing selection in the host
- Consider each sample as a whole: if HA and NA pass but all other segments fail, consider why
- High priority samples can be useful even when QC thresholds are not met
