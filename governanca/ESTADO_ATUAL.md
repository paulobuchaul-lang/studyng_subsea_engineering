# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 6 — Sprint 3 concluído e verificado: hubs reais, busca determinística, exportar/importar progresso)
**Versão publicada:** `main` inclui Sprint 1 e Sprint 2 (o merge do Sprint 3 ainda vai acontecer nesta sessão). Site com conteúdo real (24 capítulos + 9 hubs) publicado via GitHub Pages. Paulo já abriu o site publicado e considerou "ok para uma primeira versão".
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 3 concluído e verificado (hubs reais: Treinamento, Busca, Biblioteca Visual, Progresso, Referências). Próximo: Sprint 4 (capítulos 01 a 08 no novo shell, com a rubrica de excelência de AUDITORIA_CONTEUDO_DIDATICA_V4.md aplicada de verdade, inclusive o critério de inglês de D-025).

## Resumo em 10 linhas

1. Sprints 1, 2 e 3 estão fechados. Sprint 1: V3 auditada e extraída para "conteúdo como dados". Sprint 2: DESIGN_SYSTEM_V4.md aplicado às 33 páginas. Sprint 3 (Sessão 6): os 5 hubs que eram placeholder desde o Sprint 1 (Treinamento, Busca, Biblioteca Visual, Progresso, Referências) ganharam implementação real.
2. **Referências** agrega 54 fontes reais já citadas nos 24 capítulos (extraídas por script, nenhuma inventada), agrupadas por categoria. **Busca** tem resultado determinístico via `aliases.json` — buscar "pull in" e apertar Enter abre o capítulo 17, exatamente o critério de aceite do ROADMAP. **Biblioteca Visual** tem filtro funcional com estado vazio honesto (dados reais só no Sprint 7). **Progresso** lista os 24 capítulos com estado real e ganhou exportar/importar em JSON (B-011), testado com round-trip completo.
3. Testado de verdade: `src/scripts/qa.py` (33 páginas, zero erros bloqueantes) e `src/scripts/test_e2e.py` num Chromium real via Playwright, desktop + mobile — 48/48 checagens.
4. **Bug real encontrado e corrigido durante o próprio teste:** o script de QA acusava um link quebrado em `search.html` que não existia de verdade — ele lia `href="..."` no arquivo inteiro, inclusive dentro do `<script>` que monta HTML por concatenação de string. Corrigido (B-041).
5. Achado do Paulo na sessão anterior sobre uso excessivo de inglês herdado da fonte (D-025, B-040) segue registrado e sinalizado para os Sprints 4 a 6 — não foi tocado nesta sessão, que foi só plumbing de hub.
6. B-026 (mapeamento capítulo→fase) permanece deliberadamente não resolvido: é decisão de currículo (avaliar peso pedagógico, decidir fusões/divisões de capítulo) que cabe junto da reescrita de conteúdo dos Sprints 4 a 6, não como parte do trabalho de hub do Sprint 3.
7. Conteúdo técnico preservado sem perda desde o Sprint 1; os pontos de reescrita (camadas rasas, glossário genérico, quiz fraco, uso de inglês) seguem sinalizados para os Sprints 4 a 6.
8. O CI (`qa-governanca.yml`) continua com dois jobs e o fluxo branch → commit → PR → checar CI → merge continua sendo conduzido inteiramente pelo Claude (D-021); nenhuma ação manual do Paulo no GitHub.
9. Decisões vigentes acumuladas: D-004 a D-025 (ver DECISOES.md). Nenhuma decisão pendente no momento.
10. Pendentes sem bloquear o entregue: B-038 (fontes Inter/Sora locais), B-039 (ajustes visuais do Paulo), B-026 (mapeamento capítulo→fase), B-040 (revisão crítica de inglês), Sprint 4 a 6 (profundidade de conteúdo).

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
| 4 | 07/09/2026 | D-022 registrada: chunking por camada dentro da página, nunca por sequência de páginas/wizard; rubrica e design system atualizados | Sprint 2 |
| 5 | 07/09/2026 | Sprint 2 concluído: design system aplicado às 33 páginas (ícones, CSS, JS, templates), ARQUITETURA_MESTRE_V4.md consolidado, 3 bugs reais encontrados e corrigidos durante o teste (altura da Home, tema escuro no mobile, acesso ao painel PM no mobile), 35/35 checagens E2E passando. D-025 registrada a partir de achado do Paulo sobre uso excessivo de inglês herdado da fonte no conteúdo | Commit/PR/CI/merge desta sessão; depois Sprint 3 (hubs reais) |
| 6 | 07/09/2026 | Paulo testou o site publicado e aprovou como "ok para uma primeira versão". Sprint 3 concluído: Treinamento, Busca, Biblioteca Visual, Progresso e Referências implementados de verdade (antes placeholder); busca determinística via aliases; exportar/importar progresso (B-011); 54 referências extraídas dos capítulos; bug real de QA corrigido (B-041); 48/48 checagens E2E passando | Commit/PR/CI/merge desta sessão; depois Sprint 4 (capítulos 01-08 com rubrica de excelência) |
