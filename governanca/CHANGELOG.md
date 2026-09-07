# CHANGELOG.md — Plataforma Subsea Rafaela

Formato: versão · data · escopo · itens. Ordem: mais recente primeiro.

## [V4.0] — em desenvolvimento
**Escopo:** hospedagem como site estático, redesign completo da UX, pipeline de conteúdo, biblioteca visual licenciada, quiz com raciocínio, gamificação por profundidade.
**Sprint atual:** 1, 2 e 3 concluídos. Sprint 4 (capítulos 01 a 08 no novo shell, com rubrica de excelência) a iniciar.

### Sessão 6 — 07/09/2026 — Sprint 3 concluído: hubs reais, busca e exportar/importar progresso
- Os 5 hubs que eram placeholder desde o Sprint 1 (Treinamento, Busca, Biblioteca Visual, Progresso, Referências) ganharam implementação real; `hub_placeholder.html` removido por não ter mais uso.
- **Referências:** nova função em `src/build.py` extrai a seção "Aprofundamento" dos 24 `.md` (formato já consistente: item de lista com a categoria entre colchetes, o título entre colchetes e o link logo em seguida entre parênteses), agrupa por categoria e deduplica por URL citando todos os capítulos que citam a mesma fonte — 54 referências reais reunidas, nenhuma inventada.
- **Busca:** índice combinando capítulos, glossário, prompts e `aliases.json`, injetado inline como `window.SUBSEA_SEARCH_INDEX`. Resultado direto e determinístico quando a busca normalizada bate com uma alias (seção 21 do CLAUDE.md); critério de aceite do ROADMAP testado literalmente: buscar "pull in" e apertar Enter abre o capítulo 17.
- **Biblioteca Visual:** estrutura e filtro funcionando sobre `biblioteca.json` (ainda vazio por decisão, D-007); estado vazio explica que os dados reais chegam no Sprint 7, sem fingir que a função já está completa.
- **Progresso:** lista os 24 capítulos com estado real de conclusão (reaproveitando a lógica já existente de `.chapter-card`/`data-chapter-link`), resumo "X de 24" e exportar/importar progresso em JSON (B-011) — testado com round-trip completo (exportar, limpar localStorage, importar, conferir que o estado volta).
- **Treinamento:** conteúdo novo explicando os recursos da plataforma (dois modos de uso, camadas, glossário, painel PM, prompts, progresso, busca) na voz direta com a Rafaela.
- `assets/app.js` ganhou `initProgressPage()` (resumo, medidor de profundidade da página de Progresso, exportar/importar). `prompts.html` ganhou `id` por prompt-card para permitir link direto a partir da busca.
- **Bug real encontrado e corrigido durante o próprio teste:** `src/scripts/qa.py` reportava um link local quebrado em `search.html` que não existia de verdade — o checador lia `href="..."` no arquivo inteiro, inclusive dentro do `<script>` que monta HTML por concatenação de string. Corrigido removendo blocos `<script>` antes de checar links (B-041).
- `src/scripts/test_e2e.py` cresceu de 35 para 48 checagens (referências carregam, biblioteca mostra estado vazio, progresso mostra contagem, busca determinística, exportar/importar com round-trip real) — todas passando após corrigir uma corrida de tempo no próprio teste (o `reload()` do import é assíncrono, dentro do `FileReader.onload`).
- B-026 (mapeamento capítulo→fase) permanece em aberto, deliberadamente não resolvido aqui: é decisão de currículo que cabe junto da reescrita de conteúdo dos Sprints 4 a 6, não plumbing de hub.

### Sessão 5 — 07/09/2026 — Sprint 2 concluído: design system aplicado a todo o site
- DESIGN_SYSTEM_V4.md aplicado às 33 páginas de uma vez (24 capítulos + 9 hubs), não só à amostra de 3 páginas que o ROADMAP original previa — decisão D-023, possível porque a arquitetura de templates do Sprint 1 torna o custo de aplicar a tudo igual ao de aplicar a uma amostra.
- `assets/icons.js` (novo, gerado por agente em paralelo): 30+ ícones SVG inline (`window.SUBSEA_ICONS`/`SUBSEA_ICON()`), substituindo os glifos Unicode da V3 em toda a interface (B-006 concluído).
- `assets/styles.css` reescrito por completo: tokens de cor claro/escuro, tipografia, espaçamento do DESIGN_SYSTEM_V4.md seção 3; sidebar desktop + bottom tab bar mobile; popover de termo em bottom sheet no mobile; painel PM com abas; medidor de profundidade; mapa de trilha compacto (`.trail-map`).
- `assets/app.js` reescrito: ícones dinâmicos, alternância de tema (agora com botão próprio no mobile, `#themeToggleMobile`, além do desktop), abas do painel PM, medidor de profundidade, cartão "Continuar", navegação "Neste capítulo" tanto no trilho desktop quanto em bottom sheet no mobile (`#chapterSheet`).
- `src/templates/base.html`, `capitulo.html`, `home.html` reescritos para a nova estrutura (sidebar/tabbar, painel PM em abas, trilha como mapa de pontos). `src/build.py` ajustado para passar a lista de capítulos a todos os templates.
- `ARQUITETURA_MESTRE_V4.md` (novo, gerado por agente em paralelo): consolida a especificação funcional da V3 com todas as decisões de governança acumuladas, corrigindo a seção 16 duplicada e referências a V2 do documento original (B-013 concluído).
- **Bug real encontrado e corrigido durante o teste, não depois:** a Home no celular media 5219px de altura (~6 telas) na primeira versão do protótipo, violando o próprio checklist de aprovação (DESIGN_SYSTEM_V4.md seção 9, "cabe em duas telas"). Causa: a seção "Trilha" renderizava a lista completa de 24 cartões de capítulo, redundante com a Ementa. Corrigido substituindo por um mapa compacto de pontos numerados (`.trail-map`) com link para a Ementa completa, e compactando os cartões de "Hoje eu preciso..." de layout vertical para horizontal. Resultado final: 1748px, dentro do limite de 1941px (2 telas + 15% de folga). Teste `test_e2e.py` ganhou uma checagem permanente para essa medida, evitando regressão futura.
- **Dois outros gaps reais encontrados só ao revisar o próprio checklist do DESIGN_SYSTEM_V4.md**, não por reclamação externa: (1) o botão de tema escuro só existia na sidebar desktop, deixando o mobile sem forma de alternar tema — corrigido com `#themeToggleMobile` na barra superior; (2) o trilho "Neste capítulo" (acesso rápido ao painel PM) era desktop-only, deixando o mobile sem o "painel PM em dois toques" que o checklist exige — corrigido com bottom sheet dedicado.
- Validação final: `python3 src/scripts/qa.py` (33 páginas, zero erros bloqueantes) e `python3 src/scripts/test_e2e.py` (35/35 checagens em desktop e mobile: ícones, sidebar/tabbar por viewport, abas do painel PM, bottom sheet de 2 toques, tema escuro, altura da Home) — suíte completa rodada de novo após o ajuste final de CSS, sem regressão.
- Pendências abertas sem bloquear o Sprint: B-038 (fontes Inter/Sora não hospedadas localmente — sem acesso de rede nesta sessão para baixar; CSS já declara a família correta, cai em fallback do sistema até os arquivos existirem), B-039 (ajustes visuais que o Paulo pedir após ver o site publicado), B-026 (mapeamento capítulo→fase, que já bloqueia o nome do próximo marco no medidor de profundidade, D-024).
- **Achado do Paulo durante a revisão do protótipo, registrado à parte:** uso de inglês por inércia da fonte no conteúdo (não no design) — ver D-025 e B-040 abaixo.

### Sessão 5 — 07/09/2026 — Critério de uso de inglês reforçado (D-025)
- O Paulo revisou uma captura de tela do capítulo 17 (tabela "Sequência didática de second-end pull-in") e apontou que boa parte do inglês usado ali (ex.: "transfer load", "hydraulic power", "control philosophy", nomes de etapa inteiros em inglês) não reflete o que se fala de fato numa reunião em português na Petrobras — diferente de "pull-in", que é dito em inglês mesmo em frase em português.
- D-025 registrada: aperta o critério de D-019, invertendo o default para português; inglês só sobrevive com evidência de uso oral real (lista de exemplos em ambos os sentidos na decisão). AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 3.9 e rubrica da seção 4 atualizadas. B-040 aberto no backlog, com o m17 como primeiro capítulo a corrigir nos Sprints 4 a 6 — isso amplia o escopo de B-030/B-031, não é trabalho novo isolado.

### Sessão 4 — 07/09/2026 — Diretriz de chunking (D-022)
- A pedido do Paulo: páginas de capítulo não podem ser "gigantes" — o conteúdo precisa evoluir em partes curtas para não cansar nem assustar. Registrado D-022: a unidade de fragmentação é a camada de profundidade dentro da mesma página (nunca uma sequência obrigatória de páginas/telas), e dentro de cada camada o texto também precisa vir em sub-blocos curtos com heading próprio, não um parágrafo monolítico. Isso reconcilia o pedido com o Modo Consulta Imediata (CLAUDE.md seção 4), que exige resposta na mesma página sem navegação forçada.
- Rubrica de excelência (AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 4) e DESIGN_SYSTEM_V4.md (componente de controle de camadas) atualizados para exigir essa fragmentação como critério explícito nos Sprints 2 (componente) e 4-6 (redação).

### Sessão 3 — 07/09/2026 — Sprint 1 Parte B: fundação técnica e primeiro site real
- Trabalho paralelizado com 3 agentes em background para acelerar: extração de `assets/data.js` para `src/data/*.json` (glossário 126 termos, prompts 28, aliases 38, `biblioteca.json` vazio com schema documentado), geração de `INVENTARIO_V3.json` (33 páginas catalogadas: blocos presentes, IDs, links locais/externos, imagens), e o CSS/JS mínimo funcional (`assets/styles.css`, `assets/app.js`) a partir de um contrato de classes/atributos `data-*` que eu especifiquei. Enquanto isso, escrevi o núcleo acoplado (extrator de capítulos, templates, build.py) para não gerar retrabalho de integração entre as partes.
- `src/scripts/extrair_capitulos.py`: extrai os 24 capítulos do HTML original (usando as classes CSS semânticas reais da V3 — `.express`, `.pm-box`, `.mini-quiz`, `.quiz-option[data-choice]`, `.resources`, etc. — não heurística de texto) para `src/content/mNN.md`, com front-matter YAML e seções nomeadas, marcando com comentários `REESCREVER(...)`/`DIAGRAMA-INTERATIVO-ORIGINAL`/`IMAGEM-HOTLINK-ORIGINAL` os pontos que a auditoria da Sessão 2 já tinha identificado. Corrigidos 3 bugs de extração durante o teste (duplicação no callout PM, ordem errada no FAQ colapsável, texto grudado no cartão de foto) antes de rodar nos 24 capítulos.
- `src/build.py`: gera as 33 páginas HTML (24 capítulos + 9 hubs) a partir de `src/content/` e `src/data/`, usando Jinja2. Marca automaticamente todo termo do glossário presente no texto de cada capítulo como termo clicável — sem o teto de 18 ocorrências por página que a V3 tinha (B-035, D-019).
- `src/scripts/qa.py`: QA automatizado — links locais, IDs duplicados dentro da mesma página, blocos obrigatórios por capítulo, `<img>` externo (zero encontrado), HTML parseável, e uma checagem heurística de cobertura de glossário (167 siglas candidatas sem entrada, cataloga para B-031). Zero erros bloqueantes na primeira rodada completa.
- `src/scripts/test_e2e.py`: teste real num Chromium headless (Playwright) em desktop e mobile — 20/20 checagens passando (camadas de profundidade, quiz interativo, popover de termo, progresso persistente via localStorage, filtro do glossário, zero erro de JS, zero overflow horizontal). Esse teste encontrou e permitiu corrigir um bug real antes do commit: tabelas Markdown sem `overflow-x: auto` estourando a largura em 390px — corrigido em `assets/styles.css`.
- CI (`qa-governanca.yml`) ganhou um segundo job, `qa-tecnico`, que roda `src/build.py` e `src/scripts/qa.py` a cada push/PR agora que existe site de verdade para testar.
- Fidelidade de conteúdo verificada por contagem de palavras (m01: 952 vs. 844 palavras originais; m17: 1293 vs. 1146) — o extraído tem mais, não menos, porque preserva URLs completas e metadados de diagrama/foto que o texto achatado da V3 omitia.
- Sprint 1 (ambas as partes) concluído. Próximo: Sprint 2 (design system e protótipo), que precisa da direção visual completa de DESIGN_SYSTEM_V4.md aplicada sobre este esqueleto funcional.

### Sessão 2 — 07/09/2026 — Zip completo da V3 recebido + auditoria de conteúdo, didática e UX de aprendizagem
- GitHub Pages ativado pelo Paulo (B-029 concluído).
- Zip completo da V3 (43 arquivos: index + 8 hubs + 24 capítulos + assets/data.js, styles.css, app.js + documentação) recebido e totalmente inspecionado, incluindo leitura integral de 5 capítulos representativos e varredura estrutural dos 24 (B-028 concluído).
- A pedido do Paulo, inserida uma fase de auditoria de conteúdo/didática/UX/gamificação como Parte A do Sprint 1, antes de qualquer extração técnica (D-015). Resultado em `governanca/AUDITORIA_CONTEUDO_DIDATICA_V4.md`.
- Achados centrais: capítulos rasos demais para sustentar 4 camadas reais de profundidade (534-1202 palavras cada, sem marcação `data-layer` no HTML); campo "why" do glossário idêntico nos 126 termos; quiz do capítulo 17 ainda com distratores triviais e do capítulo 19 com pergunta binária fraca; fatos datados de contratos/casos Brasil sem data de verificação registrada. Capítulos 19 (IMR) e 22 (tecnologias emergentes) identificados como o padrão de qualidade a replicar.
- B-030 a B-034 abertos no backlog a partir da auditoria; rubrica de "excelente nível" por capítulo definida e incorporada como critério de aceite dos Sprints 4 a 6.
- D-016 a D-018 confirmadas pelo Paulo: profundidade completa nas camadas Técnica/Deep dive, verificação factual dos casos Brasil adiada para V4.1, reescrita do glossário incremental por lote de capítulos.
- A pedido do Paulo, adicionado critério editorial de uso de termos técnicos em inglês (D-019): todo termo não-trivial usado num capítulo precisa de entrada no glossário. Medição real mostrou 53 de 60 termos técnicos amostrados (nos 5 capítulos lidos por completo) sem entrada correspondente.
- Corrigido um erro da própria auditoria: o popover de termo (glossário em "balão" sobre a palavra) **existe e funciona** via `assets/app.js`, ao contrário do que a primeira leitura sugeria — mas só reconhece termos já cadastrados e trunca em 18 ocorrências clicáveis por capítulo, silenciosamente. B-035 aberto para corrigir isso no build da V4.
- Extração técnica (Parte B do Sprint 1) ainda não iniciada — inicia na próxima sessão, já informada por D-016 a D-019.
- A pedido do Paulo ("manter o repositório atualizado e bem configurado, de forma profissional e completa, e que o projeto garanta essa atualização constante"), adicionada automação real de governança (D-020): `.github/workflows/qa-governanca.yml` (CI que valida os 10 documentos de governança, links internos e exige CHANGELOG/ESTADO_ATUAL atualizados quando `src/`, `capitulos/` ou `assets/` mudam), `.github/PULL_REQUEST_TEMPLATE.md` (checklist de governança em todo PR), `.editorconfig`. CLAUDE.md ganhou a seção 0.10 documentando o mecanismo. Rodada real do CI no GitHub confirmada com sucesso (run 34072583228).
- Paulo inicialmente pediu PR obrigatório na `main`, depois reverteu ao perceber que isso exigiria clique manual dele a cada atualização — "não quero isso, quero que você cuide de tudo" (D-021). Decisão final: nenhuma trava manual no GitHub; o Claude assume sozinho o fluxo de branch, commit, PR, checagem do CI e merge. A auditoria de qualidade vira um hábito de fim de sessão, não uma trava técnica nem um agendamento à parte — cadência escolhida pelo Paulo: "a cada sessão de trabalho". GUIA_PUBLICACAO.md e CLAUDE.md seção 0.10 atualizados. B-036 fechado sem ação.
- Todo o trabalho das Sessões 1 e 2 mergeado na `main` pelo próprio Claude via PR #1 (squash merge, commit `55e29d1`), demonstrando o fluxo de D-021 na prática: branch → commit → PR → CI verde (run 34073749444) → merge, sem nenhum clique do Paulo. CI verde confirmado também no push resultante à `main` (run 34073767804). GitHub Pages já republicou a partir dessa `main`.

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
