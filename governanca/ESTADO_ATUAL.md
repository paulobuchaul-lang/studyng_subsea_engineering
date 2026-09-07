# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 1 — organização inicial do repositório GitHub + decisões D-004a/D-005/D-006)
**Versão publicada:** nenhuma. A V3 existe como pasta local (zip completo recebido na Sessão 0, 47 arquivos) e NÃO está em servidor web. O repositório atual ainda não recebeu esses 47 arquivos (ver seção "O que ficou bloqueado" abaixo).
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**URL do site publicado:** ainda não existe. D-004a decidida (GitHub Pages público); falta a ativação manual em Settings → Pages (GUIA_PUBLICACAO.md seção 4, passo 4).
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 1 — Publicação e fundação técnica (ver ROADMAP_V4.md). Estrutura entregue nesta sessão; extração de conteúdo e build ainda dependem do reenvio da V3 completa.

## Resumo em 10 linhas

1. A V3 tem 33 páginas HTML, 24 capítulos, 126 termos de glossário, 28 prompts profissionais e 72 questões de quiz. Conteúdo técnico é forte e deve ser preservado integralmente.
2. A V3 nunca funcionou no celular nem no notebook da forma esperada porque foi aberta pelo Google Drive, que não serve sites estáticos (CSS/JS/links relativos não resolvem). Diagnóstico completo em DIAGNOSTICO_V3.md.
3. O zip completo da V3 (47 arquivos) foi recebido e inspecionado na Sessão 0, mas NÃO foi reenviado na Sessão 1. Apenas os 9 documentos de governança chegaram nesta sessão. Decisão D-013: a V3 é insumo, não fonte de verdade; aproveita-se o conteúdo, descarta-se o shell.
4. Decisão tomada (D-004 e D-004a): hospedar como site estático em GitHub Pages público, no repositório já existente. Falta apenas a ativação manual em Settings → Pages.
5. Decisão tomada (D-005): adotar o pipeline "conteúdo como dados + shell como código" (build por script). `src/build.py` e os templates serão escritos assim que os arquivos originais da V3 chegarem, para desenhar o parser contra a estrutura real.
6. Decisão tomada (D-006): direção de design de DESIGN_SYSTEM_V4.md aprovada para virar protótipo no Sprint 2.
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
- **Pipeline de build (`src/build.py`, templates):** D-005 já foi aprovada, mas o script só será escrito junto com a extração real, contra a estrutura verdadeira do HTML da V3 (que tem blocos irregulares, por DIAGNOSTICO_V3.md). Escrever antes seria arriscar retrabalho.
- **Ativação de GitHub Pages:** D-004a já decidida (público). Falta só a ação manual do Paulo em Settings → Pages; não existe ferramenta que faça isso remotamente.

## O que o Paulo precisa fazer antes da próxima sessão

- [ ] Reenviar o zip completo da V3 (47 arquivos) para que Sprint 1 possa extrair conteúdo, gerar o inventário e escrever o build.py.
- [ ] Ativar GitHub Pages em Settings → Pages do repositório (Deploy from a branch → main → / root), conforme GUIA_PUBLICACAO.md seção 4, passo 4.
- [ ] Testar, quando houver primeira publicação, no celular e no notebook e registrar aqui.

## Riscos abertos

- A extração dos capítulos do HTML para Markdown é scriptável, mas blocos com estrutura irregular podem exigir revisão manual. O Sprint 1 registra em INVENTARIO_V3.json o que foi extraído automaticamente e o que ficou marcado para revisão (pendente de receber os arquivos da V3).
- Imagens de fornecedores: mesmo com nova estratégia, pode não haver foto licenciável para todo equipamento. Nesses casos o cartão de fonte substitui a foto, sem imagem quebrada.

## Histórico de sessões

| Sessão | Data | Entregou | Próximo passo definido |
|---|---|---|---|
| 0 | 06/09/2026 | Diagnóstico da V3, kit de governança V4 (9 documentos), roadmap por sprints; zip da V3 recebido e inspecionado | Paulo publica a V3 para teste, decide D-004a/D-005/D-006; Sprint 1 |
| 1 | 07/09/2026 | Repositório GitHub organizado: pasta `/governanca/` com os 9 .md, esqueleto `/src/`, `.nojekyll`, README raiz reescrito; D-004a, D-005 e D-006 decididas pelo Paulo (público, pipeline adotado, design aprovado) | Paulo reenvia zip completo da V3 e ativa GitHub Pages; próxima sessão escreve build.py e extrai conteúdo |
