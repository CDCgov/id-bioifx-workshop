(function() {
  function addCopyButtons() {
    document.querySelectorAll('pre > code').forEach(codeEl => {
      const pre = codeEl.parentElement;
      if (pre.classList.contains('no-copy')) return;
      if (pre.querySelector('.copy-btn')) return;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(codeEl.textContent);
          const original = btn.textContent;
            btn.textContent = 'Copied';
            btn.disabled = true;
            setTimeout(() => { btn.textContent = original; btn.disabled = false; }, 1600);
        } catch (e) {
          btn.textContent = 'Error';
        }
      });
      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }
  document.addEventListener('DOMContentLoaded', addCopyButtons);
})();