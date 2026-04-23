---
layout: page
title: Common Problems in Influenza Bioinformatics
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/17b-common-problems/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Ben Rambo-Martin and Kristine Lacek</p>
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

  pdfjsLib.getDocument('{{ site.baseurl }}/assets/pdfs/Presentation10_QMS_CommonProblems.pdf').promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    document.getElementById('page-count').textContent = pdfDoc.numPages;
    renderPage(pageNum);
  });
</script>

[Download slides (PDF)]({{ site.baseurl }}/assets/pdfs/Presentation10_QMS_CommonProblems.pdf)

---

## Objectives

- Recognize common failure modes in influenza NGS analysis
- Interpret MIRA QC failures and apply appropriate remediation
- Understand the impact of DI particles and homopolymer-induced frameshifts

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
