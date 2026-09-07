# ARQUITETURA_MESTRE_V4.md — Especificação funcional e de conteúdo vigente

**Nota de precedência.** Este documento consolida e substitui `ARQUITETURA_MESTRE_V3.md` como especificação funcional e de conteúdo vigente da Plataforma Subsea Rafaela. Ele descreve o estado atual do produto e a direção acordada para completá-lo — não é a fonte primária de requisitos. Em qualquer divergência futura entre este documento e `CLAUDE.md` (seções 1 a 30) ou `DECISOES.md`, prevalecem o CLAUDE.md e as decisões registradas (D-013). Este documento é revisado sempre que uma decisão nova o afetar; ele não cria requisito novo por si — apenas organiza o que já foi decidido e o que já existe.

A V3 e sua documentação seguem como insumo histórico (D-013): o conteúdo técnico dos 24 capítulos, os 126 termos de glossário, os 28 prompts e os enunciados de quiz vieram dela e continuam sendo aproveitados por padrão. O shell, o CSS, o JS e a arquitetura de página única/multipágina antiga da V3 foram descartados.

---

## 1. Objetivo do produto e público

A Plataforma Subsea Rafaela é uma plataforma de aprendizagem e apoio ao trabalho diário para a Rafaela, engenheira de produção que atua como gerente de projetos em projetos offshore de instalação, manutenção/intervenção e desinstalação/decommissioning de sistemas e equipamentos submarinos (CLAUDE.md seção 1).

A plataforma cumpre seis funções simultâneas: curso estruturado de engenharia submarina aplicada à gestão de projetos; referência técnica para consulta imediata; ferramenta de apoio ao trabalho diário (checklists, perguntas, análise documental); biblioteca visual de equipamentos e operações; biblioteca de prompts profissionais para uso de LLMs; ambiente de aprendizagem gamificado.

O objetivo não é formar uma projetista especialista em cada disciplina. É desenvolver alfabetização técnica profunda o suficiente para que uma gerente de projetos compreenda sistemas, interfaces, riscos, documentação e operações, e consiga formular perguntas tecnicamente relevantes e tomar decisões de gestão com mais qualidade. O texto fala diretamente com a Rafaela ("você"), assume domínio de gestão de projetos e não assume formação prévia em engenharia submarina.

## 2. Modos de uso e escopo técnico

A plataforma suporta sempre dois modos simultâneos, sem que um bloqueie o outro:

- **Modo Formação:** aprendizado sequencial e progressivo, com trilha, quizzes, fases e evolução acompanhada.
- **Modo Consulta Imediata:** acesso direto a qualquer capítulo, sem pré-requisito de conclusão. Se a Rafaela precisa entender Pull-in hoje, ela abre o capítulo 17 e começa ali. A gamificação nunca bloqueia conteúdo.

O escopo técnico cobre, entre outros: desenvolvimento de campo e arquitetura submarina; poço e interfaces com wellhead/árvore de natal molhada; manifolds, PLET/PLEM, jumpers; SURF; pipelines e flowlines rígidos; risers rígidos, flexíveis e híbridos; umbilicais e subsea controls; flow assurance; materiais, corrosão e proteção catódica; geotecnia e route engineering; unidades flutuantes, mooring e DP; embarcações de instalação; ROV, survey e metrologia; lifting, rigging e load path; installation engineering e marine operations; pull-in/pull-out; comissionamento e start-up; IMR; desinstalação e decommissioning; gestão de interfaces técnicas; documentação de engenharia (VDRL/MDR); FAT/EFAT/SIT/SAT; tecnologias emergentes. O escopo evolui quando novos assuntos relevantes forem identificados; a lista completa e o critério de priorização de fontes (Petrobras e ecossistema brasileiro, normas, academia, fornecedores) estão em CLAUDE.md seções 5, 8 e 9.

## 3. Arquitetura de informação

O produto é um site multipágina responsivo — nunca uma página única contínua (D-001). Cada tipo de página tem caminho próprio na raiz do site publicado:

| Página/hub | Caminho |
|---|---|
| Home | `index.html` |
| Ementa (lista dos 24 capítulos) | `ementa.html` |
| Treinamento (trilha/fases) | `treinamento.html` |
| Glossário | `glossario.html` |
| Biblioteca de Prompts | `prompts.html` |
| Biblioteca Visual | `biblioteca.html` |
| Mapa de Progresso | `progresso.html` |
| Referências | `referencias.html` |
| Busca | `search.html` |
| Capítulo N (24 no total) | `capitulos/mNN.html`, `NN` de 01 a 24 |

Os 24 capítulos, na ordem da ementa atual:

1. Mapa mental da engenharia submarina
2. Desenvolvimento de campo e arquitetura submarina
3. Ambiente marinho, metocean e movimentos
4. Unidades flutuantes, amarração e posicionamento dinâmico
5. Poço submarino, wellhead e árvore de natal
6. Manifolds, jumpers e estruturas submarinas
7. SURF: flowlines, risers e umbilicals
8. Pipelines e flowlines rígidos
9. Risers: configurações, cargas e fadiga
10. Riser flexível: construção, acessórios e integridade
11. Umbilicals e sistemas de controle
12. Flow assurance
13. Materiais, corrosão e proteção
14. Geotecnia submarina, rota e fundações
15. Embarcações, lay systems, ROV e survey
16. Engenharia de instalação e operações marítimas
17. Pull-in de risers: sistema, sequência e interfaces
18. Pré-comissionamento, commissioning e start-up
19. IMR, manutenção, intervenção, reparo e life-of-field
20. Risco, confiabilidade e governança técnica do projeto
21. Desinstalação e descomissionamento de sistemas submarinos
22. Tecnologias emergentes e rumo da engenharia submarina
23. Gestão de interfaces técnicas, documentos e configuração
24. FAT, EFAT, SIT, SAT e readiness de integração

Essa ordem e a divisão em fases de gamificação (seção 13) seguem em aberto para reavaliação no Sprint 2, por decisão registrada em D-013 — o número e o conteúdo dos capítulos podem mudar antes do rollout completo do shell V4.

Cada capítulo tem navegação Anterior/Próximo, indicação de posição no curso, acesso direto por URL e nenhum bloqueio por gamificação. A Home oferece "continuar de onde parou".

## 4. Arquitetura técnica: pipeline conteúdo-como-dados

A plataforma é publicada como site estático (HTML/CSS/JS) via GitHub Pages, em repositório público (D-004, D-004a). Isso já está em produção como decisão, não como plano.

O conteúdo é gerado por um pipeline "conteúdo como dados, shell como código" (D-005), hoje implementado e funcional:

```
src/content/*.md   (24 capítulos, Markdown com seções nomeadas + front-matter YAML)
src/data/*.json    (glossario.json, prompts.json, aliases.json, biblioteca.json)
        │
        ▼
src/templates/*.html   (templates Jinja2: base, capitulo, home, hub_lista_capitulos,
                         hub_placeholder, glossario, prompts)
        │
        ▼
src/build.py   (lê content + data + templates, gera o HTML final)
        │
        ▼
index.html, ementa.html, treinamento.html, glossario.html, prompts.html,
biblioteca.html, progresso.html, referencias.html, search.html,
capitulos/m01.html ... capitulos/m24.html    (site publicado, na raiz do repositório)
```

Regra operacional (CLAUDE.md 0.4 item 3): nunca editar à mão o HTML gerado. Toda mudança de conteúdo ou shell é feita em `src/content`, `src/data` ou `src/templates`, seguida de `python3 src/build.py`.

Scripts de apoio em `src/scripts/`: `extrair_capitulos.py` (extraiu os capítulos da V3 para Markdown), `qa.py` (QA automatizado: links locais, IDs duplicados, blocos obrigatórios por capítulo, `<img>` externo, cobertura de glossário), `test_e2e.py` (Playwright/Chromium, roda manualmente por sessão — fora do CI por custo, ver B-037), `gerar_inventario.py` (produziu `INVENTARIO_V3.json`).

O front-matter YAML de cada `mNN.md` traz `id`, `n` (posição no curso), `level` (fase/dificuldade), `title`, `subtitle`. Comentários HTML `<!-- REESCREVER(...) -->`, `<!-- DIAGRAMA-INTERATIVO-ORIGINAL -->` e `<!-- IMAGEM-HOTLINK-ORIGINAL -->` marcam, dentro do Markdown, o que os Sprints 4 a 6 ainda precisam reescrever ou recriar; são removidos no build e não aparecem no site publicado.

Estado de implementação: pipeline completo e testado (Sprint 1 concluído — ver seção 20). Os 24 capítulos já são gerados; o conteúdo dentro deles ainda é, em grande parte, o texto da V3 sinalizado para reescrita, não o texto final de excelência (ver seção 16).

## 5. Estrutura de um capítulo e camadas de profundidade

Cada capítulo em `src/content/mNN.md` tem hoje estas seções, nesta ordem:

1. **Express** — candidata à camada "5 minutos". Resumo rápido e pré-requisitos condensados para quem chegou direto ao tema.
2. **Corpo técnico** — hoje serve, num único bloco, às camadas "Gerente de Projetos" e "Técnica". É o principal ponto de reescrita dos Sprints 4-6 (ver abaixo).
3. **Painel PM** — três sub-blocos: Pontos de atenção, Perguntas que você deve fazer, Documentos que você encontrará no projeto.
4. **Red flags** — sinais de alerta específicos e acionáveis, não genéricos.
5. **Assistente LLM** — bloco recolhível com prompts de aprofundamento (ver seção 10).
6. **Mini quiz** — 3 a 6 questões com feedback (ver seção 12).
7. **Aprofundamento** — candidata à camada "Deep dive": normas, papers, casos reais, vídeos.

Essa estrutura de seções do arquivo-fonte não é a mesma coisa que as quatro camadas de profundidade que a interface mostra à Rafaela. As camadas (CLAUDE.md seção 12; DESIGN_SYSTEM_V4.md seção 5) são um filtro de visibilidade sobre o conteúdo, controlado por um componente segmentado (5 min · Gerente · Técnica · Deep dive) que não navega para outra página — apenas mostra ou esconde blocos marcados com `data-layer` dentro da mesma página de capítulo (D-022). "Ver tudo" fica sempre disponível.

Dois princípios de chunking regem essa relação (D-016, D-022), e ambos corrigem um problema real identificado na auditoria de conteúdo (seção 16 adiante): na V3, "Corpo técnico" era um texto corrido único sem marcação de camada, incapaz de sustentar profundidade real em "Técnica" e "Deep dive" como blocos autônomos.

1. **Camada como unidade de fragmentação entre profundidades.** Cada camada precisa de conteúdo próprio e completo, não um resumo com um parágrafo a mais em relação à anterior: 5 minutos (~150 palavras), Gerente (~300), Técnica (~400), Deep dive (referências + caso aplicado). O chunking nunca deve virar uma sequência obrigatória de páginas ou telas tipo carrossel/wizard — isso quebraria o Modo Consulta Imediata (seção 2), que exige que a Rafaela chegue direto ao que precisa numa reunião.
2. **Sub-blocos dentro da mesma camada.** Dentro de cada camada, o texto é fragmentado em parágrafos curtos (até ~80 palavras) e sub-blocos com heading próprio — nunca um bloco monolítico de 300-400 palavras num parágrafo só. O componente de camada do design system precisa suportar e espaçar visualmente vários sub-blocos, não um único texto corrido.

Essa reescrita capítulo a capítulo acontece nos Sprints 4 a 6 e é avaliada pela rubrica de excelência descrita na seção 16.

## 6. Modelo de dados

Quatro arquivos JSON em `src/data/` guardam o conteúdo estruturado da plataforma, já existentes e em uso pelo build.

**`glossario.json`** — array com os 126 termos herdados da V3. Cada item: `term` (termo), `full` (forma estendida), `definition` (definição), `why` (por que importa para o projeto), `id`, `category`. Ordenado alfabeticamente por `term`. Estado: estrutura completa, mas o campo `why` é hoje o mesmo texto genérico repetido nos 126 termos — reescrita individualizada é trabalho incremental dos Sprints 4-6 (D-018), junto com o fechamento da cobertura de termos técnicos por capítulo (seção 7).

**`prompts.json`** — array com os 28 prompts profissionais. Cada item: `title`, `category`, `text` (prompt completo, já com estrutura "para que serve" + campos `[PREENCHA]`), `href`. Ordem original da V3 mantida.

**`aliases.json`** — objeto (string → string) mapeando sinônimos e grafias alternativas de busca ao id do capítulo correspondente (ex.: `"pullin"`, `"pull-in"`, `"guincho"`, `"winch"` → `"m17"`). Alimenta a busca (seção 8).

**`biblioteca.json`** — array **vazio** por decisão de projeto, não por pendência técnica. Não existia na V3 (as imagens de lá eram hotlinks quebrados, ver D-007). Fica vazio até o Sprint 7, quando imagens licenciadas forem incorporadas. Schema já definido para quando for populado:

```json
{
  "id": "string",
  "titulo": "string",
  "categoria": "string",
  "capitulo_relacionado": "string",
  "tipo": "foto | cartao_fonte | diagrama_svg",
  "arquivo_local": "string ou null",
  "fonte_nome": "string",
  "fonte_url": "string",
  "licenca": "string",
  "data_verificacao": "string",
  "o_que_observar": "string",
  "por_que_importa": "string"
}
```

## 7. Glossário contextual

Além da página geral pesquisável (`glossario.html`, com filtro por categoria e sinônimos), termos técnicos no corpo de um capítulo são interativos: desktop usa hover/clique para abrir popover, mobile usa toque para abrir popover ou bottom sheet. O popover mostra termo completo, definição curta, "por que isso importa" e link "ver no glossário"; ao voltar do glossário, a Rafaela retorna ao ponto exato de onde saiu.

Dois pontos em que este documento segue D-019/D-022 da auditoria de conteúdo em vez do texto original da V3:

- **Sem teto de ocorrências por capítulo.** A V3 limitava a 18 o número de termos marcados como clicáveis por página, o que deixava termos cadastrados sem popover em capítulos densos (m17, m19, m21). O build da V4 remove esse teto: todo termo distinto presente no glossário é marcado, não apenas os 18 primeiros.
- **Cobertura obrigatória de glossário.** Todo termo técnico não trivial (sigla ou termo em inglês fora do vocabulário comum do dia a dia) usado no corpo de um capítulo precisa ter entrada correspondente no glossário antes de esse capítulo ser considerado migrado/aceito. Mantém-se o termo em inglês quando é o padrão de contratos/normas/reuniões do setor (ex.: "bend stiffener", "as-built"); traduz-se quando há equivalente natural e corrente (ex.: "poço"). O script de QA do build checa essa cobertura por capítulo.

Estado de implementação: o mecanismo de popover em si (`TreeWalker` sobre o texto, casamento contra os termos do glossário, popover com retorno ao ponto exato via `sessionStorage`) já existia e funcionava na V3; a correção do teto de 18 e a checagem de cobertura de glossário fazem parte da extração para o shell V4 (Sprint 1B/2).

## 8. Busca e aliases

A busca cobre capítulos, subtópicos, termos do glossário, prompts, recursos visuais, equipamentos e operações. Aliases explícitos cobrem terminologia provável — por exemplo, "pull-in" é encontrado por "pull in", "pull-in", "pullin", "winch", "guincho", conforme `src/data/aliases.json`. A busca por termos determinísticos (nome de capítulo ou sigla exata) deve ser confiável mesmo sem correspondência difusa.

## 9. Biblioteca de prompts profissionais

Página própria (`prompts.html`) com os 28 prompts parametrizáveis e copiáveis, organizados em categorias: reuniões e fornecedores; documentos e engenharia; contratos e comercial; planejamento e risco; execução offshore; IMR e decommissioning; comunicação executiva. Cada prompt tem título, "para que serve", "quando usar", termos importantes, campos `[PREENCHA]` destacados e prompt pronto para copiar (botão copiar com confirmação em toast, conforme DESIGN_SYSTEM_V4.md). Novos prompts do backlog (MOC, handover, steering committee, weather window, punch list) entram em V4.2 (ver ROADMAP_V4.md).

## 10. Assistente de aprofundamento com LLM por capítulo

Todo capítulo tem um bloco recolhível "Aprofunde este tema com uma LLM", com no mínimo três modos: dúvida rápida, aprofundamento estruturado e, quando relevante, análise de documento/reunião. Cada prompt padrão informa que a usuária é a Rafaela, engenheira de produção e gerente de projetos offshore, atuando em projetos de instalação/manutenção/intervenção/retirada em contexto Petrobras e ecossistema brasileiro; pede distinção entre fato, hipótese e requisito específico de projeto; pede explicação de siglas; pede perguntas inteligentes para especialistas; e traz um campo inequívoco "MINHA DÚVIDA / O QUE QUERO APROFUNDAR: [PREENCHA AQUI]". Termos potencialmente desconhecidos no prompt são explicados antes dele.

## 11. Biblioteca visual

Área própria (`biblioteca.html`) para consulta de imagens e diagramas por tema, equipamento, sistema, operação, empresa ou tecnologia. Cada item visual traz o que aparece, o que observar, por que é importante e o capítulo relacionado. Fotografias também aparecem distribuídas nos capítulos, não só na biblioteca isolada, seguindo a sequência foto real → o que observar → diagrama didático → implicação para o projeto.

Regra de proveniência de imagem (D-007), que substitui a prática da V3 de usar hotlinks de fornecedor (grande parte deles quebrados por bloqueio de referrer/CORS, sem direito de uso configurado):

1. imagem com licença aberta verificada é copiada para `assets/img/` com crédito e link da fonte;
2. imagem oficial sem licença aberta vira "cartão de fonte" (título, legenda, o que observar, link), sem tag `<img>`;
3. onde não existe imagem licenciável, diagrama didático próprio em SVG.

Diagramas são instrumentos de ensino, não decoração: uma animação só permanece se ensinar direção de fluxo/sinal/carga, sequência de estados, transferência de responsabilidade/carga, comparação de configuração ou feedback/causa-efeito (D-002). Diagramas fora da viewport pausam animação; `prefers-reduced-motion` é respeitado; cada diagrama interativo explica por que a interação existe e o que ela não representa.

Estado de implementação: `biblioteca.json` está vazio de propósito (seção 6) e o schema de item está definido, mas nenhuma imagem foi licenciada e incorporada ainda — isso é trabalho do Sprint 7. Os capítulos hoje têm, no lugar das fotos hotlinkadas da V3, marcações internas (`IMAGEM-HOTLINK-ORIGINAL`) indicando o que precisa virar cartão de fonte ou imagem local. Os diagramas SVG+JS interativos da V3 também não foram recriados ainda; estão marcados (`DIAGRAMA-INTERATIVO-ORIGINAL`) com título, motivo pedagógico e etapas preservados, para recriação como componente de diagrama do design system nos Sprints 2/3.

## 12. Quizzes e feedback

Cada capítulo termina com 3 a 6 questões, testando compreensão conceitual, aplicação e raciocínio de projeto — nunca apenas memorização. Pelo menos uma questão por capítulo é situacional ("o que você faria como PM?"). Ao errar, o quiz explica por que a opção está errada e reforça o conceito certo; ao acertar, reforça a lógica correta. XP não é concedido repetidamente pela mesma resposta correta.

Critério de aceite de qualidade (D-008): cada distrator precisa representar uma concepção equivocada plausível, com feedback específico por opção — não um distrator óbvio ("Nada", "Somente pintura do winch") nem uma questão binária Sim/Não. As 72 questões herdadas da V3 têm qualidade desigual (a auditoria de conteúdo, seção 16, documenta os casos concretos) e são revisadas durante a migração de capítulos, Sprints 4 a 6.

## 13. Gamificação

A gamificação existe para motivar, nunca para bloquear ou infantilizar. Elementos: XP, níveis/fases, mapa de estudo visual (medidor de profundidade), percentual por trilha, badges por marcos, streak sem induzir comportamento compulsivo, celebrações discretas ao concluir capítulo/fase, progresso salvo localmente com opção de exportar/importar em JSON. Nenhum conteúdo fica bloqueado por progresso insuficiente.

Fases sugeridas (herdadas da V3, reabertas para reavaliação no Sprint 2 junto com a ordem dos 24 capítulos, D-013): Exploradora Subsea (fundamentos), Integradora de Sistemas (SPS/SURF), Gestora de Operações (vessels/ROV/installation), Especialista de Interfaces (pull-in/commissioning), Guardião de Integridade (IMR/decommissioning), PM Subsea 360° (conclusão integrada).

Estado de implementação: medidor de profundidade, badges em SVG, "missão do dia" e página de progresso redesenhada são entrega do Sprint 8 (ver seção 20). A V3 tinha uma versão funcional destes elementos, hoje descartada junto com o resto do shell (D-013).

## 14. Tecnologias emergentes

Todo tema deve avaliar se existe tecnologia emergente modificando-o. Quando existir, o capítulo traz um bloco "Para onde isso está indo" com: tecnologia tradicional, tecnologia emergente, problema que pretende resolver, vantagens, limitações, nível de maturidade, exemplos reais, utilização no Brasil se houver, impacto potencial. Classificação obrigatória de maturidade: Comercial consolidada, Comercial em expansão, Qualificação/field trial, Emergente/P&D. Tecnologia experimental nunca é apresentada como solução consolidada.

Exemplos de escopo: all-electric subsea systems, subsea electrification, boosting/compression/separation, operação autônoma/remota, resident ROV/AUV, digital twins, machine vision para inspeção, TCP (thermoplastic composite pipe), novos materiais anti-SCC-CO2, comunicação subsea sem fio/óptica, captura de carbono e reuso de infraestrutura offshore.

Estado de implementação: hoje esse bloco existe de forma completa só no capítulo 22 (o modelo a replicar, com casos brasileiros nomeados — OneSubsea em Búzios, Strohm/Petrobras, FlatFish/Petrobras). Estendê-lo a todo capítulo onde a tecnologia emergente for relevante (estimativa de 10 a 12 dos 24, por natureza do tema) é parte da rubrica de excelência da seção 16 e acontece nos Sprints 4 a 6.

## 15. Fontes, contexto Petrobras/Brasil e citação

Recursos públicos, terminologia, casos e práticas da Petrobras têm prioridade editorial quando tecnicamente adequados, sem tratar a Petrobras como sistema isolado: a engenharia submarina é executada por um ecossistema de operadores, EPCIs, fabricantes e fornecedores (TechnipFMC, OneSubsea/SLB, Baker Hughes, Subsea7, Saipem, MODEC, NOV, Oceaneering, DOF, Aker Solutions, Oil States, Remazel, Strohm, entre outros conforme aderência). A validação usa camadas de prioridade: Petrobras e fontes brasileiras públicas; normas e recommended practices (DNV, API, ISO, IMCA, IOGP); academia; ecossistema industrial atuante no Brasil.

Toda citação diferencia claramente requisito normativo, requisito corporativo, material acadêmico, case de fornecedor, material comercial, tecnologia emergente e interpretação didática. Material comercial de fornecedor nunca vira requisito técnico universal; valores de um projeto específico nunca são apresentados como regra universal.

Verificação factual: links inseridos são verificados antes de publicação; links quebrados, privados ou excessivamente genéricos são substituídos. Fatos datados e nomeados (contratos, valores, casos de empresa) devem levar uma data de verificação ao lado — isso é regra editorial corrente, mas sua aplicação retroativa aos casos Brasil já citados nos capítulos (contratos DOF, Oceaneering, trial Strohm/Petrobras, FATs FlatFish/Petrobras, contrato OneSubsea em Búzios) foi explicitamente adiada para V4.1, depois do release da V4.0, por decisão de priorização (D-017) — não bloqueia os sprints correntes.

## 16. Critério de qualidade de conteúdo

O critério objetivo de "excelente nível" por capítulo está detalhado em `AUDITORIA_CONTEUDO_DIDATICA_V4.md` seção 4; este documento resume a rubrica sem repeti-la por inteiro.

| Critério | Insuficiente (V3, herdado) | Excelente (padrão V4) |
|---|---|---|
| Camadas | Texto corrido único sem marcação | 4 blocos com conteúdo próprio (5 min ≈150 palavras, Gerente ≈300, Técnica ≈400, Deep dive com referências + caso aplicado) |
| Fragmentação dentro da camada | Bloco monolítico de 300-400 palavras | Sub-blocos curtos com heading próprio, nunca parede de texto (D-022) |
| Quiz | Distratores às vezes triviais/binários | 3-4 perguntas, distratores como concepção equivocada plausível, feedback por opção (D-008) |
| Glossário do capítulo | "Why" genérico repetido | "Why" específico ao papel do termo naquele capítulo/projeto |
| Fatos datados/Brasil | Sem data de verificação | "Verificado em [data]" junto a todo contrato/valor/caso nomeado (V4.1, D-017) |
| Tecnologia emergente | Só no capítulo 22 | Bloco "Para onde isso está indo" em todo capítulo onde for relevante |

A auditoria completa (achados por dimensão, medição de cobertura de glossário, exemplos concretos de distrator fraco) está em `AUDITORIA_CONTEUDO_DIDATICA_V4.md`. Essa rubrica é critério de aceite formal dos Sprints 4 a 6, além do QA técnico automatizado.

## 17. Direção de design

A direção visual e de componentes está descrita por inteiro em `DESIGN_SYSTEM_V4.md`; este documento não a duplica, apenas resume o essencial. Conceito: "descer com segurança" — a Rafaela aprende descendo do litoral para águas ultraprofundas, metáfora que organiza gamificação e progresso sem virar cenário infantil. Três princípios guiam toda decisão de tela: clareza (uma coisa por vez), profundidade (camadas que ela escolhe) e impulso (sempre um próximo passo visível).

Tokens (cor, tipografia Inter+Sora, espaçamento, ícones SVG próprios sem emoji em interface), layout (bottom tab bar de cinco abas no mobile, sidebar + trilho de contexto no desktop) e o catálogo de componentes (cartão Express, controle de camadas, painel PM em abas, chip de termo, frame de diagrama, quiz, medidor de profundidade, badge, cartão de prompt) estão detalhados naquele documento, aprovado como direção (D-006) e pendente de validação por protótipo navegável no Sprint 2.

## 18. Usabilidade, acessibilidade e resiliência

A plataforma é responsiva em desktop, tablet e celular — a experiência mobile é requisito funcional, não adaptação secundária. Requisitos: navegação por teclado com foco visível; ARIA onde necessário; contraste AA; modo claro (padrão) e escuro; `prefers-reduced-motion` respeitado; busca tolerante a acentos e sinônimos; links internos estáveis e links externos em nova aba; histórico/back correto ao voltar do glossário ou de uma seção contextual; nenhuma animação que prejudique leitura; carregamento progressivo de mídia; fallback quando um recurso externo estiver indisponível. O texto principal, quizzes, glossário, progresso e diagramas essenciais funcionam mesmo sem conexão, sempre que possível, já que fontes ficam com cópia local em `assets/fonts/` e nenhuma imagem depende de hotlink externo (D-007).

## 19. Controle de qualidade e gestão de mudanças

Nenhuma versão é considerada concluída apenas porque "o recurso existe" — cada requisito é verificado funcionalmente antes do release. QA mínimo por sprint: links locais, IDs duplicados, sintaxe JS, overflow em 360px e 1440px, blocos obrigatórios de capítulo, ausência de `<img>` para domínio externo, cobertura de glossário. Isso roda automatizado (`src/scripts/qa.py`, `test_e2e.py` via Playwright) e também no CI a cada push/PR (`.github/workflows/qa-governanca.yml`, D-020, D-021). A Definition of Done de qualquer release exige, além disso, teste do Paulo na URL publicada em celular real e em notebook (D-009) — QA de viewport em navegador não substitui esse teste.

Mudanças arquiteturais relevantes vão para `DECISOES.md`; mudanças entre releases vão para `CHANGELOG.md`; pendências não implementadas de imediato vão para `BACKLOG.md`. O princípio geral é "adicionar ou melhorar sem regredir": a regra de não regressão da V3 para a V4 vale para conteúdo e função, não para forma — o shell antigo pode ser descartado livremente (D-013).

## 20. Estado atual de implementação por sprint

Detalhamento completo de entrada/saída/critério de aceite de cada sprint está em `ROADMAP_V4.md`; aqui vai o resumo do que está pronto e do que falta.

**Concluído:**
- **Sprint 0 — Governança.** Diagnóstico, kit de governança, roadmap, direção de design, guia de publicação.
- **Sprint 1, Parte A — Auditoria de conteúdo.** `AUDITORIA_CONTEUDO_DIDATICA_V4.md` produzida, com a rubrica de excelência (seção 16) e as decisões D-016 a D-019.
- **Sprint 1, Parte B — Fundação técnica.** Pipeline `src/content` → `src/data` → `src/templates` → `src/build.py` funcionando; os 24 capítulos são gerados sem erro; QA automatizado (`src/scripts/qa.py`) com zero falhas bloqueantes; teste E2E via Playwright com 20/20 checagens (camadas, quiz, popover sem teto de 18, progresso persistente, filtro de glossário, zero erro de JS, zero overflow); fidelidade de conteúdo confirmada por contagem de palavras (nenhuma perda em relação à V3). Ressalva: o teste em dispositivo real do Paulo (D-009) ainda não ocorreu, porque o site ainda não estava publicado na `main` no momento do fechamento deste sprint — ver `ESTADO_ATUAL.md` para o status corrente.

**Em aberto:**
- **Sprint 2 — Design system e protótipo.** Tokens CSS, componentes base, ícones SVG, light/dark, protótipo (Home + capítulo 17 + glossário) em `/v4-preview/`. Ainda não iniciado no momento deste documento.
- **Sprint 3 — Shell e hubs.** Ementa, Treinamento, Busca, Glossário completo, Prompts, Biblioteca Visual (estrutura), Progresso, Referências no novo design. Exportar/importar progresso.
- **Sprints 4-6 — Migração de capítulos em lotes de 8.** Reescrita de conteúdo pela rubrica da seção 16, quiz revisado, glossário incremental, popover sem teto.
- **Sprint 7 — Biblioteca Visual licenciada.** Hoje `biblioteca.json` está vazio; imagens com licença verificável e diagramas SVG próprios entram aqui.
- **Sprint 8 — Gamificação e constância.** Medidor de profundidade, badges, "missão do dia", página de progresso redesenhada.
- **Sprint 9 — QA completo e release V4.0.** Checklist final, auditoria de animações, validação de links externos com data, acessibilidade, performance, teste real do Paulo, V3 arquivada em `/v3/`.
- **V4.x pós-release:** aprofundamento Petrobras/Brasil por capítulo com data de verificação (V4.1, D-017); novos prompts (V4.2); PWA leve para leitura offline (V4.3); novos capítulos por demanda (V4.4); sincronização de progresso entre dispositivos, se justificar o custo (V4.5).
