# DIAGNÓSTICO DA V3 — Plataforma Subsea Rafaela

**Data:** 06/09/2026
**Base analisada:** ARQUITETURA_MESTRE_V3.md, MATRIZ_ACEITE_V3.md, QA_FINAL_V3.md, AUDITORIA_ANIMACOES_V3.md, index.html, biblioteca.html, prompts.html, capitulos/m17.html
**Não analisado (não disponível):** assets/styles.css, assets/data.js, assets/app.js e as demais 29 páginas. As conclusões sobre shell, busca, popovers e progresso são inferidas a partir do HTML e dos relatórios de QA, não de execução.

## 1. Veredito em uma frase

O conteúdo da V3 é um ativo real e deve ser preservado; a arquitetura de entrega (hospedagem, assets, imagens) e a experiência de uso (navegação, hierarquia visual, quiz, gamificação) precisam ser reconstruídas.

## 2. Causa raiz do problema relatado ("o CSS não funcionou")

Toda página carrega três dependências por caminho relativo: `assets/styles.css`, `assets/data.js`, `assets/app.js` (nos capítulos, com `../`). Isso é correto para um site servido por HTTP. Não funciona quando:

- os arquivos são abertos pelo Google Drive: a pré-visualização do Drive isola o HTML, não resolve caminhos relativos e não permite navegação entre páginas;
- a pasta `assets/` não foi copiada junto (os assets não constam do material enviado ao Projeto);
- as páginas são abertas por `file://` no celular: Android e iOS não expõem pastas locais a navegadores de forma utilizável.

A V3 já continha uma evidência do problema: a "ponte via `window.name`" descrita na seção 16 da arquitetura existe apenas para contornar a perda de `localStorage` em `file://`. É um sintoma tratado, não a causa.

Conclusão: a decisão multipágina está certa; faltou a decisão de hospedagem. Sem servidor web, multipágina não funciona em nenhum dispositivo de forma confiável.

## 3. Problemas por área

### 3.1 Entrega técnica

| Problema | Evidência | Impacto | Direção de correção |
|---|---|---|---|
| Sem hospedagem | Não há URL; uso via Drive/arquivo local | Nada funciona no celular; CSS/JS quebram no notebook | Site estático publicado (GitHub Pages ou Cloudflare Pages) |
| Assets fora da fonte de verdade | styles.css/data.js/app.js ausentes do Projeto | Nenhuma sessão consegue evoluir o shell sem reconstruí-lo | Repositório como fonte de verdade do código; Projeto guarda governança |
| Progresso preso ao navegador | localStorage por dispositivo | Celular e notebook não compartilham XP/conclusões | Exportar/importar progresso (curto prazo); sincronização opcional (backlog) |
| Geração monolítica | 33 páginas geradas de uma vez, com menu de 24 itens repetido em cada uma | Qualquer mudança de shell exige regenerar tudo; alto risco de regressão de conteúdo | Separar conteúdo (dados) de shell (template) com build por script |
| Ícones em Unicode | ⌁ ⌕ ◐ ☰ ▶ ≡ ✦ ▣ ◆ ↗ | Renderização inconsistente entre aparelhos; aparência amadora | Ícones SVG inline (estilo linha) |

### 3.2 Recursos visuais

As 11 fotografias da Biblioteca Visual e as 2 do capítulo 17 são hotlinks para servidores de NOV, Subsea7, TechnipFMC, OneSubsea, Oceaneering, Oil States, Petrobras e um CDN de terceiros, com `referrerpolicy="no-referrer"` e `onerror` que esconde a imagem. A maioria desses servidores bloqueia carregamento a partir de outros domínios. O próprio HTML já renderiza "Imagem externa indisponível" como comportamento esperado. A Biblioteca Visual hoje é uma lista de links com cartões sem imagem.

Além do problema técnico, há um problema de direito de uso: hotlink não equivale a licença. A estratégia precisa distinguir três casos: (a) fontes com licença aberta (Wikimedia Commons, Flickr CC, agências governamentais com termos claros), que podem ser copiadas localmente com crédito; (b) fontes oficiais sem licença aberta, que viram "cartão de fonte" com link, legenda e "o que observar", sem imagem embutida; (c) diagramas didáticos próprios em SVG, que substituem foto quando não existe imagem licenciável.

### 3.3 Experiência de uso

**Home.** Sete botões de ação, oito cartões e nove atalhos, todos apontando para os mesmos nove destinos. A usuária decide três vezes a mesma coisa. O bloco "Continuar de onde parou" está abaixo do herói, quando deveria ser o primeiro elemento para quem está em Modo Formação.

**Navegação.** O menu principal tem cinco itens no topo e o menu lateral (sheet) repete os hubs e lista os 24 capítulos. No mobile isso vira uma lista longa dentro de um sheet. Falta uma navegação de fundo de tela (bottom tab bar) com os quatro ou cinco modos de uso, e falta um "Neste capítulo" para saltar entre seções longas.

**Capítulo.** A arquitetura promete cinco camadas (5 minutos, gerente, técnica, deep dive, aplicação). No capítulo 17 elas existem como blocos sequenciais numa página longa, sem controle para escolher a camada. Quem chega para uma reunião em 20 minutos rola por tudo. O painel PM (atenção, perguntas, documentos, red flags) está bem escrito, mas aparece como quatro caixas consecutivas; funciona melhor como abas ou acordeão.

**Quiz.** Distratores como "Nada", "Somente pintura do winch" e "Apenas pressão do reservatório" tornam o acerto óbvio. A arquitetura exige questões conceituais, situacionais e "o que você faria como PM". Com distratores triviais, o XP mede cliques, não aprendizado. Regra para V4: cada distrator representa uma concepção equivocada plausível, e o feedback explica por que cada opção errada é errada.

**Gamificação.** XP, fases e badges existem, mas a Home mostra apenas "0 XP · 0 capítulos". Falta o próximo marco visível ("faltam 2 capítulos para Integradora de Sistemas"), falta metáfora ligada ao domínio e falta celebração calibrada. Proposta na DESIGN_SYSTEM_V4: progresso como profundidade (a Rafaela "desce" do litoral às águas ultraprofundas conforme avança).

**Tipografia e densidade.** Texto pequeno (0.78rem em vários pontos), parágrafos longos com dezenas de termos em inglês seguidos, sem respiro. Medida de linha e escala tipográfica precisam ser definidas para leitura em celular.

### 3.4 Conteúdo

Pontos fortes que não podem regredir: sequência didática do second-end pull-in; lista "o que governa o projeto do pull-in system"; perguntas de reunião com qualidade real; red flags; ciclo de vida do próprio pull-in system; referências públicas Petrobras separadas de material de fornecedor; 28 prompts com "Para que serve" e "Termos"; disclaimer de informação corporativa nos prompts.

Pontos a evoluir: camadas de profundidade explícitas; glossário contextual verificável (não foi possível confirmar os popovers sem app.js); quizzes com raciocínio; "Para onde isso está indo" por capítulo (hoje concentrado no capítulo 22); exemplos numéricos simples onde ajudem a intuição (ordem de grandeza de cargas, profundidades, durações), sempre marcados como ilustrativos.

### 3.5 Governança

Os quatro documentos V3 são bons e devem ser mantidos. Lacunas:

- A MATRIZ marca "Responsividade mobile ✅" com base em teste de viewport em navegador; o teste no dispositivo real e no ambiente de uso da Rafaela nunca aconteceu. A Definition of Done da V4 passa a exigir teste na URL publicada, em celular e notebook.
- ARQUITETURA_MESTRE_V3 tem duas seções numeradas "16" e ainda cita "V2" em vários pontos. Será consolidada como ARQUITETURA_MESTRE_V4 no Sprint 2, sem perda de conteúdo.
- CHANGELOG.md, BACKLOG.md e DECISOES.md eram exigidos pelo CLAUDE.md e não existiam. Criados na Sessão 0.
- Não existia um arquivo de "estado atual" para retomada entre sessões. Criado (ESTADO_ATUAL.md).
- O código (HTML/CSS/JS) não tinha fonte de verdade acessível ao Claude. Passa a ser o repositório.

## 4. O que está certo e deve ser mantido

- Arquitetura multipágina com URL por capítulo.
- Dois modos de uso (Formação e Consulta Imediata) sem bloqueio por gamificação.
- Bloco "Se você precisa entender isto agora" com pré-requisitos condensados.
- Painel PM em todo capítulo (atenção, perguntas, documentos, red flags).
- Assistente LLM com três modos e campo "MINHA DÚVIDA".
- Biblioteca de prompts com "Para que serve" e "Termos".
- Auditoria pedagógica de animações (o critério "se eu remover, a compreensão piora?" é excelente e permanece).
- Separação explícita entre requisito normativo, Petrobras, academia, fornecedor e comercial.
- Aliases de busca (pull in / pullin / winch / guincho).

## 5. Sugestões que o Paulo pode não ter considerado

1. **Repositório como memória do Claude.** Com o site no GitHub, cada sessão começa buscando os arquivos correntes pela URL raw. Isso elimina o problema "regenerar da memória" de forma estrutural, não por disciplina.
2. **Conteúdo como dados.** Cada capítulo vira um arquivo Markdown (ou JSON) com seções nomeadas; o build monta as páginas. Evoluir o capítulo 12 não toca no capítulo 17. O glossário e o índice de busca são gerados, não digitados.
3. **Protótipo antes do rollout.** Redesenhar Home + capítulo 17 + glossário primeiro, aprovar com você (e idealmente com a Rafaela), e só então aplicar aos outros 23. Evita refazer 33 páginas duas vezes.
4. **Progresso como profundidade.** Substituir a barra genérica por um medidor de profundidade: cada fase corresponde a uma lâmina d'água (litoral, plataforma continental, talude, águas profundas, ultraprofundas, campo completo). É lúdico, é do domínio dela e não infantiliza.
5. **Missão do dia.** Um cartão na Home que propõe uma ação de 10 a 15 minutos (um capítulo express, cinco termos, um quiz de revisão). Constância sem streak compulsivo.
6. **Feedback da própria Rafaela.** Um link "isso não ficou claro" em cada seção, que abre um e-mail ou formulário simples. O produto é para uma pessoa; a fonte de priorização mais barata é ela.
7. **Progressive Web App leve.** Um manifest e um service worker mínimo permitem "adicionar à tela inicial" no celular e leitura offline do texto principal. Entra no backlog, não no Sprint 1.
8. **Exportar/importar progresso** como arquivo JSON já na V4.0, para ela migrar entre celular e notebook até existir sincronização.

## 6. Inventário de aproveitamento V3 → V4 (a V3 é insumo, não restrição; ver D-013)

| Recurso V3 | Status na V4 |
|---|---|
| 24 capítulos, títulos e ordem | Aproveitar o texto; títulos e ordem serão reavaliados no Sprint 2 (B-026) |
| 126 termos de glossário | Preservar e ampliar |
| 28 prompts profissionais | Preservar; revisar campos e adicionar novos do backlog |
| 72 questões de quiz | Preservar enunciados; reescrever distratores triviais; adicionar feedback por opção |
| Diagramas interativos auditados (13) | Preservar; migrar para o novo frame de diagrama; reauditar |
| Painel PM em 24/24 | Preservar; nova apresentação (abas) |
| Assistente LLM em 24/24 | Preservar |
| Busca com aliases | Preservar; índice gerado pelo build |
| Voltar ao ponto exato do glossário | Preservar |
| Exportar progresso | Preservar; adicionar importar |
| Ponte window.name | Remover (desnecessária com hospedagem HTTP); registrar em DECISOES |
| Fotos hotlinkadas | Substituir conforme D-007 |
| Ícones Unicode | Descartar; SVG próprio |
| Shell, styles.css, app.js | Descartar; reescrever a partir do DESIGN_SYSTEM_V4 |
| ARQUITETURA_MESTRE_V3 | Insumo para ARQUITETURA_MESTRE_V4; CLAUDE.md prevalece em qualquer divergência |
