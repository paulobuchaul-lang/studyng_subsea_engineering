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

## D-016 · 07/09/2026 · Vigente
**Decisão:** As camadas "Técnica" e "Deep dive" de cada capítulo recebem profundidade completa na reescrita (Sprints 4 a 6), não um resumo com um parágrafo a mais em relação à camada "5 minutos".
**Motivo:** Resolver de uma vez o achado central da auditoria (AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 3.1) em vez de deixar a fragilidade de profundidade para uma revisão futura.
**Consequência:** Maior custo de redação por capítulo nos Sprints 4 a 6 (mais sessões por lote de 8 capítulos). B-030 atualizado com este padrão.

## D-017 · 07/09/2026 · Vigente
**Decisão:** A verificação factual com data registrada dos casos Brasil citados nos capítulos (contratos DOF, Oceaneering, Strohm, OneSubsea em Búzios — ver AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 3.4) entra como item de V4.1, depois do release da V4.0, e não bloqueia os sprints atuais.
**Motivo:** Os fatos já vêm com link real da fonte original; falta apenas a data de verificação ao lado do fato, o que é aceitável adiar para não atrasar a migração de conteúdo já em curso.
**Consequência:** B-033 mantido como P1, mas com destino V4.1, não Sprint 1-9.

## D-018 · 07/09/2026 · Vigente
**Decisão:** A reescrita do glossário (126 termos, campo "why" genérico) é incremental, feita junto com a migração de cada lote de capítulos nos Sprints 4 a 6, e não uma sessão dedicada isolada.
**Motivo:** Distribui o custo de redação sem bloquear o início da extração técnica (Parte B do Sprint 1) por uma tarefa de 126 itens.
**Consequência:** O glossário só fica 100% reescrito ao final do Sprint 6. Atualizado por D-019: a reescrita incremental passa a incluir também fechar a cobertura de termos técnicos usados no capítulo, não só reescrever o "why" das entradas já existentes.

## D-019 · 07/09/2026 · Vigente
**Decisão:** A pedido do Paulo, fica estabelecido um critério editorial obrigatório para termos técnicos em inglês: (a) todo termo técnico não-trivial (sigla ou termo em inglês fora do vocabulário comum do dia a dia em português) usado no corpo de um capítulo precisa ter entrada correspondente no glossário antes de esse capítulo ser considerado migrado/aceito; (b) mantém-se o termo em inglês quando é o padrão da indústria/contratos e a tradução geraria estranheza (ex.: "bend stiffener", "as-built"), usa-se português quando há equivalente natural e corrente (ex.: "poço"); em ambos os casos a entrada de glossário é obrigatória sempre que o termo não for de uso comum fora da indústria.
**Motivo:** Medição real (AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 3.8) mostrou que 53 de 60 termos técnicos em inglês amostrados nos capítulos lidos não têm entrada no glossário, e que o popover automático de `assets/app.js` só reconhece termos já cadastrados, além de truncar em 18 ocorrências clicáveis por capítulo — ou seja, boa parte do jargão em inglês fica sem explicação em nenhuma das duas formas de glossário (página completa e popover contextual).
**Consequência:** Script de QA do Sprint 1B (Parte B) passa a checar cobertura de glossário por capítulo. O build da V4 remove o teto fixo de 18 termos e passa a marcar todo termo distinto presente no glossário. B-035 aberto no backlog.

## D-020 · 07/09/2026 · Vigente
**Decisão:** A manutenção da governança atualizada deixa de depender só de disciplina (humana ou do Claude) e passa a ter reforço automático no próprio repositório: um workflow de CI (`.github/workflows/qa-governanca.yml`) valida em todo push/PR que os dez documentos de governança existem, que não há link interno quebrado entre eles, e que toda mudança em `src/`, `capitulos/` ou `assets/` vem acompanhada de atualização de `CHANGELOG.md` ou `ESTADO_ATUAL.md`. Um `PULL_REQUEST_TEMPLATE.md` traz o checklist de governança em todo PR.
**Motivo:** Pedido explícito do Paulo — o repositório precisa ficar "atualizado e bem configurado, de forma profissional e completa", e o projeto precisa "garantir essa atualização constante", não apenas ter isso como instrução em prosa que alguém pode esquecer de seguir.
**Consequência:** Ver detalhamento em CLAUDE.md seção 0.10. Falta uma ação manual única do Paulo para o check realmente bloquear merges: ativar branch protection na `main` exigindo o check `qa-governanca` (GUIA_PUBLICACAO.md seção 5a). Sem essa ativação, o CI roda e sinaliza mas não impede merge.
**Atualização (Sessão 3):** o workflow ganhou um segundo job, `qa-tecnico`, que roda `src/build.py` e `src/scripts/qa.py` a cada push/PR (agora que existe site de verdade para testar, não só governança). `src/scripts/test_e2e.py` (Playwright/Chromium) fica de fora do CI por ora — configurar o browser no runner tem custo que não compensa ainda (B-037); roda manualmente a cada sessão de trabalho.
**Atualização (mesma sessão, superada por D-021):** havia sido registrado que o Paulo marcaria também "Require a pull request before merging" manualmente no Settings. Isso foi revertido pelo Paulo na sequência: ele não quer nenhuma ação manual recorrente. Ver D-021.

## D-021 · 07/09/2026 · Vigente
**Decisão:** Nenhuma trava manual é configurada no GitHub (nem branch protection, nem PR obrigatório clicado pelo Paulo). Em vez disso, o Claude assume o fluxo técnico completo sempre que trabalha no repositório: cria branch, commita, abre PR, confere se o check `qa-governanca` passou e mergeia para a `main` sozinho, sem pedir confirmação do Paulo. Quando o Paulo quiser subir algo manualmente, pode continuar fazendo upload direto na `main` sem passo extra.
**Motivo:** O Paulo foi explícito — "não quero isso, quero que você cuide de tudo" — depois de entender que "Require a pull request before merging" exigiria clique manual dele a cada atualização. O custo de operar uma trava manual recorrente superou o benefício, dado que o Claude já tem acesso de push e ferramentas para conduzir PR e merge sozinho.
**Consequência:** A garantia de qualidade deixa de ser uma trava técnica bloqueante e passa a ser um hábito de processo: toda sessão do Claude fecha com uma auditoria de consistência antes de reportar a entrega como concluída (GUIA_PUBLICACAO.md seção 5a), em vez de uma auditoria agendada à parte — o Paulo escolheu essa cadência ("a cada sessão de trabalho") a uma auditoria quinzenal/mensal fixa. O CI (`qa-governanca`) continua rodando automaticamente em todo push e é a primeira coisa que o Claude confere antes de mergear qualquer PR. B-036 fechado sem ação — não há mais configuração pendente no Settings.

## D-022 · 07/09/2026 · Vigente
**Decisão:** A unidade de fragmentação de conteúdo ("chunking") é a camada de profundidade dentro da mesma página de capítulo (5 minutos / Gerente / Técnica / Deep dive), nunca uma sequência obrigatória de páginas ou telas tipo carrossel/wizard. Dentro de cada camada, o texto também precisa ser fragmentado em parágrafos curtos e sub-blocos com heading próprio — não um bloco monolítico de 300-400 palavras.
**Motivo:** Pedido do Paulo — páginas de conteúdo não podem ser "gigantes", precisam evoluir em partes curtas para não cansar nem assustar a Rafaela, o que a literatura de microlearning sustenta para retenção. Mas o CLAUDE.md seção 4 já exige um "Modo Consulta Imediata": a Rafaela abre um capítulo numa reunião e precisa da resposta na hora, sem navegar por múltiplas telas em sequência até achar o que precisa. Fragmentar via páginas/wizard resolveria o cansaço de quem estuda e quebraria a consulta rápida de quem já sabe o que procura.
**Consequência:** Cada capítulo continua sendo uma página única com URL própria (D-001). O chunking acontece em dois níveis: (1) o controle de camadas já decidido em D-016 — a pessoa escolhe quanto quer ver, ninguém vê a "parede" inteira por padrão; (2) dentro de cada camada, a reescrita de conteúdo dos Sprints 4-6 precisa quebrar o texto em parágrafos curtos e sub-blocos, não só reorganizar em uma camada só um parágrafo mais longo. Isso passa a ser critério explícito na rubrica de "excelente nível" (AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 4) e no Sprint 2: o componente de camada do design system precisa suportar múltiplos sub-blocos visuais dentro de uma camada, não um único parágrafo corrido.
