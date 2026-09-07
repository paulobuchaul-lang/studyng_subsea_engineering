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

A matriz original marca como ✅ itens que este documento mostra frágeis com o material em mãos — "Fotos reais ✅" quando são hotlinks quebrados, "Tooltip/popover contextual ✅" sem nenhuma marcação no HTML que sustente popover real, "Camadas" implícitas em "Gerente/Técnica" que não existem como blocos. Isso confirma o que DIAGNOSTICO_V3.md seção 3.5 já registrava sobre a matriz ter sido preenchida por autoavaliação, não por teste funcional. Ela continua sendo um documento histórico de referência, não uma fonte de verdade sobre o estado real do conteúdo.

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

Ver D-015 em DECISOES.md e a revisão de ROADMAP_V4.md: esta auditoria passa a ser a Parte A do Sprint 1, executada antes da extração mecânica (Parte B). A extração de conteúdo (D-005) deixa de ser uma cópia de texto para formato de dados e passa a ser cópia + reescrita guiada por esta rubrica, capítulo a capítulo, nos Sprints 4 a 6 — sem isso, o Sprint 1 entregaria uma estrutura de dados tecnicamente correta carregando o mesmo problema de profundidade que já existe hoje.

## 6. Decisões que pedem sua entrada

Registradas como perguntas ao Paulo nesta sessão (ver conversa e DECISOES.md D-016 a D-018 quando respondidas): volume-alvo por capítulo (custo de redação vs. tempo de estudo da Rafaela), se a verificação factual dos casos Brasil deve rodar antes da V4.0 ou pode entrar como V4.1, e se o glossário completo (126 termos) deve ser reescrito de uma vez ou de forma incremental por capítulo migrado.
