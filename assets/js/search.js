// filepath: /Users/nbx0/repos/id-bioifx-workshop/assets/js/search.js
// Client-side search; expects window.SEARCH_INDEX = [{title,url,content}]
(function(){
  var input = document.getElementById('search-box');
  var resultsEl = document.getElementById('search-results');
  var countEl = document.getElementById('search-count');
  var clearBtn = document.getElementById('search-clear');
  if(!input || !resultsEl) return;
  var pages = (window.SEARCH_INDEX || []).filter(function(p){ return p && p.title && p.url; });
  var debounceTimer = null;
  var activeIdx = -1;

  function tokenize(str){
    return (str||'').toLowerCase().replace(/[^a-z0-9\s]/g,' ').split(/\s+/).filter(Boolean);
  }

  function escapeRegExp(s){
    return s.replace(/[-/\\^$*+?.()|[\]{}]/g,'\\$&');
  }

  function score(qTokens, page){
    var titleLower = page.title.toLowerCase();
    var contentLower = page.content.toLowerCase();
    var s = 0;
    for(var i=0; i<qTokens.length; i++){
      var t = qTokens[i];
      var escaped = escapeRegExp(t);
      // Substring matches anywhere
      var subRe = new RegExp(escaped,'g');
      var tm = titleLower.match(subRe);
      var cm = contentLower.match(subRe);
      if(!tm && !cm) return 0; // all tokens must appear somewhere
      // Word-boundary matches get bonus
      var boundRe = new RegExp('(^|\\b)'+escaped,'g');
      var tmBound = titleLower.match(boundRe);
      var cmBound = contentLower.match(boundRe);
      // Title substring: 5pts, title word-boundary: +5 bonus, content substring: 1pt, content word-boundary: +1 bonus
      if(tm) s += tm.length * 5;
      if(tmBound) s += tmBound.length * 5;
      if(cm) s += cm.length;
      if(cmBound) s += cmBound.length;
    }
    return s;
  }

  function escapeHtml(s){
    return s.replace(/[&<>"']/g, function(c){
      return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'})[c];
    });
  }

  function highlight(snippet, tokens){
    var safe = escapeHtml(snippet);
    for(var i=0; i<tokens.length; i++){
      var re = new RegExp('('+escapeRegExp(tokens[i])+')','ig');
      safe = safe.replace(re,'<mark>$1</mark>');
    }
    return safe;
  }

  function makeSnippet(content, tokens){
    var lower = content.toLowerCase();
    var idx = Infinity;
    for(var i=0; i<tokens.length; i++){
      var pos = lower.indexOf(tokens[i]);
      if(pos!==-1 && pos<idx) idx=pos;
    }
    if(!isFinite(idx)) idx = 0;
    var start = Math.max(0, idx - 60);
    var slice = content.slice(start, start+220);
    return (start>0?'… ':'') + slice + (content.length > start+220 ? ' …' : '');
  }

  function sectionFromUrl(url){
    var m = url.match(/\/(lessons|practical|extras|presentations|workshops|WIP)\//);
    if(m) return m[1].charAt(0).toUpperCase() + m[1].slice(1);
    return 'Page';
  }

  function render(list, tokens, query){
    if(countEl){
      countEl.textContent = list.length ? list.length + ' result' + (list.length===1?'':'s') : '';
      countEl.style.display = list.length ? '' : 'none';
    }
    if(!list.length){
      resultsEl.innerHTML = '<p class="search-empty">No results for "<strong>'+escapeHtml(query)+'</strong>". Try different keywords.</p>';
      return;
    }
    var html = '<ul class="search-results-list" role="listbox">';
    for(var i=0; i<list.length; i++){
      var r = list[i];
      var section = sectionFromUrl(r.url);
      html += '<li class="search-result-item" role="option" id="sr-'+i+'">'
        + '<a href="'+r.url+'" class="search-result-link">'
        + '<span class="search-result-title">'+highlight(r.title, tokens)+'</span>'
        + '<span class="search-result-section">'+escapeHtml(section)+'</span>'
        + '</a>'
        + '<p class="search-result-snippet">'+highlight(r.snippet, tokens)+'</p>'
        + '</li>';
    }
    html += '</ul>';
    resultsEl.innerHTML = html;
    activeIdx = -1;
  }

  function doSearch(){
    var q = input.value.trim();
    // Update URL without reloading
    if(history.replaceState){
      var url = window.location.pathname + (q ? '?q='+encodeURIComponent(q) : '');
      history.replaceState(null, '', url);
    }
    if(q.length<2){
      resultsEl.innerHTML='';
      if(countEl){ countEl.textContent=''; countEl.style.display='none'; }
      toggleClear();
      return;
    }
    var tokens = tokenize(q);
    var out = [];
    for(var i=0; i<pages.length; i++){
      var p = pages[i];
      var s = score(tokens, p);
      if(s>0){
        out.push({
          title: p.title,
          url: p.url,
          snippet: makeSnippet(p.content, tokens),
          s: s
        });
      }
    }
    out.sort(function(a,b){ return b.s - a.s; });
    out = out.slice(0, 50);
    render(out, tokens, q);
    toggleClear();
  }

  function toggleClear(){
    if(clearBtn){
      clearBtn.style.display = input.value.length > 0 ? '' : 'none';
    }
  }

  // Debounced input
  input.addEventListener('input', function(){
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(doSearch, 200);
    toggleClear();
  });

  // Keyboard navigation
  input.addEventListener('keydown', function(e){
    var items = resultsEl.querySelectorAll('.search-result-item');
    if(!items.length) return;
    if(e.key==='ArrowDown'){
      e.preventDefault();
      activeIdx = Math.min(activeIdx+1, items.length-1);
      updateActive(items);
    } else if(e.key==='ArrowUp'){
      e.preventDefault();
      activeIdx = Math.max(activeIdx-1, -1);
      updateActive(items);
    } else if(e.key==='Enter' && activeIdx>=0){
      e.preventDefault();
      var link = items[activeIdx].querySelector('a');
      if(link) window.location.href = link.href;
    } else if(e.key==='Escape'){
      input.value = '';
      resultsEl.innerHTML = '';
      if(countEl){ countEl.textContent=''; countEl.style.display='none'; }
      toggleClear();
      if(history.replaceState) history.replaceState(null,'', window.location.pathname);
    }
  });

  function updateActive(items){
    for(var i=0; i<items.length; i++){
      items[i].classList.toggle('search-active', i===activeIdx);
    }
    if(activeIdx>=0 && items[activeIdx]){
      items[activeIdx].scrollIntoView({block:'nearest'});
    }
  }

  // Clear button
  if(clearBtn){
    clearBtn.addEventListener('click', function(){
      input.value = '';
      resultsEl.innerHTML = '';
      if(countEl){ countEl.textContent=''; countEl.style.display='none'; }
      toggleClear();
      input.focus();
      if(history.replaceState) history.replaceState(null,'', window.location.pathname);
    });
  }

  // Load query from URL on page load
  var params = new URLSearchParams(window.location.search);
  var initQ = params.get('q');
  if(initQ){
    input.value = initQ;
    doSearch();
  }
  toggleClear();

  // Global keyboard shortcut: "/" to focus search
  document.addEventListener('keydown', function(e){
    if(e.key==='/' && document.activeElement !== input && !e.ctrlKey && !e.metaKey && !e.altKey){
      var tag = (document.activeElement||{}).tagName;
      if(tag==='INPUT'||tag==='TEXTAREA'||tag==='SELECT') return;
      e.preventDefault();
      input.focus();
      input.select();
    }
  });
})();