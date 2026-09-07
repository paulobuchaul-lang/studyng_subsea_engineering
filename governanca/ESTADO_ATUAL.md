# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 1 — organização inicial do repositório GitHub)
**Versão publicada:** nenhuma. A V3 existe como pasta local (zip completo recebido na Sessão 0, 47 arquivos) e NÃO está em servidor web. O repositório atual ainda não recebeu esses 47 arquivos (ver seção "O que ficou bloqueado" abaixo).
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**URL do site publicado:** ainda não existe (GitHub Pages não foi ativado; ver GUIA_PUBLICACAO.md seção 4 e D-004a pendente)
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 1 — Publicação e fundação técnica (ver ROADMAP_V4.md). Iniciado parcialmente nesta sessão.

## Resumo em 10 linhas

1. A V3 tem 33 páginas HTML, 24 capítulos, 126 termos de glossário, 28 prompts profissionais e 72 questões de quiz. Conteúdo técnico é forte e deve ser preservado integralmente.
2. A V3 nunca funcionou no celular nem no notebook da forma esperada porque foi aberta pelo Google Drive, que não serve sites estáticos (CSS/JS/links relativos não resolvem). Diagnóstico completo em DIAGNOSTICO_V3.md.
3. O zip completo da V3 (47 arquivos) foi recebido e inspecionado na Sessão 0, mas NÃO foi reenviado na Sessão 1. Apenas os 9 documentos de governança chegaram nesta sessão. Decisão D-013: a V3 é insumo, não fonte de verdade; aproveita-se o conteúdo, descarta-se o shell.
4. Decisão tomada (D-004): hospedar como site estático. O repositório GitHub já existe (criado fora desta conversa, na conta paulobuchaul-lang), o que resolve a parte prática de D-004a na direção da opção A (GitHub Pages), mas a visibilidade (público vs. protegido) e a ativação de Pages ainda não foram confirmadas pelo Paulo.
5. Decisão PENDENTE do Paulo (D-005): migrar para pipeline "conteúdo como dados + shell como código" (build por script) ou manter HTML editado manualmente.
6. Decisão PENDENTE do Paulo (D-006): aprovar a direção de design descrita em DESIGN_SYSTEM_V4.md, ou pedir ajustes antes do protótipo.
7. A UX será reconstruída: Home simplificada, navegação por abas no mobile, capítulos com camadas de profundidade navegáveis, quiz com distratores plausíveis, gamificação com metáfora de profundidade. Detalhes em DESIGN_SYSTEM_V4.md.
8. A Biblioteca Visual será refeita com estratégia de licenciamento (D-007): imagens hotlinkadas de fornecedores não carregam e serão substituídas por fontes licenciáveis ou cartões de fonte bem desenhados.
9. A dinâmica de continuidade entre sessões passa a ser: ler ESTADO_ATUAL → buscar arquivos correntes no repositório → executar o sprint do ROADMAP → entregar release + governança atualizada. Protocolo em CLAUDE.md, Parte 0.
10. A regra "adicionar ou melhorar sem regredir" vale para conteúdo e funções, não para forma (D-013). O inventário do que se aproveita está em DIAGNOSTICO_V3.md, seção 6.

## O que a Sessão 1 entregou

- Estrutura de repositório criada: `/governanca/` (cópia dos 9 .md), `/src/content/`, `/src/data/`, `/src/templates/` (esqueleto, vazios propositalmente — ver bloqueios abaixo), `.nojekyll`, `README.md` raiz reescrito.
- Nenhum conteúdo de capítulo, glossário, prompt ou imagem foi migrado nesta sessão, porque o repositório de trabalho não tinha os arquivos originais da V3 (HTML, `assets/data.js`, `assets/styles.css`, `assets/app.js`, imagens) disponíveis. Só os documentos de governança em Markdown chegaram nesta sessão.
- Nenhum script de build (`src/build.py`) foi criado, porque D-005 continua PENDENTE. Criar o pipeline antes da decisão arriscaria construir em cima de uma arquitetura que o Paulo pode não aprovar.
- GitHub Pages não foi ativado (é uma ação manual em Settings → Pages, feita pelo Paulo no navegador, conforme GUIA_PUBLICACAO.md seção 4, passo 4). Também depende de D-004a (público vs. protegido por login).

## O que ficou bloqueado e por quê

- **Inventário e extração de conteúdo da V3 (itens 1 e 3 do Sprint 1):** exigem os 47 arquivos originais da V3 (HTML dos 24 capítulos, `assets/data.js` com glossário/prompts/aliases, `assets/styles.css`, `assets/app.js`, imagens). Esses arquivos foram recebidos e inspecionados na Sessão 0, mas não foram reenviados nesta sessão. **Ação do Paulo:** reenviar o zip completo da V3 (os mesmos 47 arquivos da Sessão 0) para que a extração e o inventário possam rodar.
- **Pipeline de build (D-005):** decisão pendente. Sem ela, não se sabe se `src/build.py` deve existir nem qual template engine usar.
- **Direção de design (D-006):** decisão pendente. Sem ela, o protótipo do Sprint 2 não tem tokens aprovados para aplicar.
- **Visibilidade do repositório e ativação de GitHub Pages (D-004a):** decisão pendente sobre público vs. protegido por login. Ativar Pages é uma ação manual do Paulo em Settings → Pages.

## O que o Paulo precisa fazer antes da próxima sessão

- [ ] Reenviar o zip completo da V3 (47 arquivos) para que Sprint 1 possa extrair conteúdo e gerar o inventário.
- [ ] Decidir D-004a: site público (GitHub Pages) ou protegido por login (Cloudflare Pages + Access), e ativar Pages em Settings do repositório se optar pela opção A.
- [ ] Decidir D-005 (pipeline conteúdo-como-dados) e D-006 (direção de design). Basta responder "aprovado" ou apontar o que mudar.
- [ ] Testar, quando houver primeira publicação, no celular e no notebook e registrar aqui.

## Riscos abertos

- A extração dos capítulos do HTML para Markdown é scriptável, mas blocos com estrutura irregular podem exigir revisão manual. O Sprint 1 registra em INVENTARIO_V3.json o que foi extraído automaticamente e o que ficou marcado para revisão (pendente de receber os arquivos da V3).
- Imagens de fornecedores: mesmo com nova estratégia, pode não haver foto licenciável para todo equipamento. Nesses casos o cartão de fonte substitui a foto, sem imagem quebrada.

## Histórico de sessões

| Sessão | Data | Entregou | Próximo passo definido |
|---|---|---|---|
| 0 | 06/09/2026 | Diagnóstico da V3, kit de governança V4 (9 documentos), roadmap por sprints; zip da V3 recebido e inspecionado | Paulo publica a V3 para teste, decide D-004a/D-005/D-006; Sprint 1 |
| 1 | 07/09/2026 | Repositório GitHub organizado: pasta `/governanca/` com os 9 .md, esqueleto `/src/`, `.nojekyll`, README raiz reescrito | Paulo reenvia zip completo da V3; decide D-004a, D-005, D-006 |
