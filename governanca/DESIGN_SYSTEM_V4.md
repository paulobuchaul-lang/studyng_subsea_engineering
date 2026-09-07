# DESIGN_SYSTEM_V4.md — Direção de design e sistema de componentes

**Status:** proposta para aprovação (D-006). Validada por protótipo no Sprint 2 antes de qualquer rollout.
**Briefing do Paulo:** mais profissional, mais clean, mais lúdico, sempre incentivando aprendizado e desenvolvimento. Funcionar igualmente bem no celular e no notebook.

## 1. Conceito

**"Descer com segurança."** A Rafaela aprende descendo do litoral para águas ultraprofundas. A metáfora organiza gamificação, progresso, nomes de fases e alguns elementos visuais, sem virar cenário infantil. O tom é o de um instrumento profissional bem desenhado: sóbrio na base, com um único acento quente reservado para conquista e ação.

Três palavras que guiam cada decisão: **clareza** (uma coisa por tela), **profundidade** (camadas que ela escolhe), **impulso** (sempre um próximo passo visível).

## 2. Princípios de UX

1. Uma decisão por tela. A Home apresenta no máximo quatro caminhos.
2. Continuar é o primeiro elemento para quem está em formação; "Hoje eu preciso..." é o primeiro para quem chegou com pressa.
3. Toda página longa tem "Neste capítulo" e o controle de camadas; ninguém rola por tudo para achar o que precisa.
4. Todo termo técnico é tocável. Popover no desktop, bottom sheet no mobile, "ver no glossário" e retorno ao ponto exato.
5. Progresso sempre mostra o próximo marco, nunca só o acumulado.
6. Nada bloqueia conteúdo. A gamificação reconhece, não controla.
7. Erro no quiz ensina: cada opção errada tem sua explicação.
8. Motion só quando ensina (D-002). Transições de interface em 150 a 250 ms, respeitando reduced-motion.

## 3. Tokens

### 3.1 Cor
Modo claro como padrão de leitura; modo escuro disponível.

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| --bg | #F5F8FA | #0B1B2B | fundo de página |
| --surface | #FFFFFF | #12263A | cartões, painéis |
| --surface-2 | #EAF1F5 | #183349 | áreas secundárias, código, tabelas |
| --ink | #0F2233 | #E8F1F6 | texto principal |
| --ink-2 | #4A6172 | #A9BFCC | texto secundário |
| --line | #D5E0E7 | #244761 | bordas |
| --primary | #0E7C86 | #3FB3BD | ações, links, foco |
| --primary-ink | #FFFFFF | #05161C | texto sobre primary |
| --accent | #FF6B4A | #FF8A6E | XP, marcos, celebração (uso raro) |
| --depth-1 a --depth-6 | do #7FD1DB ao #06263B | idem | escala de profundidade das fases |
| --ok | #2E9E6B | #4CC08A | acerto, concluído |
| --warn | #E0A100 | #F2C14E | pontos de atenção |
| --danger | #D64545 | #F07070 | red flags |
| --pm | #6B4EFF | #9B87FF | painel de gerente de projetos |

Regra: --accent aparece em no máximo um elemento por tela.

### 3.2 Tipografia
Corpo: **Inter** (fallback: system-ui). Títulos e números de destaque: **Sora** (fallback: Inter). Fontes carregadas com `font-display: swap` e cópia local em `assets/fonts/` para funcionar offline.

| Papel | Mobile | Desktop | Peso | Altura de linha |
|---|---|---|---|---|
| Display (título de capítulo) | 28px | 36px | 700 | 1.15 |
| H2 | 22px | 26px | 600 | 1.25 |
| H3 | 18px | 20px | 600 | 1.3 |
| Corpo | 17px | 17px | 400 | 1.6 |
| Pequeno (legendas, fontes) | 14px | 14px | 400 | 1.45 |
| Rótulo (chips, abas) | 13px | 13px | 600, caixa alta com tracking 0.04em | 1 |

Medida máxima do texto corrido: 68 caracteres. Nunca abaixo de 14px em nada legível.

### 3.3 Espaçamento, raio, sombra
Escala de espaço: 4, 8, 12, 16, 24, 32, 48, 64 px. Raio: 8 (chips, botões), 12 (cartões), 20 (bottom sheet). Sombra: apenas em elementos flutuantes (popover, sheet, toast); cartões usam borda, não sombra.

### 3.4 Iconografia
Ícones SVG inline, estilo linha 1.75px, 20 ou 24px, herdando `currentColor`. Conjunto próprio de aproximadamente 30 ícones (casa, trilha, busca, glossário, prompts, biblioteca, progresso, referências, anterior, próximo, concluído, atenção, pergunta, documento, red flag, copiar, expandir, tema, menu, fechar, profundidade, badge, missão, LLM, foto, diagrama, etapa, exportar, importar, feedback). Nenhum emoji ou glifo Unicode em elementos de interface. Emoji continua permitido apenas em texto de celebração, se o Paulo aprovar.

## 4. Layout

### Mobile (até 899px)
- Barra superior compacta: marca, título curto da página, busca.
- **Bottom tab bar** fixa com cinco abas: Trilha · Consultar · Buscar · Prompts · Eu (progresso). Alturas de toque de 48px.
- Conteúdo em coluna única com 16px de margem lateral.
- "Neste capítulo" como botão que abre bottom sheet com as seções.
- Anterior/Próximo no final do capítulo e também acessíveis pelo sheet.

### Desktop (a partir de 900px)
- Sidebar esquerda fixa (280px): marca, cinco modos, lista dos 24 capítulos com marcação de concluído e fase.
- Coluna principal de 720px centrada.
- Trilho direito (240px, a partir de 1200px): "Neste capítulo", controle de camadas e progresso do capítulo.

## 5. Componentes

**Cartão Express ("Se você precisa entender isto agora")**: fundo --surface-2, ícone de relâmpago, três frases, chips de pré-requisitos tocáveis. Sempre o primeiro bloco do capítulo.

**Controle de camadas**: segmentado com quatro opções (5 min · Gerente · Técnica · Deep dive). Não navega para outra página: filtra a visibilidade dos blocos marcados com `data-layer`. Estado lembrado por capítulo. "Ver tudo" sempre disponível.

**Painel PM**: abas (Atenção · Perguntas · Documentos · Red flags), cor --pm, ícones próprios. No mobile, abas rolam horizontalmente.

**Chip de termo**: sublinhado pontilhado em --primary; toque abre popover (desktop) ou bottom sheet (mobile) com termo, sigla, definição curta, "por que importa" e "ver no glossário".

**Frame de diagrama**: cabeçalho com "por que este recurso visual existe", controles de etapa como botões, área SVG responsiva, legenda de estado, nota "o que este diagrama não representa".

**Cartão de foto/fonte**: dois estados. Com imagem licenciada: foto local, legenda, "o que observar", crédito e licença. Sem imagem: cartão de fonte com o mesmo texto e link, sem área vazia.

**Quiz**: uma questão por vez, opções como cartões, feedback por opção, "tentar de novo", marcação de XP conquistado uma única vez.

**Medidor de profundidade**: barra vertical (mobile: horizontal compacta) com seis zonas nomeadas; marcador da posição atual; texto "faltam N capítulos para [próxima fase]".

**Badge**: SVG monocromático em --ink-2, ganha --accent quando conquistado. Sem texto de "bloqueado".

**Cartão de prompt**: título, "Para que serve", "Quando usar", "Termos", campos [PREENCHA] destacados, botão copiar com confirmação em toast.

**Toast**: canto inferior (acima da tab bar no mobile), 2 s, sem sobrepor botões.

**Missão do dia** (Sprint 8): cartão na Home com uma ação de 10 a 15 min e um botão.

## 6. Home (estrutura aprovada para protótipo)

1. Saudação curta com fase atual e medidor de profundidade compacto.
2. **Continuar**: último capítulo, progresso do capítulo, botão.
3. **Hoje eu preciso...**: seis situações (reunião sobre um tema · entender um equipamento · analisar um documento · acompanhar operação · tratar IMR/intervenção · retirada/descomissionamento), cada uma com um destino único.
4. **Trilha**: mapa compacto das seis fases com capítulos como pontos; toque abre a Ementa naquela fase.
5. Rodapé com data de revisão de conteúdo e link para Referências.

Busca fica na barra superior; Glossário, Prompts, Biblioteca e Progresso ficam na navegação, não como cartões duplicados na Home.

## 7. Acessibilidade e responsividade

Contraste AA em todos os pares de cor listados. Foco visível de 2px em --primary. Alvos de toque de 44px no mínimo. Texto respeita zoom do sistema (unidades rem). Navegação por teclado em abas, popovers e quiz. `prefers-reduced-motion` desliga transições e animações não pedagógicas. Sem overflow horizontal em 360px de largura.

## 8. O que NÃO fazer

Confete em tela cheia. Mascote. Contadores de streak que punem ausência. Ícones em emoji. Três caminhos diferentes para o mesmo destino na mesma tela. Sombra em cartão estático. Animação de fundo. Texto abaixo de 14px. Imagem hotlinkada. Cor de acento em mais de um elemento por tela.

## 9. Checklist de aprovação do protótipo (Sprint 2)

- [ ] A Home no celular cabe em duas telas e tem um caminho óbvio.
- [ ] O capítulo 17 no celular permite ir direto ao painel PM em dois toques.
- [ ] O controle de camadas reduz visivelmente o capítulo em "5 min".
- [ ] Um termo tocado abre definição e volta ao mesmo ponto.
- [ ] O medidor de profundidade diz qual é o próximo marco.
- [ ] O modo escuro é legível sem ajustes.
- [ ] O Paulo consegue descrever a identidade em uma frase sem olhar este documento.
