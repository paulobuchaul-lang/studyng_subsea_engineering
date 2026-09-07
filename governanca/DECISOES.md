# DECISOES.md — Registro de decisões arquiteturais e de produto

Formato: ID · data · status (Vigente / Pendente / Superada) · decisão · motivo · consequências.
Decisões Pendentes exigem resposta do Paulo. Decisões Vigentes só mudam com nova entrada que as supere.

---

## D-001 · 2026 (V2→V3) · Vigente
**Decisão:** Arquitetura multipágina com URL própria por capítulo, em vez de página única.
**Motivo:** Acesso direto por assunto, links compartilháveis, leitura no celular sem rolagem infinita.
**Consequência:** Exige servidor web (ver D-004). Menu e shell repetidos em todas as páginas exigem geração automatizada (ver D-005).

## D-002 · 2026 (V3) · Vigente
**Decisão:** Animação só permanece se ensinar direção, sequência, transferência de carga, comparação ou feedback. Movimento decorativo é removido.
**Motivo:** Critério pedagógico definido no CLAUDE.md, seção 14.
**Consequência:** Toda animação nova passa pela pergunta "se eu remover, a compreensão piora?". Auditoria registrada em AUDITORIA_ANIMACOES.

## D-003 · 2026 (V3) · Vigente
**Decisão:** Todo prompt profissional tem "Para que serve" e "Termos". Todo capítulo tem assistente LLM com três modos.
**Motivo:** Rafaela não é especialista; o prompt precisa ensinar seu próprio uso.
**Consequência:** Novos prompts seguem o mesmo template.

## D-004 · 06/09/2026 · Vigente
**Decisão:** A plataforma passa a ser publicada como site estático em servidor HTTP/HTTPS. Google Drive deixa de ser meio de uso e passa a ser apenas backup de releases (.zip por versão) e de documentos.
**Motivo:** O Drive não serve sites; caminhos relativos, JS e navegação entre páginas não funcionam. Foi a causa raiz do problema "CSS não funcionou". Ver DIAGNOSTICO_V3.md, seção 2.
**Consequência:** localStorage passa a funcionar normalmente; a ponte via window.name é removida. O repositório vira fonte de verdade do código. Guia operacional em GUIA_PUBLICACAO.md.

## D-004a · 06/09/2026, confirmada em 07/09/2026 · Vigente
**Decisão:** Opção (A) — GitHub Pages em repositório público (`paulobuchaul-lang/studyng_subsea_engineering`).
**Opções consideradas:**
(A) GitHub Pages em repositório público. Gratuito, simples, URL estável. O conteúdo fica acessível a qualquer pessoa com o link (não indexado por padrão se não for divulgado, mas público).
(B) Repositório privado no GitHub + Cloudflare Pages + Cloudflare Access (login por e-mail). Gratuito nos limites atuais; protege por login; exige duas contas.
**Motivo:** o repositório já existia público nessa conta; manter a opção A evita reconfigurar visibilidade e credenciais. O conteúdo não pode conter, em nenhum caso, informação confidencial Petrobras ou contratual.
**Consequência:** falta apenas a ação manual do Paulo em Settings → Pages (Deploy from a branch → main → / root) para o site entrar no ar; não há ferramenta que ative isso remotamente. Passo a passo em GUIA_PUBLICACAO.md seção 4.

## D-005 · 06/09/2026, aprovada em 07/09/2026 · Vigente
**Decisão:** Adotar pipeline "conteúdo como dados, shell como código". Cada capítulo vive em um arquivo Markdown com seções nomeadas (express, conceitos, ciclo de vida, painel PM, quiz, prompts, referências). Glossário, prompts, biblioteca visual e índice de busca vivem em JSON. Um script Python (executado pelo Claude na sessão, não pelo Paulo) gera as 33+ páginas HTML a partir de templates.
**Motivo:** Hoje o shell (menu, header, footer, scripts) está copiado em 33 arquivos. Qualquer mudança de layout exige regenerar tudo, e regenerar tudo por LLM é a principal fonte de regressão de conteúdo. Com dados separados, evoluir um capítulo não toca nos outros, e o shell muda em um único lugar.
**Custo:** menor do que o estimado inicialmente: o `assets/data.js` da V3 já contém glossário (126 termos), prompts (28) e aliases (38) em JSON estruturado. Só o corpo dos 24 capítulos precisa ser extraído do HTML, o que é scriptável. Estimativa: meia sessão. Depois disso, cada sessão fica mais barata e mais segura.
**Alternativa:** manter HTML manual como na V3. Menor custo inicial, maior custo e risco a cada evolução.
**Consequência:** `src/build.py` e os templates em `src/templates/` só podem ser escritos com segurança depois que os 47 arquivos originais da V3 forem reenviados, para que o parser seja desenhado contra a estrutura real dos blocos (inclusive os irregulares citados em DIAGNOSTICO_V3.md) em vez de uma suposição. Ver B-028.

## D-006 · 06/09/2026, aprovada em 07/09/2026 · Vigente
**Decisão:** Direção de design descrita em DESIGN_SYSTEM_V4.md (paleta oceânica com acento coral, tipografia Inter + Sora, ícones SVG, navegação por abas no mobile e barra lateral no desktop, camadas de profundidade como controle segmentado, progresso como medidor de profundidade) aprovada para virar protótipo.
**Validação:** Sprint 2 entrega protótipo navegável (Home + capítulo 17 + glossário) para aprovação antes do rollout aos demais capítulos.

## D-007 · 06/09/2026 · Vigente
**Decisão:** Nenhuma imagem é embutida por hotlink de site de terceiros. Regra em três níveis: (a) imagem com licença aberta verificada é copiada para `assets/img/` com crédito e link da fonte; (b) imagem oficial sem licença aberta vira "cartão de fonte" (título, legenda, o que observar, link), sem tag `<img>`; (c) onde não existe imagem licenciável, diagrama didático próprio em SVG.
**Motivo:** Hotlinks de NOV, TechnipFMC, Oceaneering etc. não carregam (bloqueio de referrer/CORS) e não configuram direito de uso.
**Consequência:** Biblioteca Visual refeita no Sprint 7. Cada imagem local recebe registro em `data/biblioteca.json` com fonte, licença e data de verificação.

## D-008 · 06/09/2026 · Vigente
**Decisão:** Quiz só é aceito se cada distrator representar uma concepção equivocada plausível e se o feedback explicar por que cada opção errada é errada. Pelo menos uma questão por capítulo é situacional ("o que você faria como PM?").
**Motivo:** Distratores triviais na V3 tornam o XP uma medida de cliques.
**Consequência:** As 72 questões são revisadas durante a migração de capítulos (Sprints 4 a 6).

## D-009 · 06/09/2026 · Vigente
**Decisão:** Definition of Done de qualquer release inclui teste na URL publicada, em celular real e em notebook, feito pelo Paulo, além do QA automatizado feito pelo Claude.
**Motivo:** A V3 foi marcada como "responsiva ✅" por teste de viewport em navegador e falhou no uso real.

## D-010 · 06/09/2026 · Vigente
**Decisão:** Continuidade entre sessões é garantida por ESTADO_ATUAL.md (lido primeiro em toda sessão) e pelo repositório (arquivos correntes buscados por URL). O conhecimento do Projeto guarda apenas governança; código e conteúdo vivem no repositório.
**Motivo:** Regra fundamental do CLAUDE.md (nunca evoluir a partir da memória) não era operacionalizável sem fonte de verdade acessível.

## D-011 · 06/09/2026 · Vigente
**Decisão:** Versionamento semântico simplificado: V4.0 é o primeiro release do redesign; V4.x são evoluções de conteúdo e recursos sem mudança de shell; V5 apenas para mudança arquitetural. Nunca usar "FINAL" em nome de arquivo.

## D-012 · 06/09/2026 · Vigente
**Decisão:** Rollout do redesign é incremental: protótipo aprovado (Sprint 2) → hubs (Sprint 3) → capítulos em lotes de 8 (Sprints 4 a 6). A V3 continua publicada até a V4.0 passar na Definition of Done.
**Motivo:** Evita refazer 33 páginas antes de validar a direção.

## D-013 · 06/09/2026 · Vigente
**Decisão:** Os arquivos da V3 (páginas, CSS, JS, documentação de arquitetura V3) são INSUMO, não fonte de verdade nem restrição. A fonte de verdade dos requisitos é o CLAUDE.md (seções 1 a 30). Qualquer elemento da V3 pode ser repensado, reescrito ou descartado quando não atender ao que o CLAUDE.md pede, sem necessidade de justificar cada remoção individualmente.
**O que se aproveita por padrão (porque tem valor comprovado):** texto técnico dos 24 capítulos, painéis PM, 126 termos, 28 prompts, enunciados das 72 questões, lógica pedagógica dos 13 diagramas auditados, aliases de busca, critério de auditoria de animações.
**O que se descarta por padrão:** shell (header, menus, footer), styles.css, app.js, ponte window.name, ícones Unicode, imagens hotlinkadas, geração monolítica de páginas.
**O que fica em aberto para o Sprint 2:** a própria ementa de 24 capítulos e sua ordem, a reavaliar contra o escopo da seção 5 do CLAUDE.md e as seis fases de gamificação (ver B-026).
**Consequência:** o Sprint 1 não precisa reproduzir a V3; extrai o conteúdo para dados e começa o shell V4 do zero. A regra "não regredir" (seção 25) passa a valer para conteúdo e funções, não para forma.

## D-014 · 07/09/2026 · Vigente
**Decisão:** A organização inicial do repositório GitHub (Sessão 1) seguiu apenas com o que independia das decisões então pendentes: estrutura de pastas, cópia da governança em `/governanca/`, `.nojekyll`. Não se criou `src/build.py` nem se migrou conteúdo da V3 na primeira parte da sessão.
**Motivo:** Construir um pipeline ou migrar conteúdo antes da decisão do Paulo (D-005) arriscaria retrabalho; o zip completo da V3 (47 arquivos) recebido na Sessão 0 não estava disponível nesta sessão — apenas os 9 documentos de governança.
**Atualização (mesma sessão):** D-004a, D-005 e D-006 foram decididas pelo Paulo logo em seguida (ver acima), o que desbloqueia o pipeline. `src/build.py` e os templates continuam não escritos, agora só porque os 47 arquivos da V3 ainda não foram reenviados — não mais por decisão pendente. Ver B-028.
**Consequência:** `/src/content/`, `/src/data/` e `/src/templates/` existem como esqueleto vazio com README explicando a dependência restante. Ver ESTADO_ATUAL.md, seção "O que ficou bloqueado".

## D-015 · 07/09/2026 · Vigente
**Decisão:** Inserir uma fase de auditoria de conteúdo, didática, UX de aprendizagem e gamificação como Parte A do Sprint 1, executada antes de qualquer extração técnica ou build. Nenhuma extração de conteúdo é tratada como cópia neutra: nasce sinalizada com os pontos que a auditoria marcou para reescrita.
**Motivo:** Pedido explícito do Paulo — conteúdo e forma de apresentação são a base do projeto e precisam estar em excelente nível antes de qualquer investimento em shell/design/publicação avançar. Alinhado ao critério de decisão da seção 27 do CLAUDE.md (aprendizagem antes de estética e sofisticação tecnológica).
**Consequência:** AUDITORIA_CONTEUDO_DIDATICA_V4.md criado como novo documento de governança, com rubrica objetiva de "excelente nível" por capítulo. Sprints 4 a 6 (migração de capítulos) passam a ter essa rubrica como critério de aceite adicional, não só QA técnico. B-030 a B-034 abertos no backlog a partir dos achados.
**Achados centrais da auditoria (resumo, ver documento completo):** capítulos com 534-1202 palavras não sustentam 4 camadas de profundidade reais; nenhum HTML tem marcação de camada; glossário tem "why" idêntico nos 126 termos; quiz do capítulo 17 ainda tem distratores triviais ("Nada", "Somente pintura do winch"); fatos datados de contratos/casos Brasil não têm data de verificação registrada.
