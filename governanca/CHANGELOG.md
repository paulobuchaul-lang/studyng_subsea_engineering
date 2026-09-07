# CHANGELOG.md — Plataforma Subsea Rafaela

Formato: versão · data · escopo · itens. Ordem: mais recente primeiro.

## [V4.0] — em desenvolvimento
**Escopo:** hospedagem como site estático, redesign completo da UX, pipeline de conteúdo, biblioteca visual licenciada, quiz com raciocínio, gamificação por profundidade.
**Sprint atual:** 1 (ver ROADMAP_V4.md).

### Sessão 1 — 07/09/2026 — Organização inicial do repositório GitHub + decisões D-004a/D-005/D-006
- Repositório `paulobuchaul-lang/studyng_subsea_engineering` estruturado: pasta `/governanca/` recebeu cópia dos 9 documentos de governança (CLAUDE.md, ESTADO_ATUAL.md, ROADMAP_V4.md, DECISOES.md, BACKLOG.md, CHANGELOG.md, DESIGN_SYSTEM_V4.md, GUIA_PUBLICACAO.md, DIAGNOSTICO_V3.md).
- Esqueleto técnico do Sprint 1 criado (`/src/content/`, `/src/data/`, `/src/templates/`), vazio e com README explicando a dependência do reenvio do zip completo da V3.
- `.nojekyll` e `.gitignore` adicionados na raiz, preparando a hospedagem estática (D-004).
- README.md raiz reescrito com descrição real do projeto, status e estrutura.
- D-004a decidida: GitHub Pages público, no repositório já existente.
- D-005 decidida: adotar o pipeline "conteúdo como dados, shell como código".
- D-006 decidida: direção de design de DESIGN_SYSTEM_V4.md aprovada para protótipo no Sprint 2.
- D-014 registrada: nesta sessão não se criou `src/build.py` nem se migrou conteúdo da V3, porque os 47 arquivos originais da V3 não foram reenviados (só a governança chegou). B-028 (reenvio da V3) e B-029 (ativação manual do GitHub Pages) abertos no backlog para destravar o restante do Sprint 1.
- Nenhum conteúdo técnico dos capítulos, glossário, prompts ou quiz foi tocado nesta sessão.

### Sessão 0 — 06/09/2026 — Governança
- Diagnóstico completo da V3 (DIAGNOSTICO_V3.md).
- Criação de ESTADO_ATUAL.md, DECISOES.md, BACKLOG.md, CHANGELOG.md, ROADMAP_V4.md, DESIGN_SYSTEM_V4.md, GUIA_PUBLICACAO.md.
- CLAUDE.md atualizado com Parte 0 (protocolo de sessão) preservando integralmente as seções 1 a 30 originais.
- Decisões D-004, D-007 a D-013 registradas como vigentes; D-004a, D-005 e D-006 aguardam o Paulo.
- Zip completo da V3 recebido e inspecionado (47 arquivos; data.js com glossário, prompts e aliases estruturados).
- D-013: a V3 é insumo, não fonte de verdade.

## [V3.0] — 06/09/2026 — Multipágina
- 33 páginas HTML: Home, Ementa, Treinamento, Glossário, Prompts, Biblioteca Visual, Progresso, Referências, Busca e 24 capítulos.
- 126 termos de glossário, 28 prompts profissionais, 72 questões de quiz, 13 diagramas auditados.
- Navegação Anterior/Próximo, "capítulo X de 24", "continuar de onde parou".
- Ponte via window.name para uso por file:// (removida na V4 por D-004).
- QA: 0 links locais quebrados, 0 IDs duplicados, 0 erros JS no roteiro; teste de viewport 1440 px e 390 px.
- Problema conhecido: nunca publicada em servidor web; imagens hotlinkadas não carregam.

## [V2.0] — 2026 — Página única expandida
- Estrutura padrão de capítulo, camadas de profundidade, painel PM, quizzes, gamificação, glossário contextual, biblioteca de prompts, diagramas interativos.
- Base de requisitos consolidada em ARQUITETURA_MESTRE (seções 1 a 18).

## [V1.0] — 2026 — Guia inicial
- Página única sobre risers e Pull-In. Congelada como referência histórica.
