# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 5 — Sprint 2 concluído e verificado; D-025 registrada a partir de achado do Paulo sobre uso de inglês)
**Versão publicada:** V4.0-sprint1, mergeada na `main` (o merge do Sprint 2 ainda vai acontecer nesta sessão). Site com conteúdo real (24 capítulos + 9 hubs) publicado via GitHub Pages.
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 2 concluído e verificado (design system aplicado a todo o site). Próximo: Sprint 3 (hubs reais: Ementa, Busca, Progresso, Referências, Biblioteca — hoje placeholders).

## Resumo em 10 linhas

1. Sprints 1 e 2 estão fechados. Sprint 1: V3 auditada (Sessão 2) e extraída para o pipeline "conteúdo como dados" (Sessão 3) — 24 capítulos em Markdown, dados em JSON, `src/build.py`, QA e E2E automatizados. Sprint 2 (Sessão 5): DESIGN_SYSTEM_V4.md aplicado às 33 páginas de uma vez (D-023) — ícones SVG, sidebar/tabbar, painel PM em abas, medidor de profundidade, tema escuro, mapa de trilha compacto.
2. Testado de verdade, não só afirmado: `src/scripts/qa.py` (33 páginas, zero erros bloqueantes) e `src/scripts/test_e2e.py` num Chromium real via Playwright, desktop + mobile — 35/35 checagens (camadas, quiz, popover, progresso persistente, glossário, ícones, sidebar/tabbar por viewport, abas do painel PM, bottom sheet de 2 toques, tema escuro, altura da Home).
3. Três bugs reais foram encontrados e corrigidos durante o próprio teste do Sprint 2, não depois de reportado como pronto: Home no mobile media 5219px (~6 telas) na primeira versão, corrigida para 1748px com mapa de trilha compacto; botão de tema escuro só existia no desktop, faltando no mobile; trilho "Neste capítulo" (acesso ao painel PM) era desktop-only, faltando o "2 toques" no mobile que o próprio checklist exige.
4. O checklist de aprovação do DESIGN_SYSTEM_V4.md seção 9 está com 5 de 7 itens verificados automaticamente; os 2 restantes (medidor nomear a próxima fase, e o Paulo descrever a identidade em uma frase) dependem de B-026 e do teste real do Paulo, respectivamente.
5. **Achado do Paulo nesta sessão, revisando uma captura do capítulo 17:** uso de inglês por inércia da fonte (ex.: "hydraulic power", "transfer load" numa tabela) que não reflete fala real de reunião no Brasil — diferente de "pull-in", que é dito em inglês de verdade. D-025 registrada, apertando o critério de D-019 (português é o default; inglês só com evidência de uso oral real). B-040 aberto, ampliando o escopo de B-030/B-031 para os Sprints 4 a 6, com o m17 como primeiro capítulo a corrigir.
6. Conteúdo técnico preservado sem perda desde o Sprint 1 (verificado por contagem de palavras); os pontos de reescrita (camadas rasas, glossário genérico, quiz fraco, agora também uso de inglês) seguem sinalizados para os Sprints 4 a 6.
7. O CI (`qa-governanca.yml`) continua com dois jobs (`qa-governanca` e `qa-tecnico`) e o fluxo branch → commit → PR → checar CI → merge continua sendo conduzido inteiramente pelo Claude (D-021); nenhuma ação manual do Paulo no GitHub.
8. Decisões vigentes acumuladas: D-004 a D-025 (ver DECISOES.md). Nenhuma decisão pendente no momento.
9. O Paulo ainda não testou o site publicado num dispositivo real — isso é D-009 e faz mais sentido depois que este merge do Sprint 2 publicar via GitHub Pages.
10. Pendentes sem bloquear o entregue: B-038 (fontes Inter/Sora locais, falta acesso de rede), B-039 (ajustes visuais do Paulo pós-publicação), B-026 (mapeamento capítulo→fase), B-040 (revisão crítica de inglês, novo), Sprint 3 (hubs reais) e Sprints 4-6 (profundidade de conteúdo).

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
