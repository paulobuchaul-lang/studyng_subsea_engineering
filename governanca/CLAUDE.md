PLATAFORMA SUBSEA RAFAELA — INSTRUÇÃO PERMANENTE DO PROJETO
Versão 3 — 07/09/2026. A Parte 0 (protocolo de sessão) foi ampliada com a seção 0.10 (garantia de atualização contínua via CI). As seções 1 a 30 são as originais do Paulo, preservadas na íntegra.

===============================================================
PARTE 0 — PROTOCOLO DE SESSÃO E FONTES DE VERDADE
===============================================================

0.1 ORDEM DE LEITURA OBRIGATÓRIA AO INICIAR QUALQUER SESSÃO

1. ESTADO_ATUAL.md — onde estamos, o que está decidido, o que vem agora, o que o Paulo precisava fazer.
2. ROADMAP_V4.md — qual sprint executar e seu critério de aceite.
3. DECISOES.md — decisões vigentes e pendentes. Nunca contrariar uma decisão Vigente sem registrar nova decisão que a supere.
4. BACKLOG.md — pendências; não implementar item do backlog sem promovê-lo ao sprint.
5. DESIGN_SYSTEM_V4.md — tokens e componentes; toda tela nova obedece a ele.
6. ARQUITETURA_MESTRE (versão mais recente) — especificação funcional e de conteúdo.
7. DIAGNOSTICO_V3.md — para lembrar o que não pode regredir (seção 6).
8. CHANGELOG.md, MATRIZ_ACEITE, QA, AUDITORIA — quando relevantes.

Se ESTADO_ATUAL.md estiver ausente ou desatualizado, dizer isso ao Paulo antes de produzir qualquer coisa.

0.2 ONDE VIVE CADA COISA

- Conhecimento do Projeto (Claude): somente documentos de governança em Markdown.
- Repositório (GitHub, URL registrada em ESTADO_ATUAL.md): código, conteúdo, dados, imagens, build. É a fonte de verdade do produto.
- Google Drive: backup de releases (.zip) e cópia dos .md. Nunca meio de uso.

0.3 ANTES DE MODIFICAR O PRODUTO

Buscar os arquivos correntes no repositório (web_fetch nas URLs raw registradas em ESTADO_ATUAL.md; ou pedir o .zip corrente se o repositório ainda não existir). Nunca reconstruir a partir da memória da conversa ou de um resumo. Inspecionar a versão corrente do arquivo antes de reescrevê-lo.

0.4 COMO EXECUTAR UM SPRINT

1. Reler o pedido do Paulo e o sprint no ROADMAP.
2. Confirmar entradas do sprint (decisões pendentes, arquivos necessários). Se faltar algo, dizer exatamente o quê.
3. Se D-005 estiver vigente: editar conteúdo em src/content e src/data, editar shell em src/templates e assets, rodar src/build.py, validar a saída. Nunca editar HTML gerado à mão.
4. Rodar QA automatizado: links locais, IDs duplicados, sintaxe JS, overflow em 360px e 1440px, presença dos blocos obrigatórios de capítulo, ausência de <img> apontando para domínio externo.
5. Auditar animações novas pelo critério da seção 14.
6. Comparar com a versão anterior: nada removido sem registro em DECISOES.
7. Entregar: .zip da versão + ESTADO_ATUAL.md + CHANGELOG.md + BACKLOG.md atualizados (+ DECISOES.md se houve decisão, + MATRIZ_ACEITE se houve release).
8. Dizer ao Paulo, em prosa curta, o que ele deve fazer com cada arquivo entregue e qual é o teste de aceite.

0.5 DEFINITION OF DONE

Um sprint só está concluído quando o Paulo testou na URL publicada, em celular e em notebook, e registrou o resultado no ESTADO_ATUAL.md. QA de viewport em navegador não substitui teste em dispositivo real (D-009).

0.6 ENTREGÁVEIS

- Nomear versões como V4.0-sprintN até o release e V4.0, V4.1 depois. Nunca "FINAL".
- Toda sessão termina com ESTADO_ATUAL.md atualizado, mesmo que o sprint não tenha fechado.
- Novas ideias vão para o BACKLOG com classificação e prioridade, não para o sprint corrente.
- Decisões que exigem o Paulo são marcadas PENDENTE em DECISOES.md e listadas em ESTADO_ATUAL.md.

0.7 ESTILO DE COMUNICAÇÃO COM O PAULO

Prosa direta em PT-BR, sem travessões, listas apenas quando a estrutura exige (matrizes, checklists, roadmap). Distinguir fato verificado, inferência e proposta. Dizer explicitamente o que exige decisão dele e o que pode ser executado sem ele.

0.8 CONTEÚDO E SEGURANÇA DE INFORMAÇÃO

O site é público (D-004a, opção A) ou protegido por login (opção B). Em qualquer caso: nenhuma informação confidencial Petrobras, contratual ou pessoal. Apenas fontes públicas, com diferenciação de natureza (norma, Petrobras, academia, fornecedor, comercial, emergente, didática) conforme seção 8.

0.9 STATUS DA V3

A V3 e sua documentação (ARQUITETURA_MESTRE_V3, MATRIZ, QA, AUDITORIA) são insumo histórico, não fonte de verdade (D-013). Em divergência entre V3 e este CLAUDE.md, prevalece este documento. Aproveitar o conteúdo técnico da V3 sempre que tiver valor; descartar forma, shell e código sem necessidade de justificativa individual. O que não pode regredir é conteúdo e função, listados em DIAGNOSTICO_V3.md seção 6.

0.10 GARANTIA DE ATUALIZAÇÃO CONTÍNUA (D-020)

A disciplina de manter ESTADO_ATUAL, CHANGELOG, BACKLOG e DECISOES atualizados (seções 0.6 e 24) não depende só de lembrança humana ou do Claude: o repositório tem mecanismos automáticos que travam isso.

- `.github/workflows/qa-governanca.yml` roda em todo push e pull request, em qualquer branch. Falha o build se: (a) faltar algum dos dez documentos obrigatórios de `/governanca/`; (b) houver link interno quebrado entre os arquivos de governança; (c) o push/PR alterar `src/`, `capitulos/` ou `assets/` sem também alterar `governanca/CHANGELOG.md` ou `governanca/ESTADO_ATUAL.md` no mesmo push. Isso torna "esquecer de atualizar a governança" um build vermelho, não um lapso silencioso.
- `.github/PULL_REQUEST_TEMPLATE.md` traz o checklist de governança (CHANGELOG, ESTADO_ATUAL, DECISOES, BACKLOG, rubrica de conteúdo quando aplicável) direto na descrição de todo PR aberto.
- Branch protection na branch `main` (Settings → Branches, ação manual do Paulo, documentada em GUIA_PUBLICACAO.md) deve exigir que o check `qa-governanca` passe antes de qualquer merge. Sem isso ativado, o CI roda e sinaliza, mas não impede o merge.
- Toda sessão de trabalho no repositório, sessão do Claude ou upload manual do Paulo, deve deixar o CI verde antes de considerar a entrega concluída. CI vermelho é sinal de governança desatualizada, não de erro cosmético a ignorar.

===============================================================
PARTE 1 — REQUISITOS PERMANENTES (seções 1 a 30, texto original do Paulo)
===============================================================

1. OBJETIVO DO PROJETO

Este projeto existe para desenvolver, manter e evoluir uma plataforma digital de aprendizagem chamada provisoriamente Plataforma Subsea Rafaela, destinada à Rafaela, engenheira de produção que atua como Gerente de Projetos em projetos offshore, incluindo instalação, manutenção, intervenção e desinstalação de equipamentos e sistemas submarinos.

A plataforma deve funcionar simultaneamente como:

1. curso estruturado de Engenharia Submarina aplicada à gestão de projetos;
2. referência técnica para consulta imediata;
3. ferramenta de apoio ao trabalho diário;
4. biblioteca visual de equipamentos, sistemas e operações;
5. biblioteca de prompts profissionais para utilização de LLMs;
6. ambiente de aprendizagem gamificado.

O objetivo NÃO é formar uma projetista especialista em cada disciplina de engenharia. O objetivo é desenvolver alfabetização técnica profunda o suficiente para que uma Gerente de Projetos compreenda sistemas, interfaces, riscos, documentação, operações, decisões de engenharia e consiga formular perguntas tecnicamente relevantes.

---

2. REGRA FUNDAMENTAL DE CONTINUIDADE

NUNCA iniciar uma nova evolução da plataforma exclusivamente a partir da memória da conversa ou de uma descrição resumida do projeto.

Antes de modificar o produto, consultar obrigatoriamente os arquivos de governança disponíveis no Projeto, especialmente:

- "ARQUITETURA_MESTRE_V3.md"
- "MATRIZ_ACEITE_V3.md"
- "QA_FINAL_V3.md"
- "AUDITORIA_ANIMACOES_V3.md"
- versão mais recente do portal
- "CHANGELOG.md", se existir
- "BACKLOG.md", se existir
- "DECISOES.md", se existir

Esses documentos constituem a fonte de verdade — Single Source of Truth — do projeto.

Se houver divergência entre uma conversa antiga e a documentação vigente, prevalece a decisão mais recente documentada, salvo nova orientação explícita do usuário.

Nunca recriar do zero algo já implementado sem antes inspecionar a versão corrente.

---

3. ARQUITETURA DO PRODUTO

A plataforma deve permanecer prioritariamente como um site multipágina responsivo, e não como uma única página contínua.

Cada capítulo deve possuir sua própria página e URL.

A estrutura principal deve contemplar, no mínimo:

- Home;
- Ementa;
- Treinamento;
- capítulos individuais;
- Busca;
- Glossário;
- Biblioteca Visual;
- Biblioteca de Prompts;
- Mapa de Progresso;
- Referências;
- documentação de governança do projeto.

O sistema deve funcionar adequadamente em:

- notebook/desktop;
- tablet;
- celular.

A experiência mobile é requisito funcional, não adaptação secundária.

---

4. DOIS MODOS DE USO

A plataforma deve sempre suportar simultaneamente:

Modo Formação

Aprendizado sequencial e progressivo.

A Rafaela pode seguir uma trilha de estudo estruturada, acompanhando seu avanço, quizzes, fases e evolução.

Modo Consulta Imediata

A Rafaela pode acessar diretamente qualquer assunto, sem necessidade de concluir capítulos anteriores.

Exemplo:

Se ela precisar hoje compreender Pull-In, deve conseguir abrir diretamente esse conteúdo e começar a estudar imediatamente.

Conteúdos avançados devem possuir uma seção semelhante a:

«"Se você precisa entender este tema agora"»

Essa seção deve apresentar os conhecimentos prévios estritamente necessários de forma resumida e permitir aprofundamento opcional.

A gamificação NUNCA deve bloquear conteúdo.

---

5. ESCOPO TÉCNICO

A plataforma não deve ser limitada a risers ou Pull-In.

A formação deve abranger Engenharia Submarina de maneira integrada e aplicada ao gerenciamento de projetos offshore.

Entre os temas relevantes estão:

- desenvolvimento de campos offshore;
- arquitetura submarina;
- SPS — Subsea Production Systems;
- SURF;
- poços submarinos;
- wellhead;
- árvore de natal molhada;
- manifolds;
- jumpers;
- flowlines;
- pipelines;
- risers rígidos;
- risers flexíveis;
- umbilicais;
- sistemas de controle;
- flow assurance;
- materiais;
- corrosão;
- proteção catódica;
- geotecnia;
- metocean;
- FPSO e outras unidades flutuantes;
- mooring;
- dynamic positioning;
- embarcações offshore;
- PLSV;
- ROV;
- survey;
- lifting;
- rigging;
- marine operations;
- installation engineering;
- Pull-In;
- Pull-Out;
- pre-commissioning;
- commissioning;
- start-up;
- FAT;
- EFAT;
- SIT;
- SAT;
- IMR;
- inspeção;
- manutenção;
- intervenção;
- reparo;
- integrity management;
- life-of-field;
- desinstalação;
- decommissioning;
- recuperação de equipamentos;
- abandono;
- gestão de interfaces;
- gestão de riscos;
- readiness;
- SIMOPS;
- MOC;
- engenharia de instalação;
- documentação técnica;
- gestão de fornecedores.

O escopo deve evoluir quando forem identificados assuntos relevantes.

---

6. CICLO DE VIDA COMO PRINCÍPIO DIDÁTICO

Sempre que aplicável, um equipamento ou sistema deve ser explicado ao longo do ciclo de vida.

Não limitar a explicação a "o que é".

Perguntar sempre:

- Para que existe?
- Como funciona?
- Quais são seus componentes?
- Quais são suas interfaces?
- Como é fabricado?
- Como é transportado?
- Como é instalado?
- Como é integrado?
- Como é testado?
- Como entra em operação?
- Como é monitorado?
- Como é inspecionado?
- Como é mantido?
- Como é intervencionado?
- Como pode falhar?
- Como é reparado?
- Como é removido?
- Como é descomissionado?
- Quais documentos demonstram que cada etapa foi concluída corretamente?

---

7. FOCO EM GESTÃO DE PROJETOS

Todo tema técnico deve possuir uma camada explícita chamada, ou equivalente a:

O QUE ISSO MUDA NO SEU PROJETO

Essa camada deve explicar, sempre que aplicável:

- principais interfaces;
- disciplinas envolvidas;
- fornecedores envolvidos;
- documentos relevantes;
- predecessoras;
- sucessoras;
- gates;
- hold points;
- acceptance criteria;
- long-lead items;
- riscos;
- premissas;
- restrições;
- dependências;
- impactos de mudança;
- impacto no cronograma;
- impacto em custo;
- impacto offshore;
- impacto em segurança;
- riscos de integração.

Também incluir:

PONTOS DE ATENÇÃO

e

PERGUNTAS QUE VOCÊ DEVERIA FAZER

As perguntas devem ser tecnicamente relevantes para uma Gerente de Projetos e não perguntas genéricas.

Exemplo de qualidade esperada:

Não perguntar apenas:

«"O fornecedor está atrasado?"»

Preferir algo como:

«"Quais interfaces ainda possuem dados TBD/TBC e quais delas impedem o congelamento do design para fabricação?"»

---

8. CONTEXTO PETROBRAS E ECOSSISTEMA BRASILEIRO

A Rafaela atua na Petrobras.

Por isso, recursos públicos, terminologia, casos e práticas relacionadas à Petrobras devem possuir prioridade editorial quando forem tecnicamente adequados.

Entretanto, a Petrobras NÃO deve ser tratada como sistema isolado.

A Engenharia Submarina é executada por um ecossistema de operadores, EPCIs, fabricantes, empresas de instalação, intervenção, survey, ROV, embarcações e fornecedores especializados.

Pesquisar e utilizar também fontes relevantes de empresas atuantes no Brasil ou em projetos tecnicamente comparáveis, como, entre outras:

- TechnipFMC;
- OneSubsea / SLB;
- Subsea7;
- Saipem;
- Baker Hughes;
- MODEC;
- NOV;
- Oceaneering;
- DOF;
- Aker Solutions;
- Oil States;
- Remazel;
- Strohm;
- fornecedores e integradores relevantes identificados futuramente.

Sempre diferenciar claramente:

- requisito normativo;
- requisito corporativo;
- material acadêmico;
- case de fornecedor;
- material comercial;
- tecnologia emergente;
- interpretação didática.

Nunca transformar material comercial de fornecedor em requisito técnico universal.

---

9. PESQUISA E VALIDAÇÃO

Conteúdo técnico relevante deve ser validado utilizando fontes atuais e confiáveis.

Quando o assunto puder ter mudado ou quando versões de normas, tecnologias, projetos ou equipamentos forem relevantes, pesquisar fontes atuais antes de alterar o conteúdo.

Priorizar, conforme aplicável:

- Petrobras;
- DNV;
- API;
- ISO;
- IMCA;
- IOGP;
- universidades;
- papers;
- congressos técnicos;
- fabricantes;
- operadores;
- EPCIs;
- empresas de instalação e intervenção.

Links inseridos no portal devem ser verificados.

Links quebrados, privados, removidos ou excessivamente genéricos devem ser substituídos.

Registrar quando relevante a data de verificação.

---

10. TECNOLOGIAS EMERGENTES

Não limitar o conteúdo às soluções tradicionais.

Sempre avaliar:

«"Existe tecnologia emergente modificando este assunto?"»

Quando existir, criar uma seção equivalente a:

PARA ONDE ISSO ESTÁ INDO

Explicar:

- tecnologia tradicional;
- tecnologia emergente;
- problema que pretende resolver;
- vantagens;
- limitações;
- nível de maturidade;
- exemplos reais;
- utilização no Brasil, se houver;
- impacto potencial para futuros projetos.

Não apresentar tecnologia experimental como solução consolidada.

Indicar claramente o estágio de maturidade.

---

11. DIDÁTICA

Todo conteúdo deve ser escrito diretamente para a Rafaela.

Evitar frases como:

«"O aluno deverá compreender..."»

Preferir:

«"Ao terminar este capítulo, você deverá conseguir..."»

ou:

«"Quando este assunto aparecer em uma reunião, sua primeira preocupação deve ser..."»

A linguagem deve ser tecnicamente correta sem pressupor formação prévia em Engenharia Submarina.

Conceitos complexos devem ser construídos em camadas.

Preferir:

intuição → conceito → funcionamento → engenharia → projeto → aplicação prática.

Usar analogias somente quando melhorarem a compreensão e nunca quando distorcerem o fenômeno físico.

---

12. CONTEÚDO EM CAMADAS

Sempre que o assunto justificar, oferecer níveis de profundidade:

5 MINUTOS

O essencial para compreender uma reunião.

VISÃO DE GERENTE DE PROJETOS

Interfaces, riscos, documentos e decisões.

VISÃO TÉCNICA

Funcionamento físico e engenharia.

DEEP DIVE

Normas, papers, casos reais, vídeos e materiais externos.

---

13. GLOSSÁRIO

Manter um glossário técnico geral e pesquisável.

Cada termo deve possuir, quando aplicável:

- sigla;
- termo em inglês;
- tradução;
- definição;
- explicação didática;
- importância para o projeto;
- termos relacionados.

Termos relevantes dentro dos capítulos devem permitir interação contextual.

No desktop:

- hover ou clique.

No mobile:

- toque.

A definição deve aparecer em popover ou componente equivalente.

Deve existir opção:

«"Ver no glossário"»

Ao retornar do glossário, a Rafaela deve voltar para a posição exata de onde saiu.

Nunca presumir que uma sigla é conhecida apenas porque é comum na indústria.

---

14. DIAGRAMAS

Diagramas são instrumentos de ensino, não decoração.

Preferir SVG e componentes interativos quando isso melhorar a compreensão.

Uma animação só deve existir quando comunicar fenômeno técnico, como:

- direção;
- fluxo;
- sequência;
- mudança de estado;
- transferência de carga;
- feedback;
- propagação;
- movimento;
- causa e efeito.

Movimento puramente decorativo deve ser removido.

Pergunta obrigatória durante QA:

«"Se eu remover esta animação, a compreensão piora?"»

Se a resposta for não, remover a animação.

Exemplos adequados:

- fluxo de produção;
- malha de controle;
- DP feedback loop;
- load path;
- Pull-In;
- sequência de marine operation;
- ciclo IMR;
- decommissioning.

Exemplos que podem ser melhores estáticos:

- corte de flexible pipe;
- comparação entre configurações de riser;
- desenhos geométricos;
- esquemas onde movimento não represente fenômeno físico real.

---

15. RECURSOS VISUAIS REAIS

Utilizar fotografias reais, diagramas, vídeos, animações e materiais externos quando melhorarem o ensino.

Não concentrar todas as fotografias em uma biblioteca isolada.

Distribuí-las também pelos capítulos.

Sempre que possível:

FOTO REAL → O QUE OBSERVAR → DIAGRAMA DIDÁTICO → IMPLICAÇÃO PARA O PROJETO

Fotografias devem possuir fonte e contexto.

Não usar imagem apenas como decoração.

---

16. BIBLIOTECA VISUAL

Manter também uma Biblioteca Visual independente para consulta rápida.

Permitir pesquisa por:

- equipamento;
- sistema;
- operação;
- empresa;
- tecnologia;
- tipo de instalação.

Cada item visual deve explicar:

- o que aparece;
- o que observar;
- por que é importante;
- capítulo relacionado.

---

17. QUIZZES

Todo capítulo deve possuir mini quiz ao final.

As perguntas devem testar:

1. compreensão conceitual;
2. aplicação;
3. raciocínio de projeto.

Evitar quizzes baseados apenas em memorização.

Quando a Rafaela errar:

- explicar por que;
- apresentar novamente o conceito;
- indicar onde revisá-lo.

Quando acertar:

- reforçar o raciocínio correto.

Não conceder XP repetidamente para a mesma resposta correta.

---

18. GAMIFICAÇÃO

A gamificação deve incentivar, nunca infantilizar.

Utilizar:

- XP;
- fases;
- mapa de progresso;
- capítulos concluídos;
- badges;
- desafios;
- marcos;
- celebrações discretas.

Nenhum conteúdo pode ficar bloqueado.

As fases podem representar evolução, por exemplo:

- Exploradora Subsea;
- Integradora de Sistemas;
- Engenheira de Operabilidade;
- Gestora de Operações;
- Guardião de Integridade;
- PM Subsea 360°.

Gamificação deve estimular constância e curiosidade.

---

19. ASSISTENTE LLM EM CADA CAPÍTULO

Todo capítulo deve possuir uma seção recolhível:

APROFUNDE COM UMA LLM

Disponibilizar, no mínimo:

DÚVIDA RÁPIDA

APROFUNDAMENTO COMPLETO

ANALISAR DOCUMENTO

Antes de cada prompt, explicar:

- para que serve;
- quando utilizar;
- que tipo de resposta esperar.

Explicar também termos potencialmente desconhecidos presentes no prompt.

Cada prompt deve conter um campo claramente identificado para a Rafaela escrever:

«MINHA DÚVIDA / O QUE QUERO APROFUNDAR:»

ou equivalente.

---

20. BIBLIOTECA PROFISSIONAL DE PROMPTS

Manter uma página independente com prompts que auxiliem o trabalho diário.

Cada prompt deve possuir:

- título;
- para que serve;
- quando usar;
- termos importantes;
- campos a preencher;
- prompt pronto para copiar.

Cobrir progressivamente atividades como:

- preparar reunião;
- criar pauta;
- preparar perguntas;
- registrar ata;
- analisar contrato;
- analisar SOW;
- analisar especificação;
- analisar datasheet;
- analisar drawing;
- analisar P&ID;
- analisar cálculo;
- comparar revisões;
- criar TQ/RFI;
- analisar interface register;
- preparar MOC;
- preparar FAT;
- preparar EFAT;
- preparar SIT;
- preparar SAT;
- offshore readiness;
- SIMOPS;
- análise de riscos;
- pre-mortem;
- análise de cronograma;
- análise de mudança;
- análise de fornecedor;
- análise de atraso;
- IMR;
- análise de finding;
- intervenção submarina;
- decommissioning;
- lessons learned;
- handover;
- decision paper;
- comunicação executiva;
- escalonamento de risco;
- preparação para gate review.

Novos prompts relevantes podem ser adicionados.

---

21. BUSCA

A busca deve permitir encontrar:

- capítulos;
- subtópicos;
- termos do glossário;
- prompts;
- recursos visuais;
- equipamentos;
- operações.

Criar aliases explícitos para terminologia provável.

Exemplo:

Pull-In deve ser encontrado por:

- pull in;
- pull-in;
- pullin;
- winch;
- guincho;
- riser pull-in.

Busca de emergência deve ser determinística sempre que possível.

---

22. EXPERIÊNCIA MULTIPÁGINA

Cada capítulo deve possuir:

- posição no curso;
- título;
- objetivo;
- botão Anterior;
- botão Próximo;
- acesso à Home;
- acesso à busca;
- progresso;
- marcação de conclusão.

Links devem utilizar páginas reais sempre que possível.

Evitar transformar novamente a plataforma em SPA sem benefício pedagógico claro.

---

23. CONTROLE DE QUALIDADE

Nenhuma nova versão deve ser considerada concluída apenas porque "o recurso existe".

Antes de release, verificar funcionalmente cada requisito.

QA mínimo:

- desktop;
- mobile;
- navegação;
- links;
- busca;
- glossário;
- retorno ao ponto anterior;
- quiz;
- XP;
- progresso;
- prompts;
- diagramas;
- animações;
- imagens;
- links externos;
- ausência de overflow;
- ausência de IDs duplicados;
- ausência de erros JavaScript;
- responsividade;
- acessibilidade básica.

Animações devem passar por auditoria pedagógica.

Links devem passar por auditoria funcional.

---

24. GESTÃO DE MUDANÇAS

Antes de implementar uma mudança significativa:

1. identificar o requisito;
2. avaliar impacto na arquitetura;
3. avaliar impacto em recursos existentes;
4. implementar;
5. testar;
6. atualizar documentação.

Mudanças arquiteturais relevantes devem ser registradas em "DECISOES.md".

Mudanças entre releases devem ser registradas em "CHANGELOG.md".

Pendências conhecidas devem ir para "BACKLOG.md".

---

25. NÃO PERDER FUNCIONALIDADES

Ao evoluir uma versão, não assumir que funcionalidades antigas podem ser descartadas.

Comparar a nova versão com a anterior.

Aplicar o princípio:

«adicionar ou melhorar sem regredir.»

Se uma mudança exigir remoção de funcionalidade, explicar claramente o motivo e registrar a decisão.

---

26. BACKLOG E MELHORIA CONTÍNUA

Ao encontrar uma oportunidade relevante que não deva ser implementada imediatamente, registrar no backlog.

Classificar preferencialmente como:

- conteúdo;
- didática;
- visual;
- interação;
- técnico;
- Petrobras/Brasil;
- tecnologia emergente;
- UX;
- gamificação;
- LLM;
- performance;
- QA.

Não implementar indiscriminadamente toda ideia nova.

Priorizar impacto no aprendizado e no trabalho da Rafaela.

---

27. CRITÉRIO PRINCIPAL PARA DECISÕES

Quando houver dúvida entre duas soluções, priorizar nesta ordem:

1. aprendizagem;
2. correção técnica;
3. utilidade no projeto real;
4. clareza;
5. navegabilidade;
6. evidência;
7. estética;
8. sofisticação tecnológica.

Tecnologia e animação nunca devem prevalecer sobre aprendizagem.

---

28. COMPORTAMENTO AO INICIAR UMA NOVA SESSÃO

Quando o usuário solicitar continuidade do desenvolvimento:

1. consultar os documentos de governança do Projeto;
2. identificar a versão vigente;
3. consultar backlog e decisões pendentes;
4. verificar o último QA;
5. resumir internamente o estado atual;
6. continuar do ponto correto.

Não pedir ao usuário para reconstruir o contexto que já está documentado no Projeto.

Se faltarem arquivos essenciais, informar especificamente qual fonte está faltando.

---

29. COMPORTAMENTO ANTES DE ENTREGAR UMA NOVA VERSÃO

Antes de anunciar uma versão como pronta:

1. reler o pedido atual do usuário;
2. reler os requisitos permanentes;
3. revisar a matriz de aceite;
4. executar QA;
5. registrar problemas encontrados;
6. corrigir problemas relevantes;
7. atualizar changelog;
8. atualizar backlog;
9. atualizar matriz de aceite;
10. somente então gerar o release.

Nunca utilizar "FINAL" no nome de um arquivo se ainda houver pendências relevantes conhecidas.

Preferir versionamento:

"V3.1"
"V3.2"
"V4.0"

---

30. FILOSOFIA DO PRODUTO

A pergunta central durante todo o desenvolvimento deve ser:

«"Depois de estudar isto, a Rafaela compreenderá melhor o que está acontecendo no projeto, identificará riscos antes, fará perguntas melhores e tomará decisões de gestão com maior qualidade?"»

Se a resposta for não, o conteúdo ou recurso precisa ser revisto.
