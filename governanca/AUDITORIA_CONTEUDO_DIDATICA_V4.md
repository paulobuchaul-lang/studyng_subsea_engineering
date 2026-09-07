# AUDITORIA_CONTEUDO_DIDATICA_V4.md — Conteúdo, didática, UX de aprendizagem e gamificação

**Data:** 07/09/2026 (Sessão 2)
**Base analisada:** os 43 arquivos completos da V3 (`Portal_Subsea_Rafaela_V3_COMPLETO.zip`), incluindo os 24 capítulos completos via `assets/data.js`, leitura integral de 5 capítulos representativos (m01, m05, m17, m19, m22), varredura estrutural dos 24, os 126 termos de glossário, os 28 prompts, e a documentação V3 (MATRIZ_ACEITE_V3, QA_FINAL_V3, AUDITORIA_ANIMACOES_V3).
**Por que este documento existe:** a pedido do Paulo, antes de qualquer extração técnica, build ou publicação avançar, porque conteúdo e didática são a base do produto e precisam estar em nível de excelência antes de ganhar uma casca visual nova.
**Como se relaciona com DIAGNOSTICO_V3.md:** aquele documento avaliou a V3 sem acesso aos arquivos completos (inferência a partir de 4 páginas e dos relatórios de QA). Este documento confirma parte das suspeitas, corrige otimismo indevido da própria MATRIZ_ACEITE_V3, e adiciona achados novos só visíveis com o material completo em mãos.

## 1. Veredito em uma frase

O esqueleto pedagógico é sólido e a voz é certa (fala direto com a Rafaela, traz perguntas de reunião de qualidade real e red flags específicos), mas o conteúdo de cada capítulo é raso demais para sustentar as quatro camadas de profundidade que o próprio CLAUDE.md exige, e uma fração dos componentes de aprendizagem (glossário, quiz, verificação de fatos) foi preenchida de forma mecânica em vez de pensada termo a termo.

## 2. O que já está em nível bom e não pode se perder

- **Voz e orientação a decisão.** Nenhum capítulo trata a Rafaela como estudante genérica. "Para você, gerente de projetos", "Pontos de atenção", "Perguntas que você deve fazer" aparecem nos 24/24 capítulos, com perguntas de qualidade real — exemplo literal do capítulo 17: *"Qual é o governing load case e qual a margem em cada elemento do load path?"*, *"Qual é o single point failure do sistema durante load transfer?"*. Isso é o padrão que a seção 7 do CLAUDE.md pede, não uma aproximação.
- **Red flags específicos e acionáveis** em 24/24 capítulos (não genéricos). Exemplo do capítulo 5: *"Interfaces de hub/orientation ainda preliminares perto da fabricação"*.
- **Capítulo 19 (IMR)** é o melhor do conjunto: estrutura de ciclo de vida completa (DESIGN → INSTALAR → OPERAR → IMR → RETIRAR), tabela ameaça-por-família de ativo, tabela etapa/pergunta técnica/impacto para o PM, e um caso Brasil datado e linkado (DOF, Oceaneering) com URLs reais verificáveis. É o modelo a copiar para os outros 23.
- **Capítulo 22 (tecnologias emergentes)** aplica corretamente a lógica de radar de maturidade da seção 10 do CLAUDE.md (comercial vs. em qualificação vs. field trial), com casos brasileiros nomeados (OneSubsea em Búzios P-74/P-75, Strohm/Petrobras em TCP, FlatFish/Petrobras).
- **Prompts (28)**: estrutura consistente, campos [PREENCHA] claros, instrução de saída bem definida. Amostra lida (reunião técnica, análise de SOW) está no nível profissional que a seção 20 pede.
- **Referências têm URLs reais**, não placeholders — confirmado em código-fonte (DNV, IMCA, Oceaneering, DOF), o que desmente a hipótese de que seriam links fictícios.

## 3. Achados críticos por dimensão

### 3.1 Profundidade e camadas de aprendizagem — CRÍTICO

Cada capítulo tem entre 534 e 1202 palavras no total (média ≈ 730). Esse número cobre simultaneamente a introdução, "se você precisa entender agora", corpo técnico, painel PM completo, perguntas de reunião, documentos, red flags e quiz. Não há, em nenhum dos 24 arquivos HTML, nenhuma marcação de camada (`data-layer` ou equivalente) separando 5 minutos / visão de gerente / visão técnica / deep dive, como pede a seção 12 do CLAUDE.md e como o próprio DESIGN_SYSTEM_V4 pressupõe no "controle de camadas". O que existe é um texto corrido único, o que o DIAGNOSTICO_V3.md já suspeitava e este documento confirma com o texto em mãos.

Consequência prática: migrar esse texto para o novo shell com um controle de camadas visual, sem reescrever o conteúdo, produziria uma interface bonita sobre um conteúdo que não tem profundidade real para preencher a camada "Técnica" nem a "Deep dive" como blocos autônomos. O controle pareceria funcionar, mas a Rafaela selecionaria "Deep dive" e encontraria o mesmo parágrafo raso que já leu em "5 minutos".

### 3.2 Quiz — qualidade desigual, com regressões antigas ainda presentes

D-008 já determinou que distratores triviais devem ser reescritos, mas o material mostra que a inconsistência é maior do que um "reescrever 72 questões": há variação de padrão dentro do próprio conjunto.

- Capítulo 17 ainda tem literalmente as opções *"Nada"* e *"Somente pintura do winch"* como distratores — o mesmo exemplo que o DIAGNOSTICO_V3.md já citava, confirmando que a V3 entregue não corrigiu esse ponto antes do envio.
- Capítulo 19 tem uma questão binária fraca: *"IMR começa quando aparece a primeira falha? Sim / Não"* — nem sequer usa o formato de três alternativas dos demais capítulos, e a resposta é óbvia pela própria pergunta.
- Em contraste, a terceira pergunta situacional ("Como gerente de projetos, qual atitude é mais consistente com este tema?") é boa e consistente nos 24 capítulos — é a primeira e segunda pergunta de cada capítulo que variam de qualidade.

### 3.3 Glossário — "por que importa" é um texto genérico copiado, não conteúdo

Os 126 termos têm estrutura completa (sigla, nome completo, definição, categoria), mas o campo `why` ("por que importa") é o **mesmo texto, palavra por palavra, em todos os termos verificados**: *"Porque reconhecer este termo ajuda você a conectar linguagem técnica a interface, risco, documento ou decisão de projeto."* Isso não é "importância para o projeto" no sentido da seção 13 do CLAUDE.md — é um placeholder que nunca foi individualizado. Um glossário de 126 termos com essa frase repetida 126 vezes não passaria em uma leitura atenta da Rafaela.

### 3.4 Rigor de fontes e verificação factual — relevante dado o contexto Petrobras/compliance

Vários capítulos citam fatos específicos e datados que soam corretos e vêm com URL real (contrato DOF, contrato Oceaneering, trial Strohm/Petrobras, FATs FlatFish/Petrobras, contrato OneSubsea em Búzios), mas nenhum desses trechos carrega uma data de verificação visível no texto, como a seção 9 do CLAUDE.md exige ("registrar quando relevante a data de verificação"). Dado que você trabalha com contratos públicos e reputação regulatória é uma variável que você já me pediu para tratar como prioridade, publicar números de contrato, valores e nomes de empresas sem uma data de verificação ao lado é um risco editorial real: se algum desses fatos estiver desatualizado ou impreciso no momento da publicação, não há como o leitor (ou você) distinguir isso de uma afirmação atual. Isso é B-023 do backlog, mas a auditoria eleva a prioridade: sem isso, o capítulo 19 e o 22 — hoje os dois melhores do conjunto — são também os dois com maior exposição.

### 3.5 Petrobras/Brasil — presente, mas concentrado

Menção nominal a "Petrobras" aparece em 7 dos 24 capítulos (m04, m09, m15, m17, m19, m21, m22). Não é ausência grave, mas confirma o item já registrado (B-016): capítulos como poços/ANM (m05), flow assurance (m12) e materiais/corrosão (m13) — todos com literatura pública Petrobras disponível — não têm nenhum caso nacional citado.

### 3.6 Higiene visual (não é o foco desta auditoria, mas confirmado em código)

Ícones seguem em Unicode (⌁ ⌕ ◐ ☰ ▶ ≡ ✦ ▣ ◆) nos 24 capítulos e nos hubs, e ao menos 4 capítulos (m04, m15, m17, m21) têm o texto literal "Imagem externa indisponível" renderizado — a foto hotlinkada de fato não carrega. Isso já está coberto por D-007/B-006/B-009 e não muda com esta auditoria; citado aqui só para confirmar que o achado do DIAGNOSTICO_V3.md, feito por inferência, se confirma no material completo.

### 3.7 Sobre a MATRIZ_ACEITE_V3

A matriz original marca como ✅ itens que partes deste documento mostraram frágeis com o material em mãos — "Fotos reais ✅" quando são hotlinks quebrados, "Camadas" implícitas em "Gerente/Técnica" que não existem como blocos. Isso confirma o que DIAGNOSTICO_V3.md seção 3.5 já registrava sobre a matriz ter sido preenchida por autoavaliação, não por teste funcional completo. Ela continua sendo um documento histórico de referência, não uma fonte de verdade sobre o estado real do conteúdo. Uma ressalva importante aparece na seção 3.8 abaixo: nem todo ✅ da matriz estava errado.

### 3.8 Cobertura do glossário e critério de uso de termos em inglês — achado adicional, a pedido do Paulo

**Correção a um achado anterior deste documento:** a primeira versão desta auditoria, seguindo a suspeita do DIAGNOSTICO_V3.md, afirmava que não havia evidência de popover de termo funcional. Isso estava errado, e a MATRIZ_ACEITE_V3 estava certa neste ponto específico. `assets/app.js` implementa o popover: ao carregar um capítulo, um `TreeWalker` varre o texto, casa contra um regex construído a partir dos termos do glossário e envolve as ocorrências em `<span class="term" data-term="...">` clicável/hover, abrindo um popover com termo, nome completo, definição, "por que importa" e link "Ver no glossário" com retorno ao ponto exato (`sessionStorage`). A mecânica descrita na seção 13 do CLAUDE.md existe e funciona.

Mas tem duas falhas estruturais que o achado do Paulo expôs:

1. **Cobertura limitada aos termos já cadastrados.** O regex só reconhece os termos que já estão nos 126 do glossário. Qualquer termo técnico em inglês usado no corpo do texto que não tenha entrada correspondente nunca vira clicável — fica como texto comum, sem explicação disponível em nenhuma das duas formas (popover ou página completa).
2. **Truncamento silencioso em 18 termos por capítulo.** O código limita explicitamente a 18 o número de ocorrências marcadas como clicáveis por página (`if(count>=18)return`). Um capítulo denso em jargão (m17, m19, m21 — os mais técnicos) atinge esse teto e passa a ter termos não-clicáveis mesmo quando estão cadastrados no glossário, sem qualquer aviso ao usuário ou ao autor de conteúdo.

**Medição real da lacuna de cobertura.** Cruzando os termos técnicos em inglês efetivamente lidos nos 5 capítulos analisados na íntegra (m01, m05, m17, m19, m22) contra os 126 termos do glossário: de 60 termos amostrados (hold point, acceptance criteria, tubing hanger, running tool, as-built, baseline survey, condition monitoring, digital twin, integrity management, governing load case, entre outros), **53 não têm entrada no glossário** — só 7 (top angle, hang-off, bellmouth, line pull, choke, work-class ROV, load path) estão cadastrados. Essa é uma amostra de 5 dos 24 capítulos; a lacuna real no conjunto completo é provavelmente maior, não menor, porque os capítulos mais técnicos (SPS, SURF, risers, materiais, geotecnia) ainda não foram lidos na íntegra.

**Critério editorial proposto (a aplicar a partir da migração de cada capítulo):**

- Regra de cobertura: nenhum capítulo é considerado migrado/aceito enquanto tiver um termo técnico não-trivial (sigla ou termo em inglês fora do vocabulário comum do dia a dia em português) sem entrada correspondente no glossário. Isso passa a ser parte do script de QA (Sprint 1B) e do critério de aceite por capítulo (Sprints 4 a 6), junto com a rubrica da seção 4.
- Critério de manter em inglês vs. traduzir: mantém-se em inglês quando é o termo padrão usado em contratos, normas e reuniões reais do setor (ex.: "bend stiffener", "hang-off", "as-built") e a tradução geraria estranheza ou desalinhamento com o vocabulário que a Rafaela vai de fato ouvir; traduz-se ou usa-se o termo em português quando existe equivalente natural e corrente (ex.: "poço", não forçar "well"). Em qualquer um dos dois casos, a entrada do glossário é obrigatória se o termo não for de uso comum fora da indústria.
- Correção técnica necessária no popover da V4: remover o teto fixo de 18 ocorrências (ou torná-lo por termo único, não por ocorrência — marcar todo termo distinto presente no glossário, não as primeiras 18 menções) e gerar, no build, um relatório de "termos citados sem entrada de glossário" por capítulo, para que a lacuna nunca mais fique invisível.

## 4. O que "excelente nível" significa, em termos verificáveis

Proposta de rubrica por capítulo, para orientar a extração/reescrita nos Sprints 4 a 6 e servir de critério de aceite (a aprovar por você):

| Critério | Insuficiente (V3 atual, típico) | Excelente (padrão V4) |
|---|---|---|
| Camadas | Um texto corrido único | 4 blocos com conteúdo próprio: 5 min (≈150 palavras), Gerente (≈300), Técnica (≈400), Deep dive (referências + 1 caso aplicado) |
| Quiz | 3 perguntas, distratores às vezes triviais ou binários | 3 a 4 perguntas, todos os distratores como concepção equivocada plausível, feedback individual por opção (D-008) |
| Glossário (termos do capítulo) | "Why" genérico | "Why" específico ao papel do termo naquele capítulo/projeto |
| Fatos datados/Brasil | Sem data de verificação | Toda alegação de contrato, valor ou caso nomeado leva "verificado em [data]" |
| Tecnologia emergente | Só no capítulo 22 | "Para onde isso está indo" como bloco próprio em todo capítulo onde exista tecnologia emergente relevante (ao menos 10 a 12 dos 24, por natureza do tema) |

## 5. Onde isso entra no roadmap

Ver D-015 em DECISOES.md e a revisão de ROADMAP_V4.md: esta auditoria passa a ser a Parte A do Sprint 1, executada antes da extração mecânica (Parte B). A extração de conteúdo (D-005) deixa de ser uma cópia de texto para formato de dados e passa a ser cópia + reescrita guiada por esta rubrica, capítulo a capítulo, nos Sprints 4 a 6 — sem isso, o Sprint 1 entregaria uma estrutura de dados tecnicamente correta carregando o mesmo problema de profundidade que já existe hoje. A cobertura de glossário (seção 3.8) entra como verificação automatizada no script de QA do Sprint 1B e como parte da reescrita incremental de glossário por capítulo (D-018).

## 6. Decisões tomadas nesta sessão

- **D-016 — Volume por capítulo:** profundidade completa nas camadas Técnica e Deep dive, não um resumo com mais um parágrafo.
- **D-017 — Verificação factual dos casos Brasil:** entra em V4.1, depois do release da V4.0, não bloqueia o Sprint atual.
- **D-018 — Reescrita do glossário:** incremental, por capítulo migrado (Sprints 4 a 6), e passa a incluir também fechar a cobertura de termos técnicos usados naquele capítulo (seção 3.8), não só reescrever o "why" das entradas já existentes.
- **D-019 — Critério de uso de termos em inglês e cobertura obrigatória de glossário:** ver seção 3.8. Regra vigente a partir desta sessão.

Ver texto completo de cada decisão em DECISOES.md.
