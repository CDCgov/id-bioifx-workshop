---
layout: page
title: Search
permalink: /search/
sidebar: workshop_sidebar
topnav: topnav
search: exclude
toc: false
---

<link href="{{ '/pagefind/pagefind-ui.css' | relative_url }}" rel="stylesheet">

<p>Search across all lessons, practicals, presentations, and embedded PDF/PPTX content.</p>

<div id="search"></div>

<script src="{{ '/pagefind/pagefind-ui.js' | relative_url }}"></script>
<script>
  window.addEventListener('DOMContentLoaded', function () {
    var pf = new PagefindUI({
      element: "#search",
      showSubResults: true,
      showImages: false,
      processResult: function (result) {
        if (result.meta && result.meta.url) {
          result.url = result.meta.url;
        }
        return result;
      }
    });
    var params = new URLSearchParams(window.location.search);
    var q = params.get('q');
    if (q) {
      pf.triggerSearch(q);
    }
  });
</script>
