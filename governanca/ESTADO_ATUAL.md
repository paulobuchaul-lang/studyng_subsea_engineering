# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 3 — Sprint 1 concluído: fundação técnica, primeiro site real gerado, testado em navegador real e mergeado)
**Versão publicada:** V4.0-sprint1, mergeada na `main`. Site com conteúdo real (24 capítulos + 9 hubs) pronto para ser publicado via GitHub Pages assim que o merge desta sessão for concluído.
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 1 CONCLUÍDO (Partes A e B). Próximo: Sprint 2 — design system e protótipo (ver ROADMAP_V4.md).

## Resumo em 10 linhas

1. O Sprint 1 está fechado: a V3 foi auditada (Sessão 2) e depois extraída para o pipeline "conteúdo como dados" (Sessão 3) — 24 capítulos em Markdown, glossário/prompts/aliases em JSON, um `src/build.py` que gera as 33 páginas do site, um script de QA e um teste E2E em navegador real.
2. O site gerado foi testado de verdade: `src/scripts/qa.py` (links, IDs, blocos obrigatórios, img externo — zero erros) e `src/scripts/test_e2e.py` num Chromium real via Playwright, em desktop e mobile (20/20 checagens: camadas de profundidade, quiz, popover de termo, progresso persistente, filtro de glossário, zero erro JS, zero overflow horizontal).
3. O design ainda é um esqueleto funcional, não o DESIGN_SYSTEM_V4.md completo — isso é o Sprint 2, o próximo passo.
4. Conteúdo técnico preservado sem perda (verificado por contagem de palavras); os pontos que a auditoria de conteúdo (AUDITORIA_CONTEUDO_DIDATICA_V4.md) marcou para reescrita (camadas rasas, glossário genérico, quiz com distratores fracos) estão sinalizados com comentários `REESCREVER(...)` dentro de cada `src/content/mNN.md`, para os Sprints 4 a 6.
5. O popover de termo do glossário (D-019/B-035) foi corrigido: sem o teto de 18 ocorrências por página que a V3 tinha; todo termo do glossário presente no texto é marcado.
6. O CI (`qa-governanca.yml`) agora tem dois jobs: `qa-governanca` (documentos, links internos, CHANGELOG/ESTADO_ATUAL atualizados) e `qa-tecnico` (roda o build e o QA do site a cada push/PR).
7. O fluxo de branch → commit → PR → checar CI → merge continua sendo conduzido inteiramente pelo Claude (D-021); nenhuma ação manual do Paulo é necessária no GitHub.
8. Decisões vigentes acumuladas: D-004 a D-021 (ver DECISOES.md para o texto completo de cada uma). Nenhuma decisão pendente no momento.
9. O Paulo ainda não testou o site publicado num dispositivo real — isso é D-009 e só faz sentido depois que o GitHub Pages servir esta `main` atualizada.
10. A Biblioteca Visual (Sprint 7), a verificação factual dos casos Brasil com data (V4.1, D-017) e a reescrita completa do glossário/camadas de profundidade (Sprints 4 a 6) continuam pendentes, sem bloquear o que já foi entregue.

## O que a Sessão 3 entregou

- `src/scripts/extrair_capitulos.py`, `src/scripts/gerar_inventario.py`, `src/scripts/qa.py`, `src/scripts/test_e2e.py`.
- `src/data/glossario.json` (126), `src/data/prompts.json` (28), `src/data/aliases.json` (38), `src/data/biblioteca.json` (vazio, com schema documentado).
- `src/content/m01.md` a `m24.md`.
- `src/templates/*.html` (base, capítulo, home, hub de lista, glossário, prompts, placeholder).
- `src/build.py`, `src/requirements.txt`, `src/requirements-dev.txt`.
- `assets/styles.css`, `assets/app.js` — CSS/JS funcionais (camadas, quiz, popover, progresso), sem o design final do Sprint 2.
- Site gerado: `index.html`, `ementa.html`, `treinamento.html`, `glossario.html`, `prompts.html`, `biblioteca.html`, `progresso.html`, `referencias.html`, `search.html`, `capitulos/m01.html` a `m24.html`.
- `INVENTARIO_V3.json`.
- CI estendido com o job `qa-tecnico`.
- Um bug real encontrado e corrigido pelo teste E2E: tabelas sem scroll horizontal próprio estourando a largura em mobile (390px).

## O que ainda falta (não bloqueia o que foi entregue)

- **Teste em dispositivo real (D-009):** só faz sentido depois que este merge publicar via GitHub Pages. Ação do Paulo quando a URL estiver servindo o conteúdo novo.
- **Sprint 2 (design system):** aplicar DESIGN_SYSTEM_V4.md de verdade sobre este esqueleto.
- **Sprints 4 a 6:** reescrever camadas de profundidade, quiz e glossário conforme a rubrica da auditoria — os comentários `REESCREVER(...)` em cada `.md` apontam exatamente onde.
- **Sprint 7:** Biblioteca Visual com imagens licenciadas (hoje todo hotlink virou "cartão de fonte" sem `<img>`, conforme D-007 — confirmado por QA, zero `<img>` externo).

## Riscos abertos

- A extração dos capítulos do HTML para Markdown é scriptável, mas blocos com estrutura irregular podem exigir revisão manual em capítulos ainda não lidos integralmente durante a auditoria (só 5 dos 24 foram lidos por completo). O QA técnico não substitui uma segunda leitura humana de amostra.
- Imagens de fornecedores: mesmo com nova estratégia, pode não haver foto licenciável para todo equipamento. Nesses casos o cartão de fonte substitui a foto, sem imagem quebrada (já é o comportamento atual).

## Histórico de sessões

| Sessão | Data | Entregou | Próximo passo definido |
|---|---|---|---|
| 0 | 06/09/2026 | Diagnóstico da V3, kit de governança V4 (9 documentos), roadmap por sprints; zip da V3 recebido e inspecionado | Paulo publica a V3 para teste, decide D-004a/D-005/D-006; Sprint 1 |
| 1 | 07/09/2026 | Repositório GitHub organizado: pasta `/governanca/` com os 9 .md, esqueleto `/src/`, `.nojekyll`, README raiz reescrito; D-004a, D-005 e D-006 decididas pelo Paulo (público, pipeline adotado, design aprovado) | Paulo reenvia zip completo da V3 e ativa GitHub Pages; próxima sessão escreve build.py e extrai conteúdo |
| 2 | 07/09/2026 | Zip completo da V3 recebido e inspecionado por inteiro; GitHub Pages ativado pelo Paulo; auditoria de conteúdo/didática/UX/gamificação conduzida (AUDITORIA_CONTEUDO_DIDATICA_V4.md); D-015 a D-019 decididas; automação de governança via CI (D-020) e fluxo de branch/PR/merge assumido integralmente pelo Claude (D-021); B-030 a B-036 fechados ou abertos conforme aplicável | Próxima sessão inicia Parte B do Sprint 1 (extração técnica) |
| 3 | 07/09/2026 | Sprint 1 Parte B concluído: extração de conteúdo, build.py, QA automatizado, teste E2E em navegador real (20/20), CI estendido com qa-tecnico, site completo gerado e mergeado | Sprint 2 (design system e protótipo); Paulo testa em dispositivo real assim que Pages publicar |
