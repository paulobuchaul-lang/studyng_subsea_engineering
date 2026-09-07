/* =========================================================================
   Plataforma Subsea Rafaela — app.js (Sprint 2 — design system e protótipo)
   -------------------------------------------------------------------------
   Camadas de profundidade, popover de termos, quiz, progresso (localStorage),
   ícones SVG inline, tema claro/escuro, navegação ativa, abas do painel PM,
   medidor de profundidade e "Continuar" na Home.
   Sem XP nem gamificação completa — isso é Sprint 8. window.SUBSEA_GLOSSARIO
   e window.SUBSEA_ICONS já foram injetados antes deste arquivo carregar.
   ========================================================================= */

(function () {
  "use strict";

  var LAYER_PREF_KEY = "subsea_layer_pref";
  var PROGRESS_KEY = "subsea_progress";
  var THEME_KEY = "subsea_theme";
  var LAST_CHAPTER_KEY = "subsea_last_chapter";

  function safeGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function safeSet(key, value) {
    try { window.localStorage.setItem(key, value); } catch (e) { /* ok */ }
  }

  function getProgressList() {
    var raw = safeGet(PROGRESS_KEY);
    if (!raw) return [];
    try {
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) { return []; }
  }

  function addToProgress(chapterId) {
    var list = getProgressList();
    if (list.indexOf(chapterId) === -1) {
      list.push(chapterId);
      safeSet(PROGRESS_KEY, JSON.stringify(list));
    }
  }

  /* =========================================================================
     0. ICONES
     ========================================================================= */
  function populateIcons() {
    if (!window.SUBSEA_ICON) return;
    var nodes = Array.prototype.slice.call(document.querySelectorAll("[data-icon]"));
    nodes.forEach(function (el) {
      var name = el.getAttribute("data-icon");
      var svg = window.SUBSEA_ICON(name);
      if (svg) el.innerHTML = svg;
    });
  }

  /* =========================================================================
     1. TEMA CLARO/ESCURO
     ========================================================================= */
  function initTheme() {
    var saved = safeGet(THEME_KEY);
    if (saved === "light" || saved === "dark") {
      document.documentElement.setAttribute("data-theme", saved);
    }
    var buttons = [document.getElementById("themeToggle"), document.getElementById("themeToggleMobile")]
      .filter(Boolean);
    if (buttons.length === 0) return;

    function toggle() {
      var current = document.documentElement.getAttribute("data-theme");
      var isDark = current === "dark" || (!current && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = isDark ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      safeSet(THEME_KEY, next);
    }

    buttons.forEach(function (btn) { btn.addEventListener("click", toggle); });
  }

  /* =========================================================================
     2. NAVEGACAO ATIVA (sidebar + tab bar)
     ========================================================================= */
  function initActiveNav() {
    var here = location.pathname.replace(/\/+$/, "").split("/").pop() || "index.html";
    var links = Array.prototype.slice.call(
      document.querySelectorAll(".sidebar-nav a, .tabbar-mobile a, .sidebar-chapters a")
    );
    links.forEach(function (a) {
      var target = a.getAttribute("href").split("/").pop();
      if (target === here) a.classList.add("active");
    });
  }

  /* =========================================================================
     3. CONTROLE DE CAMADAS DE PROFUNDIDADE
     ========================================================================= */
  function initLayerControl() {
    var control = document.querySelector(".layer-control");
    if (!control) return;

    var buttons = Array.prototype.slice.call(control.querySelectorAll(".layer-btn"));
    var sections = Array.prototype.slice.call(document.querySelectorAll(".chapter-section"));
    if (buttons.length === 0) return;

    function applyLayer(layer) {
      sections.forEach(function (section) {
        var raw = section.getAttribute("data-layer");
        if (!raw || layer === "all") {
          section.hidden = false;
          return;
        }
        var values = raw.split(/\s+/);
        section.hidden = values.indexOf(layer) === -1;
      });
      buttons.forEach(function (btn) {
        btn.classList.toggle("active", btn.getAttribute("data-layer-btn") === layer);
      });
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var layer = btn.getAttribute("data-layer-btn");
        applyLayer(layer);
        safeSet(LAYER_PREF_KEY, layer);
      });
    });

    var saved = safeGet(LAYER_PREF_KEY);
    var validValues = buttons.map(function (btn) { return btn.getAttribute("data-layer-btn"); });
    applyLayer(saved && validValues.indexOf(saved) !== -1 ? saved : "all");
  }

  /* =========================================================================
     4. TERMOS DO GLOSSARIO (POPOVER)
     ========================================================================= */
  function findGlossaryEntry(term) {
    var list = window.SUBSEA_GLOSSARIO;
    if (!Array.isArray(list) || !term) return null;
    var needle = term.trim().toLowerCase();
    for (var i = 0; i < list.length; i++) {
      var entry = list[i];
      if (entry && typeof entry.term === "string" && entry.term.trim().toLowerCase() === needle) {
        return entry;
      }
    }
    return null;
  }

  function buildPopover() {
    var existing = document.getElementById("term-popover");
    if (existing) return existing;
    var popover = document.createElement("div");
    popover.id = "term-popover";
    popover.className = "term-popover";
    popover.hidden = true;
    popover.innerHTML =
      '<h4 class="term-title"></h4>' +
      '<p class="term-full"></p>' +
      '<p class="term-def"></p>' +
      '<p class="term-why"></p>' +
      '<div class="pop-actions"><a class="term-more" href="#">Ver no glossário</a>' +
      '<button type="button" class="term-close">Fechar</button></div>';
    document.body.appendChild(popover);
    return popover;
  }

  function initGlossaryPopover() {
    var terms = Array.prototype.slice.call(document.querySelectorAll(".term"));
    if (terms.length === 0) return;

    var popover = buildPopover();
    var titleEl = popover.querySelector(".term-title");
    var fullEl = popover.querySelector(".term-full");
    var defEl = popover.querySelector(".term-def");
    var whyEl = popover.querySelector(".term-why");
    var moreEl = popover.querySelector(".term-more");
    var closeEl = popover.querySelector(".term-close");

    function hidePopover() { popover.hidden = true; }

    var isMobileSheet = window.matchMedia && window.matchMedia("(max-width: 480px)").matches;

    function positionNear(target) {
      if (isMobileSheet) return; /* CSS fixa como bottom sheet */
      var rect = target.getBoundingClientRect();
      var margin = 8;
      popover.style.visibility = "hidden";
      popover.hidden = false;
      var popRect = popover.getBoundingClientRect();
      var popWidth = popRect.width || 300;
      var popHeight = popRect.height || 160;
      var top = rect.bottom + margin;
      if (top + popHeight > window.innerHeight) {
        top = rect.top - popHeight - margin;
        if (top < margin) top = margin;
      }
      var left = rect.left;
      if (left + popWidth > window.innerWidth - margin) left = window.innerWidth - popWidth - margin;
      if (left < margin) left = margin;
      popover.style.top = top + "px";
      popover.style.left = left + "px";
      popover.style.visibility = "";
    }

    function showFor(target) {
      var term = target.getAttribute("data-term") || target.textContent;
      var entry = findGlossaryEntry(term);
      if (!entry) return;

      titleEl.textContent = entry.term || "";
      fullEl.textContent = entry.full || "";
      fullEl.hidden = !entry.full;
      defEl.textContent = entry.definition || "";
      whyEl.textContent = entry.why ? "Por que importa: " + entry.why : "";
      whyEl.hidden = !entry.why;
      moreEl.setAttribute("href", "glossario.html#" + (entry.id || ""));

      popover.hidden = false;
      positionNear(target);
    }

    terms.forEach(function (term) {
      term.addEventListener("click", function (event) {
        event.stopPropagation();
        showFor(term);
      });
      term.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          showFor(term);
        }
      });
      if (!isMobileSheet && window.matchMedia && window.matchMedia("(hover: hover)").matches) {
        term.addEventListener("mouseenter", function () { showFor(term); });
      }
    });

    closeEl.addEventListener("click", function (event) {
      event.stopPropagation();
      hidePopover();
    });
    popover.addEventListener("click", function (event) { event.stopPropagation(); });
    document.addEventListener("click", function (event) {
      if (!popover.hidden && !popover.contains(event.target)) hidePopover();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") hidePopover();
    });
  }

  /* =========================================================================
     5. PAINEL PM EM ABAS
     ========================================================================= */
  function initPmTabs() {
    var tabs = Array.prototype.slice.call(document.querySelectorAll(".pm-tab"));
    if (tabs.length === 0) return;
    var boxes = Array.prototype.slice.call(document.querySelectorAll(".pm-box"));

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var key = tab.getAttribute("data-pm-tab");
        tabs.forEach(function (t) { t.classList.toggle("active", t === tab); });
        boxes.forEach(function (box) {
          box.hidden = box.getAttribute("data-pm-box") !== key;
        });
      });
    });
  }

  /* =========================================================================
     6. QUIZ
     ========================================================================= */
  function initQuiz() {
    var questions = Array.prototype.slice.call(document.querySelectorAll(".quiz-question"));
    questions.forEach(function (question) {
      var correctAnswer = question.getAttribute("data-answer");
      var feedbackText = question.getAttribute("data-feedback") || "";
      var feedbackEl = question.querySelector(".quiz-feedback");
      var options = Array.prototype.slice.call(question.querySelectorAll(".quiz-option"));

      options.forEach(function (option) {
        option.addEventListener("click", function () {
          var choice = option.getAttribute("data-choice");
          if (!feedbackEl) return;
          if (choice === correctAnswer) {
            option.classList.remove("incorrect");
            option.classList.add("correct");
            feedbackEl.textContent = "Certo! " + feedbackText;
            feedbackEl.hidden = false;
            options.forEach(function (opt) { opt.disabled = true; });
          } else {
            option.classList.remove("correct");
            option.classList.add("incorrect");
            feedbackEl.textContent = "Não é essa — tente outra opção.";
            feedbackEl.hidden = false;
          }
        });
      });
    });
  }

  /* =========================================================================
     7. PROGRESSO
     ========================================================================= */
  function setDoneState(button) {
    var icon = button.querySelector(".icon");
    button.textContent = "";
    if (icon) {
      var span = document.createElement("span");
      span.className = "icon";
      span.setAttribute("data-icon", "concluido");
      button.appendChild(span);
      if (window.SUBSEA_ICON) span.innerHTML = window.SUBSEA_ICON("concluido");
    }
    button.appendChild(document.createTextNode("Estudado"));
    button.classList.add("done");
  }

  function initMarkDone() {
    var button = document.querySelector(".mark-done");
    if (!button) return;
    var chapterId = button.getAttribute("data-chapter") || document.body.getAttribute("data-chapter-id");

    if (chapterId) safeSet(LAST_CHAPTER_KEY, chapterId);

    if (chapterId && getProgressList().indexOf(chapterId) !== -1) {
      setDoneState(button);
    }
    button.addEventListener("click", function () {
      if (!chapterId) return;
      addToProgress(chapterId);
      setDoneState(button);
    });
  }

  function initChapterCards() {
    var cards = Array.prototype.slice.call(document.querySelectorAll(".chapter-card, .sidebar-chapters a, .trail-point"));
    if (cards.length === 0) return;
    var progress = getProgressList();
    cards.forEach(function (card) {
      var chapterId = card.getAttribute("data-chapter-link");
      if (chapterId && progress.indexOf(chapterId) !== -1) card.classList.add("done");
    });
  }

  /* =========================================================================
     8. MEDIDOR DE PROFUNDIDADE (visual — logica de fases real e Sprint 8)
     ========================================================================= */
  function computeDepthZone(doneCount, total) {
    if (!total) return 0;
    var ratio = doneCount / total;
    return Math.min(6, Math.max(1, Math.ceil(ratio * 6) || (doneCount > 0 ? 1 : 0)));
  }

  function renderDepthMeter(track, label, doneCount, total) {
    if (!track) return;
    var zone = computeDepthZone(doneCount, total);
    var zones = Array.prototype.slice.call(track.querySelectorAll(".depth-meter-zone"));
    zones.forEach(function (el, idx) {
      el.classList.toggle("filled", idx < zone);
      el.classList.toggle("unfilled", idx >= zone);
    });
    if (label) {
      var restante = total - doneCount;
      label.textContent = doneCount === 0
        ? "Comece pelo capítulo 1 para descer ao primeiro marco."
        : restante > 0
          ? "Faltam " + restante + " capítulo(s) para o próximo marco."
          : "Todos os capítulos concluídos.";
    }
  }

  function initDepthMeters() {
    var totalChapters = document.querySelectorAll(".sidebar-chapters a[data-chapter-link]").length ||
      document.querySelectorAll(".chapter-card[data-chapter-link]").length;
    if (!totalChapters) return;
    var doneCount = getProgressList().length;

    renderDepthMeter(document.getElementById("homeDepthTrack"), document.getElementById("homeDepthLabel"), doneCount, totalChapters);

    var railDepth = document.getElementById("railDepth");
    if (railDepth) {
      railDepth.innerHTML = '<div class="depth-meter"><div class="depth-meter-track">' +
        '<div class="depth-meter-zone"></div>'.repeat(6) +
        '</div><div class="depth-meter-label"></div></div>';
      renderDepthMeter(railDepth.querySelector(".depth-meter-track"), railDepth.querySelector(".depth-meter-label"), doneCount, totalChapters);
    }
  }

  /* =========================================================================
     9. CONTINUAR (Home)
     ========================================================================= */
  function initContinue() {
    var section = document.getElementById("continueSection");
    if (!section) return;
    var lastId = safeGet(LAST_CHAPTER_KEY);
    if (!lastId) return;

    var sourceCard = document.querySelector('.sidebar-chapters a[data-chapter-link="' + lastId + '"], .chapter-card[data-chapter-link="' + lastId + '"]');
    var title = sourceCard ? sourceCard.textContent.trim() : lastId;

    var card = document.getElementById("continueCard");
    var titleEl = document.getElementById("continueTitle");
    if (card) card.setAttribute("href", "capitulos/" + lastId + ".html");
    if (titleEl) titleEl.textContent = title;
    section.hidden = false;
  }

  /* =========================================================================
     10. NESTE CAPITULO (trilho direito no desktop, bottom sheet no mobile)
     ========================================================================= */
  function buildSectionLink(section) {
    var a = document.createElement("a");
    a.textContent = section.getAttribute("data-section-title");
    a.href = "#";
    a.addEventListener("click", function (e) {
      e.preventDefault();
      section.hidden = false;
      section.scrollIntoView({ behavior: "smooth", block: "start" });
      var sheet = document.getElementById("chapterSheet");
      var backdrop = document.getElementById("chapterSheetBackdrop");
      if (sheet && !sheet.hidden) {
        sheet.hidden = true;
        if (backdrop) backdrop.hidden = true;
      }
    });
    return a;
  }

  function initRailSections() {
    var sections = Array.prototype.slice.call(document.querySelectorAll(".chapter-section[data-section-title]"));
    if (sections.length === 0) return;

    var railNav = document.getElementById("railSections");
    if (railNav) {
      sections.forEach(function (section) { railNav.appendChild(buildSectionLink(section)); });
    }

    var sheetNav = document.getElementById("chapterSheetSections");
    if (sheetNav) {
      sections.forEach(function (section) { sheetNav.appendChild(buildSectionLink(section)); });
    }
  }

  function initChapterSheet() {
    var openBtn = document.getElementById("chapterSheetOpen");
    var sheet = document.getElementById("chapterSheet");
    var backdrop = document.getElementById("chapterSheetBackdrop");
    var closeBtn = document.getElementById("chapterSheetClose");
    if (!openBtn || !sheet || !backdrop) return;

    function open() {
      sheet.hidden = false;
      backdrop.hidden = false;
    }
    function close() {
      sheet.hidden = true;
      backdrop.hidden = true;
    }

    openBtn.addEventListener("click", open);
    if (closeBtn) closeBtn.addEventListener("click", close);
    backdrop.addEventListener("click", close);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });
  }

  /* =========================================================================
     11. PAGINA DE PROGRESSO: resumo + exportar/importar JSON (B-011)
     ========================================================================= */
  var EXPORT_KEYS = [PROGRESS_KEY, LAST_CHAPTER_KEY, LAYER_PREF_KEY, THEME_KEY];

  function initProgressPage() {
    var resumo = document.getElementById("progresso-resumo");
    var track = document.getElementById("progressoDepthTrack");
    var label = document.getElementById("progressoDepthLabel");
    var exportBtn = document.getElementById("export-progress-btn");
    var importInput = document.getElementById("import-progress-input");
    if (!resumo && !exportBtn && !importInput) return;

    var totalChapters = document.querySelectorAll(".chapter-list .chapter-card[data-chapter-link]").length;
    var doneCount = getProgressList().length;

    if (resumo) {
      resumo.textContent = totalChapters
        ? doneCount + " de " + totalChapters + " capítulos concluídos neste navegador."
        : "Nenhum capítulo carregado.";
    }
    if (track) renderDepthMeter(track, label, doneCount, totalChapters);

    if (exportBtn) {
      exportBtn.addEventListener("click", function () {
        var data = {};
        EXPORT_KEYS.forEach(function (key) {
          var value = safeGet(key);
          if (value !== null) data[key] = value;
        });
        var blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "subsea-rafaela-progresso.json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }

    if (importInput) {
      importInput.addEventListener("change", function () {
        var file = importInput.files && importInput.files[0];
        if (!file) return;
        var reader = new FileReader();
        reader.onload = function () {
          try {
            var data = JSON.parse(String(reader.result));
            EXPORT_KEYS.forEach(function (key) {
              if (typeof data[key] === "string") safeSet(key, data[key]);
            });
            window.location.reload();
          } catch (e) {
            window.alert("Arquivo inválido. Exporte de novo a partir de Progresso e tente importar esse arquivo.");
          }
        };
        reader.readAsText(file);
      });
    }
  }

  /* =========================================================================
     Inicializacao
     ========================================================================= */
  function init() {
    populateIcons();
    initTheme();
    initActiveNav();
    initLayerControl();
    initGlossaryPopover();
    initPmTabs();
    initQuiz();
    initMarkDone();
    initChapterCards();
    initDepthMeters();
    initContinue();
    initRailSections();
    initChapterSheet();
    initProgressPage();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
