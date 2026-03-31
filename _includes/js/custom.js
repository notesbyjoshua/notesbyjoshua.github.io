// Accordion sidebar: opening a section closes its siblings at the same depth.
// Runs after Just the Docs' expander toggle (same click, deferred with setTimeout(0)).
jtd.onReady(function () {
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
});
