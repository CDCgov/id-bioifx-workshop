---
layout: page
title: Search
permalink: /search/
sidebar: workshop_sidebar
topnav: topnav
search: exclude
---

# Site Search

<div class="search-container">
  <div class="search-input-wrap">
    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <input id="search-box" type="search" placeholder="Search lessons, practicals, extras…" aria-label="Search site content" autocomplete="off" />
    <button id="search-clear" type="button" aria-label="Clear search" style="display:none;">&times;</button>
    <kbd class="search-shortcut" title="Press / to focus search">/</kbd>
  </div>
  <p id="search-count" class="search-count" aria-live="polite" style="display:none;"></p>
  <p class="search-hint">Use <kbd>&uarr;</kbd><kbd>&darr;</kbd> to navigate, <kbd>Enter</kbd> to open, <kbd>Esc</kbd> to clear</p>
</div>

<div id="search-results" aria-live="polite"></div>

<style>
.search-container { max-width: 700px; }
.search-input-wrap {
  position: relative;
  display: flex;
  align-items: center;
}
.search-icon {
  position: absolute;
  left: 12px;
  color: #888;
  pointer-events: none;
}
#search-box {
  width: 100%;
  padding: .7rem .7rem .7rem 2.5rem;
  font-size: 1.05rem;
  border: 2px solid #d0d5dd;
  border-radius: 8px;
  outline: none;
  transition: border-color .2s, box-shadow .2s;
  background: #fff;
}
#search-box:focus {
  border-color: #3578e5;
  box-shadow: 0 0 0 3px rgba(53,120,229,.15);
}
#search-clear {
  position: absolute;
  right: 42px;
  background: none;
  border: none;
  font-size: 1.3rem;
  color: #888;
  cursor: pointer;
  padding: 0 6px;
  line-height: 1;
}
#search-clear:hover { color: #333; }
.search-shortcut {
  position: absolute;
  right: 12px;
  background: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 1px 7px;
  font-size: .75rem;
  color: #666;
  pointer-events: none;
}
.search-count {
  margin: .6rem 0 0;
  font-size: .85rem;
  color: #555;
}
.search-hint {
  margin: .3rem 0 0;
  font-size: .78rem;
  color: #999;
}
.search-hint kbd {
  background: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 3px;
  padding: 0 4px;
  font-size: .75rem;
}
.search-empty {
  color: #666;
  font-style: italic;
}
.search-results-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.search-result-item {
  padding: .65rem .75rem;
  border-bottom: 1px solid #eee;
  border-radius: 6px;
  transition: background .15s;
}
.search-result-item:hover,
.search-result-item.search-active {
  background: #f0f5ff;
}
.search-result-link {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  text-decoration: none;
  gap: .5rem;
}
.search-result-title {
  font-weight: 600;
  font-size: 1rem;
  color: #1a56db;
}
.search-result-link:hover .search-result-title {
  text-decoration: underline;
}
.search-result-section {
  font-size: .72rem;
  text-transform: uppercase;
  letter-spacing: .04em;
  color: #888;
  background: #f3f4f6;
  padding: 1px 8px;
  border-radius: 10px;
  white-space: nowrap;
}
.search-result-snippet {
  margin: .25rem 0 0;
  font-size: .85rem;
  color: #555;
  line-height: 1.45;
}
.search-result-snippet mark {
  background: #fef08a;
  padding: 0 2px;
  border-radius: 2px;
}
</style>

<script>
window.SEARCH_INDEX = [
  {%- assign pages = site.pages | where_exp:'p','p.title' -%}
  {%- for p in pages -%}
  {"title": {{ p.title | jsonify }}, "url": {{ p.url | relative_url | jsonify }}, "content": {{ p.content | strip_html | normalize_whitespace | jsonify }} }{%- unless forloop.last -%},{%- endunless -%}
  {%- endfor -%}
];
</script>
<script src="{{ '/assets/js/search.js' | relative_url }}?v={{ site.time | date: '%s' }}"></script>
