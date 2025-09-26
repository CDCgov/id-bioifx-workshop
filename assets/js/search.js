// filepath: /Users/nbx0/repos/id-bioifx-workshop/assets/js/search.js
// Client-side search; expects window.SEARCH_INDEX = [{title,url,content}]
(function(){
  const input = document.getElementById('search-box');
  const resultsEl = document.getElementById('search-results');
  if(!input || !resultsEl) return;
  const pages = (window.SEARCH_INDEX || []).filter(p=>p && p.title && p.url);

  function tokenize(str){
    return (str||'').toLowerCase().replace(/[^a-z0-9\s]/g,' ').split(/\s+/).filter(Boolean);
  }
  function score(qTokens, page){
    const text = (page.title+' '+page.content).toLowerCase();
    let s=0; qTokens.forEach(t=>{ const re=new RegExp('(^|\\b)'+t,'g'); const m=text.match(re); if(m) s+=m.length; });
    return s;
  }
  function escapeHtml(s){
    return s.replace(/[&<>"']/g, function(c){ return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[c]); });
  }
  function highlight(snippet, tokens){
    let safe = escapeHtml(snippet);
    tokens.forEach(t=>{
      const re = new RegExp('('+t.replace(/[-/\\^$*+?.()|[\]{}]/g,'\\$&')+')','ig');
      safe = safe.replace(re,'<mark>$1</mark>');
    });
    return safe;
  }
  function makeSnippet(content, tokens){
    const lower = content.toLowerCase();
    let idx = Infinity;
    tokens.forEach(t=>{
      const i = lower.indexOf(t);
      if(i!==-1 && i<idx) idx=i;
    });
    if(!isFinite(idx)) idx = 0;
    const start = Math.max(0, idx - 40);
    const slice = content.slice(start, start+180);
    return (start>0?'…':'') + slice + (content.length > start+180 ? '…' : '');
  }
  function render(list, tokens){
    if(!list.length){ resultsEl.innerHTML='<p>No matches.</p>'; return; }
    resultsEl.innerHTML='<ul>'+list.map(r=>`<li><a href="${r.url}">${escapeHtml(r.title)}</a><br><small>${highlight(r.snippet, tokens)}</small></li>`).join('')+'</ul>';
  }
  input.addEventListener('input', function(){
    const q=this.value.trim();
    if(q.length<2){ resultsEl.innerHTML=''; return; }
    const tokens=tokenize(q);
    const out=pages.map(p=>({
        title:p.title,
        url:p.url,
        snippet: makeSnippet(p.content, tokens),
        s: score(tokens,p)
      }))
      .filter(o=>o.s>0)
      .sort((a,b)=>b.s-a.s)
      .slice(0,40);
    render(out, tokens);
  });
})();