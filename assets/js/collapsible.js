(function() {
  document.addEventListener('DOMContentLoaded', () => {
    // Existing placeholder for legacy .collapsible
    document.querySelectorAll('details.collapsible').forEach(d => {
      d.addEventListener('toggle', () => {
        // Placeholder for analytics or future animation hooks.
      });
    });

    // Enhance markdown-preserving collapsibles with a close button
    function enhanceCollapsibleMd() {
      document.querySelectorAll('details.collapsible-md').forEach(d => {
        if (!d.querySelector('button.collapse-close')) {
          const inner = d.querySelector('.collapsible-inner') || d;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'collapse-close';
          btn.setAttribute('aria-label', 'Collapse section');
          btn.textContent = 'Collapse';
          btn.addEventListener('click', () => {
            d.open = false;
            const summary = d.querySelector('summary');
            if (summary) summary.focus();
          });
          inner.appendChild(btn);
        }
      });
    }

    enhanceCollapsibleMd();
  });
})();