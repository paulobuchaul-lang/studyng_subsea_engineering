/* =========================================================================
   Plataforma Subsea Rafaela — app.js (Sprint 1)
   -------------------------------------------------------------------------
   Funcionalidade minima e essencial: controle de camadas de profundidade,
   popover de termos do glossario, feedback de quiz, e progresso simples
   (marcar capitulo como estudado) via localStorage.
   Sem XP, sem gamificacao avancada, sem confete — isso fica para sprints
   futuros. Este script assume que, quando presente, window.SUBSEA_GLOSSARIO
   ja foi injetado pelo build.py ANTES deste arquivo ser carregado.
   ========================================================================= */

(function () {
  "use strict";

  var LAYER_PREF_KEY = "subsea_layer_pref";
  var PROGRESS_KEY = "subsea_progress";

  /* -----------------------------------------------------------------------
     Utilitarios de localStorage — protegidos contra ambientes que bloqueiam
     acesso (modo privado, etc.), para nunca quebrar a pagina por causa disso.
     ----------------------------------------------------------------------- */

  function safeGet(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function safeSet(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (e) {
      /* ignorar — preferencia nao persistida, mas a pagina segue funcional */
    }
  }

  function getProgressList() {
    var raw = safeGet(PROGRESS_KEY);
    if (!raw) {
      return [];
    }
    try {
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function addToProgress(chapterId) {
    var list = getProgressList();
    if (list.indexOf(chapterId) === -1) {
      list.push(chapterId);
      safeSet(PROGRESS_KEY, JSON.stringify(list));
    }
  }

  /* =========================================================================
     1. CONTROLE DE CAMADAS DE PROFUNDIDADE
     ========================================================================= */

  function initLayerControl() {
    var control = document.querySelector(".layer-control");
    if (!control) {
      return;
    }

    var buttons = Array.prototype.slice.call(
      control.querySelectorAll(".layer-btn")
    );
    var sections = Array.prototype.slice.call(
      document.querySelectorAll(".chapter-section")
    );

    if (buttons.length === 0) {
      return;
    }

    function applyLayer(layer) {
      sections.forEach(function (section) {
        var raw = section.getAttribute("data-layer");
        if (!raw) {
          /* Sem data-layer: sempre visivel (ex.: quiz). */
          section.hidden = false;
          return;
        }
        if (layer === "all") {
          section.hidden = false;
          return;
        }
        var values = raw.split(/\s+/);
        section.hidden = values.indexOf(layer) === -1;
      });

      buttons.forEach(function (btn) {
        var isActive = btn.getAttribute("data-layer-btn") === layer;
        btn.classList.toggle("active", isActive);
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
    var validValues = buttons.map(function (btn) {
      return btn.getAttribute("data-layer-btn");
    });
    var initial = saved && validValues.indexOf(saved) !== -1 ? saved : "all";
    applyLayer(initial);
  }

  /* =========================================================================
     2. TERMOS DO GLOSSARIO (POPOVER)
     ========================================================================= */

  function findGlossaryEntry(term) {
    var list = window.SUBSEA_GLOSSARIO;
    if (!Array.isArray(list) || !term) {
      return null;
    }
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
    if (existing) {
      return existing;
    }

    var popover = document.createElement("div");
    popover.id = "term-popover";
    popover.className = "term-popover";
    popover.hidden = true;
    popover.innerHTML =
      '<h4 class="term-title"></h4>' +
      '<p class="term-full"></p>' +
      '<p class="term-def"></p>' +
      '<p class="term-why"></p>' +
      '<a class="term-more" href="#">Ver no glossário</a>' +
      '<button type="button" class="term-close">Fechar</button>';
    document.body.appendChild(popover);
    return popover;
  }

  function initGlossaryPopover() {
    var terms = Array.prototype.slice.call(document.querySelectorAll(".term"));
    if (terms.length === 0) {
      return;
    }

    var popover = buildPopover();
    var titleEl = popover.querySelector(".term-title");
    var fullEl = popover.querySelector(".term-full");
    var defEl = popover.querySelector(".term-def");
    var whyEl = popover.querySelector(".term-why");
    var moreEl = popover.querySelector(".term-more");
    var closeEl = popover.querySelector(".term-close");

    function hidePopover() {
      popover.hidden = true;
    }

    function positionNear(target) {
      var rect = target.getBoundingClientRect();
      var margin = 8;

      /* Precisamos medir o popover; garantimos que ele esteja visivel
         (mas fora da tela) antes de medir, para pegar dimensoes reais. */
      popover.style.visibility = "hidden";
      popover.hidden = false;

      var popRect = popover.getBoundingClientRect();
      var popWidth = popRect.width || 300;
      var popHeight = popRect.height || 160;

      var top = rect.bottom + margin;
      if (top + popHeight > window.innerHeight) {
        top = rect.top - popHeight - margin;
        if (top < margin) {
          top = margin;
        }
      }

      var left = rect.left;
      if (left + popWidth > window.innerWidth - margin) {
        left = window.innerWidth - popWidth - margin;
      }
      if (left < margin) {
        left = margin;
      }

      popover.style.top = top + "px";
      popover.style.left = left + "px";
      popover.style.visibility = "";
    }

    function showFor(target) {
      var term = target.getAttribute("data-term") || target.textContent;
      var entry = findGlossaryEntry(term);

      if (!entry) {
        /* Termo marcado sem entrada correspondente no glossario:
           evita quebrar a pagina, apenas nao abre popover. */
        return;
      }

      titleEl.textContent = entry.term || "";
      fullEl.textContent = entry.full || "";
      fullEl.hidden = !entry.full;
      defEl.textContent = entry.definition || "";
      whyEl.textContent = entry.why ? "Por que importa: " + entry.why : "";
      whyEl.hidden = !entry.why;

      var id = entry.id || "";
      moreEl.setAttribute("href", "glossario.html#" + id);

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

      if (window.matchMedia && window.matchMedia("(hover: hover)").matches) {
        term.addEventListener("mouseenter", function () {
          showFor(term);
        });
      }
    });

    closeEl.addEventListener("click", function (event) {
      event.stopPropagation();
      hidePopover();
    });

    popover.addEventListener("click", function (event) {
      event.stopPropagation();
    });

    document.addEventListener("click", function (event) {
      if (!popover.hidden && !popover.contains(event.target)) {
        hidePopover();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        hidePopover();
      }
    });
  }

  /* =========================================================================
     3. QUIZ
     ========================================================================= */

  function initQuiz() {
    var questions = Array.prototype.slice.call(
      document.querySelectorAll(".quiz-question")
    );

    questions.forEach(function (question) {
      var correctAnswer = question.getAttribute("data-answer");
      var feedbackText = question.getAttribute("data-feedback") || "";
      var feedbackEl = question.querySelector(".quiz-feedback");
      var options = Array.prototype.slice.call(
        question.querySelectorAll(".quiz-option")
      );

      options.forEach(function (option) {
        option.addEventListener("click", function () {
          var choice = option.getAttribute("data-choice");

          if (!feedbackEl) {
            return;
          }

          if (choice === correctAnswer) {
            option.classList.remove("incorrect");
            option.classList.add("correct");
            feedbackEl.textContent = "Certo! " + feedbackText;
            feedbackEl.hidden = false;

            options.forEach(function (opt) {
              opt.disabled = true;
            });
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
     4. PROGRESSO — marcar capitulo como estudado / marcar cartoes concluidos
     ========================================================================= */

  function setDoneState(button) {
    button.textContent = "✓ Estudado";
    button.classList.add("done");
  }

  function initMarkDone() {
    var button = document.querySelector(".mark-done");
    if (!button) {
      return;
    }

    var chapterId =
      button.getAttribute("data-chapter") ||
      document.body.getAttribute("data-chapter-id");

    if (chapterId && getProgressList().indexOf(chapterId) !== -1) {
      setDoneState(button);
    }

    button.addEventListener("click", function () {
      if (!chapterId) {
        return;
      }
      addToProgress(chapterId);
      setDoneState(button);
    });
  }

  function initChapterCards() {
    var cards = Array.prototype.slice.call(
      document.querySelectorAll(".chapter-card")
    );
    if (cards.length === 0) {
      return;
    }

    var progress = getProgressList();

    cards.forEach(function (card) {
      var chapterId = card.getAttribute("data-chapter-link");
      if (chapterId && progress.indexOf(chapterId) !== -1) {
        card.classList.add("done");
      }
    });
  }

  /* =========================================================================
     Inicializacao
     ========================================================================= */

  function init() {
    initLayerControl();
    initGlossaryPopover();
    initQuiz();
    initMarkDone();
    initChapterCards();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
