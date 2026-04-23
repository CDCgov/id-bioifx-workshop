---
layout: page
title: Training Overview - Influenza Vaccine Composition
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/02-overview-vcm/
---
<p style="color: #015CAE; font-size: 19px;">Content developed by Ben Rambo-Martin</p>
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

  pdfjsLib.getDocument('{{ site.baseurl }}/assets/pdfs/Presentation1_TrainingOverviewVCM.pdf?v=2').promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    document.getElementById('page-count').textContent = pdfDoc.numPages;
    renderPage(pageNum);
  });
</script>

[Download slides (PDF)]({{ site.baseurl }}/assets/pdfs/Presentation1_TrainingOverviewVCM.pdf?v=2)
