/**
 * SUBSEA_ICONS — conjunto próprio de ícones SVG inline (Plataforma Subsea Rafaela)
 *
 * Padrão (ver governanca/DESIGN_SYSTEM_V4.md, seção 3.4 — Iconografia):
 *   - viewBox="0 0 24 24"
 *   - fill="none", stroke="currentColor"
 *   - stroke-width="1.75", stroke-linecap="round", stroke-linejoin="round"
 *   - sem width/height fixos (controlado por CSS, ex.: width:1em; height:1em)
 *   - sem emoji, sem glifos de fonte externa
 *
 * Uso:
 *   window.SUBSEA_ICONS['home']            -> string SVG completa
 *   window.SUBSEA_ICON('home', 'icon-lg')  -> mesma string com class="icon-lg" adicionada
 */
(function (global) {
  'use strict';

  var ATTR = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"';

  function svg(inner) {
    return '<svg xmlns="http://www.w3.org/2000/svg" ' + ATTR + '>' + inner + '</svg>';
  }

  var ICONS = {

    // 1. home — casa simples (telhado triangular + corpo retangular)
    home: svg(
      '<path d="M4 11.5 12 4l8 7.5"/>' +
      '<path d="M6 10.5V20h12v-9.5"/>' +
      '<path d="M10 20v-5.5h4V20"/>'
    ),

    // 2. trilha — sequência de pontos conectados (progresso da trilha)
    trilha: svg(
      '<path d="M4 19c3-1 3-4 6-4s3 3 6 3 3-4 4-6"/>' +
      '<circle cx="4" cy="19" r="1.4"/>' +
      '<circle cx="10" cy="15" r="1.4"/>' +
      '<circle cx="16" cy="18" r="1.4"/>' +
      '<circle cx="20" cy="12" r="1.4"/>'
    ),

    // 3. busca — lupa (círculo + linha diagonal)
    busca: svg(
      '<circle cx="10.5" cy="10.5" r="6.5"/>' +
      '<line x1="15.5" y1="15.5" x2="20.5" y2="20.5"/>'
    ),

    // 4. glossario — livro aberto simples
    glossario: svg(
      '<path d="M12 6.5c-1.7-1.3-4-2-6.5-2v13c2.5 0 4.8.7 6.5 2 1.7-1.3 4-2 6.5-2v-13c-2.5 0-4.8.7-6.5 2Z"/>' +
      '<line x1="12" y1="6.5" x2="12" y2="19.5"/>'
    ),

    // 5. prompts — balão de fala com asterisco (IA / prompt)
    prompts: svg(
      '<path d="M4 5.5h16v10H10l-4 3.5v-3.5H4Z"/>' +
      '<path d="M12 7.5v4"/>' +
      '<path d="M10 8.8l4 1.4"/>' +
      '<path d="M14 8.8l-4 1.4"/>'
    ),

    // 6. biblioteca — pilha de livros vista de lado
    biblioteca: svg(
      '<rect x="3.5" y="4" width="4" height="16" rx="0.6"/>' +
      '<rect x="8.5" y="4" width="4" height="16" rx="0.6"/>' +
      '<path d="M14 5.2l4.3-1.1 3.1 15.5-4.3 1.1Z"/>'
    ),

    // 7. progresso — gráfico de barras ascendente
    progresso: svg(
      '<line x1="4" y1="20" x2="20" y2="20"/>' +
      '<rect x="6" y="14" width="3" height="6"/>' +
      '<rect x="11" y="10" width="3" height="10"/>' +
      '<rect x="16" y="6" width="3" height="14"/>'
    ),

    // 8. referencias — documento com seta apontando para fora (link externo)
    referencias: svg(
      '<path d="M13 4H6.5A1.5 1.5 0 0 0 5 5.5v13A1.5 1.5 0 0 0 6.5 20h11a1.5 1.5 0 0 0 1.5-1.5V11"/>' +
      '<path d="M14 4h5v5"/>' +
      '<line x1="19" y1="4" x2="11" y2="12"/>'
    ),

    // 9. anterior — chevron-left
    anterior: svg(
      '<polyline points="14.5,5 8,12 14.5,19"/>'
    ),

    // 10. proximo — chevron-right
    proximo: svg(
      '<polyline points="9.5,5 16,12 9.5,19"/>'
    ),

    // 11. concluido — check mark dentro de um círculo
    concluido: svg(
      '<circle cx="12" cy="12" r="8.5"/>' +
      '<polyline points="8,12.3 10.8,15 16,9.5"/>'
    ),

    // 12. atencao — triângulo com exclamação (warning)
    atencao: svg(
      '<path d="M12 4.2 21 19H3Z"/>' +
      '<line x1="12" y1="10" x2="12" y2="14.2"/>' +
      '<circle cx="12" cy="16.8" r="0.15" fill="currentColor"/>'
    ),

    // 13. pergunta — ponto de interrogação dentro de um círculo
    pergunta: svg(
      '<circle cx="12" cy="12" r="8.5"/>' +
      '<path d="M9.8 9.6a2.2 2.2 0 1 1 3.4 1.8c-.9.6-1.2 1-1.2 2"/>' +
      '<circle cx="12" cy="16.3" r="0.15" fill="currentColor"/>'
    ),

    // 14. documento — folha com linhas de texto e canto dobrado
    documento: svg(
      '<path d="M7 3.5h7l4 4V20a.9.9 0 0 1-.9.9H7a.9.9 0 0 1-.9-.9V4.4a.9.9 0 0 1 .9-.9Z"/>' +
      '<polyline points="14,3.5 14,7.5 18,7.5"/>' +
      '<line x1="9" y1="12" x2="15" y2="12"/>' +
      '<line x1="9" y1="15.2" x2="15" y2="15.2"/>' +
      '<line x1="9" y1="18.4" x2="12.5" y2="18.4"/>'
    ),

    // 15. red_flag — bandeirola triangular presa a um mastro vertical
    red_flag: svg(
      '<line x1="6" y1="3.5" x2="6" y2="20.5"/>' +
      '<path d="M6 4.5h12l-3.5 4L18 12.5H6Z"/>'
    ),

    // 16. copiar — dois retângulos sobrepostos
    copiar: svg(
      '<rect x="9" y="9" width="10.5" height="10.5" rx="1"/>' +
      '<path d="M14.5 9V5.5A1.5 1.5 0 0 0 13 4H5.5A1.5 1.5 0 0 0 4 5.5V13a1.5 1.5 0 0 0 1.5 1.5H9"/>'
    ),

    // 17. expandir — setas diagonais apontando para fora dos cantos opostos
    expandir: svg(
      '<polyline points="9,4.5 4.5,4.5 4.5,9"/>' +
      '<polyline points="15,19.5 19.5,19.5 19.5,15"/>' +
      '<line x1="4.5" y1="4.5" x2="10.2" y2="10.2"/>' +
      '<line x1="19.5" y1="19.5" x2="13.8" y2="13.8"/>'
    ),

    // 18. tema — círculo meio preenchido (sol/lua)
    tema: svg(
      '<circle cx="12" cy="12" r="8.5"/>' +
      '<path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/>'
    ),

    // 19. menu — três linhas horizontais (hamburger)
    menu: svg(
      '<line x1="4" y1="6.5" x2="20" y2="6.5"/>' +
      '<line x1="4" y1="12" x2="20" y2="12"/>' +
      '<line x1="4" y1="17.5" x2="20" y2="17.5"/>'
    ),

    // 20. fechar — X simples
    fechar: svg(
      '<line x1="6" y1="6" x2="18" y2="18"/>' +
      '<line x1="18" y1="6" x2="6" y2="18"/>'
    ),

    // 21. profundidade — ondas horizontais empilhadas
    profundidade: svg(
      '<path d="M3 8c2 1.4 4 1.4 6 0s4-1.4 6 0 4 1.4 6 0"/>' +
      '<path d="M3 13.2c2 1.4 4 1.4 6 0s4-1.4 6 0 4 1.4 6 0"/>' +
      '<path d="M3 18.4c2 1.4 4 1.4 6 0s4-1.4 6 0 4 1.4 6 0"/>'
    ),

    // 22. badge — escudo simples
    badge: svg(
      '<path d="M12 3.5 19 6v6c0 4.5-3 7.3-7 8.5-4-1.2-7-4-7-8.5V6Z"/>' +
      '<polyline points="9,12 11.2,14.2 15.2,9.8"/>'
    ),

    // 23. missao — alvo (círculos concêntricos)
    missao: svg(
      '<circle cx="12" cy="12" r="8.5"/>' +
      '<circle cx="12" cy="12" r="5"/>' +
      '<circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/>'
    ),

    // 24. llm — chip/circuito com pinos nas bordas
    llm: svg(
      '<rect x="7" y="7" width="10" height="10" rx="1.2"/>' +
      '<circle cx="12" cy="12" r="2.2"/>' +
      '<line x1="12" y1="2.5" x2="12" y2="7"/>' +
      '<line x1="12" y1="17" x2="12" y2="21.5"/>' +
      '<line x1="2.5" y1="12" x2="7" y2="12"/>' +
      '<line x1="17" y1="12" x2="21.5" y2="12"/>' +
      '<line x1="5.5" y1="5.5" x2="8.5" y2="8.5"/>' +
      '<line x1="15.5" y1="15.5" x2="18.5" y2="18.5"/>' +
      '<line x1="18.5" y1="5.5" x2="15.5" y2="8.5"/>' +
      '<line x1="8.5" y1="15.5" x2="5.5" y2="18.5"/>'
    ),

    // 25. foto — câmera simples (retângulo + círculo lente)
    foto: svg(
      '<path d="M4 8h3.2l1.4-2h6.8l1.4 2H20v11H4Z"/>' +
      '<circle cx="12" cy="13.5" r="3.3"/>'
    ),

    // 26. diagrama — fluxograma com retângulos e seta
    diagrama: svg(
      '<rect x="3" y="4.5" width="6" height="4.5" rx="0.8"/>' +
      '<rect x="15" y="4.5" width="6" height="4.5" rx="0.8"/>' +
      '<rect x="9" y="15" width="6" height="4.5" rx="0.8"/>' +
      '<path d="M9 6.8h4.5"/>' +
      '<polyline points="12,5.3 13.8,6.8 12,8.3"/>' +
      '<path d="M12 9v3.5"/>' +
      '<polyline points="10.5,11 12,12.8 13.5,11"/>'
    ),

    // 27. etapa — círculo numerado vazio / marcador de passo
    etapa: svg(
      '<circle cx="12" cy="12" r="8.5"/>' +
      '<circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/>'
    ),

    // 28. exportar — seta saindo de uma caixa, apontando para cima
    exportar: svg(
      '<path d="M5 14v4.5A1.5 1.5 0 0 0 6.5 20h11a1.5 1.5 0 0 0 1.5-1.5V14"/>' +
      '<line x1="12" y1="14.5" x2="12" y2="4"/>' +
      '<polyline points="8.2,7.8 12,4 15.8,7.8"/>'
    ),

    // 29. importar — seta entrando numa caixa, apontando para baixo
    importar: svg(
      '<path d="M5 14v4.5A1.5 1.5 0 0 0 6.5 20h11a1.5 1.5 0 0 0 1.5-1.5V14"/>' +
      '<line x1="12" y1="4" x2="12" y2="14.5"/>' +
      '<polyline points="8.2,10.7 12,14.5 15.8,10.7"/>'
    ),

    // 30. feedback — balão de fala com exclamação
    feedback: svg(
      '<path d="M4 5.5h16v10H10l-4 3.5v-3.5H4Z"/>' +
      '<line x1="12" y1="8" x2="12" y2="11.6"/>' +
      '<circle cx="12" cy="14" r="0.15" fill="currentColor"/>'
    )

  };

  global.SUBSEA_ICONS = ICONS;

  global.SUBSEA_ICON = function (name, extraClass) {
    var markup = ICONS[name];
    if (!markup) return '';
    if (extraClass) {
      markup = markup.replace('<svg ', '<svg class="' + extraClass + '" ');
    }
    return markup;
  };

})(typeof window !== 'undefined' ? window : this);
