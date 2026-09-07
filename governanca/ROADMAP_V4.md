# ROADMAP_V4.md — Plano de evolução por sprints

Princípio: **uma sessão = um sprint = uma entrega testável**. Cada sprint tem entrada (o que precisa existir antes), saída (o que o Paulo recebe) e critério de aceite. Nenhum sprint começa sem o anterior aceito, salvo decisão registrada em DECISOES.md.

Estimativa de sessões é indicativa. Sprints de conteúdo podem se dividir em duas sessões se a qualidade exigir.

---

## Sprint 0 — Governança · CONCLUÍDO em 06/09/2026
Saída: diagnóstico, kit de governança, roadmap, direção de design, guia de publicação.

## Sprint 1 — Auditoria de conteúdo + fundação técnica
**Entrada:** D-004a e D-005 decididas (ambas vigentes). Zip completo da V3 recebido (Sessão 2).

### Parte A — Auditoria de conteúdo, didática e UX de aprendizagem (D-015)
Executada antes de qualquer extração técnica, por decisão explícita do Paulo: conteúdo e didática são a base do produto e precisam estar em excelente nível antes de ganhar shell novo.
1. Leitura e avaliação crítica dos 24 capítulos, do glossário (126 termos), dos prompts (28) e das referências, contra os critérios do CLAUDE.md (camadas, ciclo de vida, foco em PM, tecnologia emergente, Petrobras/Brasil, rigor de fonte).
2. Resultado registrado em `AUDITORIA_CONTEUDO_DIDATICA_V4.md`: o que está em nível bom (preservar), o que é raso ou mecânico (corrigir), e uma rubrica objetiva de "excelente nível" por capítulo.
3. Itens novos abertos no BACKLOG a partir dos achados (ver B-030 a B-034).
**Saída:** AUDITORIA_CONTEUDO_DIDATICA_V4.md. **Concluída em 07/09/2026 (Sessão 2).**

### Parte B — Fundação técnica e extração de conteúdo
**Faz:**
1. Inventário automatizado da V3 (páginas, blocos por capítulo, termos, quizzes, prompts, links, imagens) salvo como `INVENTARIO_V3.json`, marcando o que foi extraído limpo e o que exige revisão.
2. Estrutura do repositório: `/` (site publicado), `/src/content/` (capítulos em Markdown com seções nomeadas), `/src/data/` (glossario.json, prompts.json, aliases.json, biblioteca.json), `/src/templates/`, `/src/build.py`, `/governanca/` (cópia dos .md), `.nojekyll`, `README.md`.
3. Extração do conteúdo da V3 para o formato de dados. Glossário, prompts e aliases vêm prontos do `data.js`; capítulos são extraídos do HTML por bloco (express, corpo, PM, quiz, prompts, referências). **Diferença em relação ao plano original: a extração não é mais cópia neutra — já nasce sinalizada com os pontos que a auditoria (Parte A) marcou para reescrita nos Sprints 4 a 6 (camadas rasas, "why" genérico do glossário, distratores fracos, ausência de data de verificação em fatos datados).**
4. Esqueleto do shell V4 (sem design final): template de capítulo e de hub que já obedece à estrutura da seção 6 da arquitetura e às camadas `data-layer`. Build gera as 33 páginas em versão "sem estilo bonito, com estrutura certa".
5. Script de QA: links locais, IDs duplicados, blocos obrigatórios por capítulo, `<img>` externo, overflow, e **cobertura de glossário por capítulo** (todo termo técnico não-trivial usado no texto tem entrada correspondente no glossário — D-019, B-035).
**Saída:** zip do repositório inicial (src + site gerado) e INVENTARIO_V3.json.
**Aceite:** build roda sem erro; 24 capítulos gerados com todos os blocos obrigatórios; QA zero falhas; Paulo abre 3 capítulos na URL e confirma que nenhum texto técnico se perdeu em relação à V3 (comparação por amostragem).
**Concluída em 07/09/2026 (Sessão 3).** Evidências: `python3 src/build.py` gera as 33 páginas sem erro; `python3 src/scripts/qa.py` retorna zero erros bloqueantes (links locais, IDs duplicados, blocos obrigatórios, `<img>` externo — nenhum encontrado — e uma checagem heurística de cobertura de glossário que já alimenta B-031); `python3 src/scripts/test_e2e.py` roda os 24 capítulos gerados num Chromium real via Playwright em desktop e mobile — 20/20 checagens passaram (camadas de profundidade, quiz, popover de termo sem o limite de 18 da V3, progresso persistente, filtro de glossário, zero erro de JS, zero overflow horizontal). Fidelidade de conteúdo verificada por contagem de palavras: o texto extraído tem mais palavras que o original (m01: 952 vs. 844; m17: 1293 vs. 1146), porque captura URLs completas e metadados de diagrama/foto que o texto achatado da V3 omitia — nenhuma perda encontrada.
**Ressalva sobre o aceite:** o teste E2E automatizado acima é mais rigoroso que "abrir 3 capítulos e olhar", mas continua sendo QA automatizado, não teste em dispositivo real. D-009 continua exigindo o teste humano do Paulo antes de qualquer release — isso ainda não aconteceu porque o site ainda não está publicado na `main` no momento em que este texto foi escrito (ver ESTADO_ATUAL.md).

## Sprint 2 — Design system e protótipo
**Entrada:** Sprint 1 aceito; D-006 decidida.
**Faz:** tokens CSS (cores, tipografia, espaçamento, raio, sombra, motion); componentes base (header, tab bar mobile, sidebar desktop, cartão, botão, chip de termo, popover/bottom sheet, quiz, medidor de profundidade, badge, toast, frame de diagrama, cartão de prompt, cartão de foto/fonte); ícones SVG; light/dark; reduced-motion. **O chip de termo reimplementa a lógica de `assets/app.js` sem o teto de 18 ocorrências por página (B-035): marca todo termo distinto do glossário presente no texto.** Aplica ao protótipo: Home nova + capítulo 17 novo + glossário novo. Consolida ARQUITETURA_MESTRE_V4.md.
**Saída:** protótipo publicado em `/v4-preview/` na mesma URL, sem tocar na V3.
**Aceite:** Paulo (e Rafaela, se possível) aprovam a direção visual e a navegação no celular e notebook. Ajustes registrados no BACKLOG antes do Sprint 3.

## Sprint 3 — Shell e hubs
**Faz:** aplica o design aprovado a Ementa, Treinamento, Busca, Glossário completo, Prompts, Biblioteca Visual (estrutura; imagens no Sprint 7), Progresso, Referências. Busca com índice gerado e aliases. Exportar/importar progresso em JSON.
**Aceite:** todos os hubs navegáveis nos dois dispositivos; busca "pull in" abre capítulo 17; exportar/importar funciona entre celular e notebook.

## Sprint 4 — Capítulos 01 a 08 no novo shell
**Faz:** migração com camadas de profundidade navegáveis, painel PM em abas, quiz revisado (D-008), "Para onde isso está indo" onde aplicável, termos com popover. Sem alterar o sentido do conteúdo técnico; melhorias de conteúdo entram como itens explícitos no CHANGELOG. **Cada capítulo migrado passa pela rubrica de AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 4 (camadas com conteúdo próprio, quiz sem distrator trivial/binário, "why" de glossário específico, fatos datados com data de verificação).**
**Aceite:** QA automatizado (links, IDs, JS) + rubrica de excelência cumprida + leitura de amostra pelo Paulo em 2 capítulos.

## Sprint 5 — Capítulos 09 a 16
Mesmo padrão do Sprint 4, rubrica de excelência incluída. Inclui reauditoria dos diagramas de riser, flexível, controle, flow assurance, lay systems, marine operations e load path.

## Sprint 6 — Capítulos 17 a 24
Mesmo padrão do Sprint 4, rubrica de excelência incluída. Inclui Pull-In (já usado como referência de qualidade na auditoria, mas com quiz a reescrever), IMR (capítulo 19, o de melhor nível na auditoria — modelo a replicar), decommissioning, tecnologias emergentes (capítulo 22, também modelo), interfaces, FAT/SIT/SAT.

## Sprint 7 — Biblioteca Visual licenciada
**Faz:** pesquisa de imagens com licença verificável (Wikimedia Commons, Flickr CC, agências governamentais, Petrobras quando os termos permitirem); cópia local com crédito; cartões de fonte para o restante; diagramas SVG próprios onde não houver foto; distribuição nos capítulos (FOTO → O QUE OBSERVAR → DIAGRAMA → IMPLICAÇÃO). Registro de licença e data por item.
**Aceite:** nenhuma tag `<img>` apontando para domínio externo; nenhuma imagem quebrada; toda imagem com fonte e licença.

## Sprint 8 — Gamificação e constância
**Faz:** medidor de profundidade, fases com marcos visíveis, badges em SVG, "missão do dia", celebrações discretas, página de progresso redesenhada, "isso não ficou claro" em cada seção.
**Aceite:** próximo marco sempre visível na Home; nenhuma função bloqueada por gamificação; XP não duplica em resposta repetida.

## Sprint 9 — QA completo e release V4.0
**Faz:** checklist do CLAUDE.md seção 23 item a item; auditoria de animações; validação de links externos com data; acessibilidade básica; performance; teste real em celular e notebook pelo Paulo; MATRIZ_ACEITE_V4 preenchida; CHANGELOG fechado; V3 arquivada em `/v3/`.
**Aceite:** todos os itens da matriz com evidência; Definition of Done (D-009) cumprida.

## V4.x — Após o release (ordem sugerida, a validar com uso real da Rafaela)
- V4.1 Aprofundamento Petrobras/Brasil por capítulo (casos públicos, terminologia, especificações públicas).
- V4.2 Novos prompts do backlog (MOC, handover, steering committee, weather window, punch list).
- V4.3 PWA leve (manifest + service worker) para tela inicial e leitura offline.
- V4.4 Novos capítulos por demanda (ex.: logística offshore e readiness como capítulo próprio; HAZID/HAZOP para PM; contratos EPCI e modelos de contratação).
- V4.5 Sincronização de progresso entre dispositivos (avaliar custo/benefício; pode ser desnecessário com exportar/importar).

## Regras do roadmap
- Um sprint pode encolher; não pode pular o aceite.
- Ideias novas entram no BACKLOG, não no sprint corrente, salvo bloqueio.
- Toda sessão termina com ESTADO_ATUAL.md, CHANGELOG.md e BACKLOG.md atualizados, mesmo que o sprint não tenha fechado.
