---
layout: page
title: Phylogenetics
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/15-phylogenetics/
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

  pdfjsLib.getDocument('{{ site.baseurl }}/WIP/phylogenetics.pdf').promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    document.getElementById('page-count').textContent = pdfDoc.numPages;
    renderPage(pageNum);
  });
</script>

[Download slides (PDF)]({{ site.baseurl }}/WIP/phylogenetics.pdf)

## Content and practical materials available [here](https://github.com/nhassell/seasonal-flu-demo/tree/master)

Clone the practical materials with the following command:

```{bash}
git clone https://github.com/nhassell/seasonal-flu-demo.git
```
