// Accordion sidebar: only one sibling branch open per level (after theme toggles expander).
(function () {
  var jtd = window.jtd;
  if (!jtd || typeof jtd.addEvent !== 'function') return;

  function bindAccordionClicks() {
    jtd.addEvent(document, 'click', function (e) {
      var target = e.target;
      while (target && !(target.classList && target.classList.contains('nav-list-expander'))) {
        target = target.parentNode;
      }
      if (!target) return;

      var item = target.parentNode;
      if (!item || !item.classList.contains('nav-list-item')) return;

      window.setTimeout(function () {
        if (!item.classList.contains('active')) return;

        var parentList = item.parentElement;
        if (!parentList || !parentList.classList.contains('nav-list')) return;

        var siblings = parentList.children;
        for (var i = 0; i < siblings.length; i++) {
          var sib = siblings[i];
          if (sib === item || !sib.classList || !sib.classList.contains('nav-list-item')) continue;
          sib.classList.remove('active');
          var ex = sib.querySelector(':scope > .nav-list-expander');
          if (ex) {
            ex.setAttribute('aria-expanded', 'false');
          }
        }
      }, 0);
    });
  }

  if (typeof jtd.onReady === 'function') {
    jtd.onReady(bindAccordionClicks);
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', bindAccordionClicks);
    } else {
      bindAccordionClicks();
    }
  }
})();

(function () {
  var STORAGE_KEY = 'notes-site-theme';

  function syncThemeButtons() {
    var t = document.documentElement.getAttribute('data-site-theme') || 'light';
    document.querySelectorAll('.site-theme-switch__btn').forEach(function (btn) {
      var v = btn.getAttribute('data-site-theme-value');
      btn.setAttribute('aria-pressed', v === t ? 'true' : 'false');
    });
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.site-theme-switch__btn');
    if (!btn) return;
    var v = btn.getAttribute('data-site-theme-value');
    if (v !== 'dark' && v !== 'light') return;
    document.documentElement.setAttribute('data-site-theme', v);
    try {
      localStorage.setItem(STORAGE_KEY, v);
    } catch (err) {}
    syncThemeButtons();
  });

  function onReady(fn) {
    if (typeof window.jtd !== 'undefined' && typeof window.jtd.onReady === 'function') {
      window.jtd.onReady(fn);
    } else if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  onReady(syncThemeButtons);
})();
