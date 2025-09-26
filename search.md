---
layout: page
title: Search
permalink: /search/
nav_order: 98
---

# Site Search

Type to filter pages. JavaScript performs an in-browser search index (no external service).

<input id="search-box" type="text" placeholder="Search terms..." style="width:100%;padding:.6rem;border:1px solid var(--c-border);border-radius:6px;" aria-label="Search site content" />

<div id="search-results" aria-live="polite" style="margin-top:1.5rem;"></div>

<script>
window.SEARCH_INDEX = [
  {%- assign pages = site.pages | where_exp:'p','p.title' -%}
  {%- for p in pages -%}
  {"title": {{ p.title | jsonify }}, "url": {{ p.url | relative_url | jsonify }}, "content": {{ p.content | strip_html | normalize_whitespace | jsonify }} }{%- unless forloop.last -%},{%- endunless -%}
  {%- endfor -%}
];
</script>
<script src="{{ '/assets/js/search.js' | relative_url }}"></script>
