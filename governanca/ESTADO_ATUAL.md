# ESTADO ATUAL DO PROJETO — Plataforma Subsea Rafaela

> Este é o PRIMEIRO arquivo a ler em qualquer sessão. Ele responde "onde estamos, o que foi decidido, o que vem agora".
> Atualizado ao FINAL de cada sessão. Se a data abaixo for antiga, desconfie e pergunte.

**Última atualização:** 07/09/2026 (Sessão 2 — zip completo da V3 recebido + auditoria de conteúdo/didática/UX/gamificação)
**Versão publicada:** nenhuma ainda com conteúdo real. GitHub Pages foi ativado pelo Paulo, mas a raiz do repositório só tem a estrutura da Sessão 1 (governança + esqueleto vazio) — não há site de produto no ar.
**Versão em desenvolvimento:** V4.0 (redesign + hospedagem + pipeline de conteúdo)
**URL do site publicado:** GitHub Pages ativo (URL a confirmar/registrar na próxima sessão); ainda sem conteúdo de produto.
**Repositório:** https://github.com/paulobuchaul-lang/studyng_subsea_engineering
**Sprint atual:** Sprint 1 — Parte A (Auditoria de conteúdo e didática) concluída. Parte B (fundação técnica e extração) ainda não iniciada — ver ROADMAP_V4.md.

## Resumo em 10 linhas

1. A V3 tem 33 páginas HTML, 24 capítulos, 126 termos de glossário, 28 prompts profissionais e 72 questões de quiz. A voz, as perguntas de reunião e os red flags são fortes e devem ser preservados; a profundidade do corpo técnico e parte dos componentes de aprendizagem (glossário, quiz) são mais rasos do que o CLAUDE.md exige — ver AUDITORIA_CONTEUDO_DIDATICA_V4.md.
2. A V3 nunca funcionou no celular nem no notebook da forma esperada porque foi aberta pelo Google Drive, que não serve sites estáticos (CSS/JS/links relativos não resolvem). Diagnóstico completo em DIAGNOSTICO_V3.md.
3. O zip completo da V3 (43 arquivos) foi recebido e totalmente inspecionado na Sessão 2. Decisão D-013: a V3 é insumo, não fonte de verdade; aproveita-se o conteúdo (com a reescrita que a auditoria mapeou), descarta-se o shell.
4. Decisão tomada (D-004 e D-004a): hospedar como site estático em GitHub Pages público. O Paulo já ativou o Pages em Settings.
5. Decisão tomada (D-005): adotar o pipeline "conteúdo como dados + shell como código" (build por script). `src/build.py` e os templates serão escritos na Parte B do Sprint 1, já informados pela rubrica da auditoria.
6. Decisão tomada (D-006): direção de design de DESIGN_SYSTEM_V4.md aprovada para virar protótipo no Sprint 2.
7. Decisão tomada (D-015): antes de qualquer extração técnica, uma auditoria de conteúdo/didática/UX de aprendizagem/gamificação foi conduzida com o material completo da V3. Achados e rubrica de "excelente nível" em AUDITORIA_CONTEUDO_DIDATICA_V4.md; itens B-030 a B-034 abertos no backlog.
8. A Biblioteca Visual será refeita com estratégia de licenciamento (D-007): imagens hotlinkadas de fornecedores não carregam e serão substituídas por fontes licenciáveis ou cartões de fonte bem desenhados.
9. A dinâmica de continuidade entre sessões passa a ser: ler ESTADO_ATUAL → buscar arquivos correntes no repositório → executar o sprint do ROADMAP → entregar release + governança atualizada. Protocolo em CLAUDE.md, Parte 0.
10. A regra "adicionar ou melhorar sem regredir" vale para conteúdo e funções, não para forma (D-013), e agora também não para profundidade rasa: capítulos migrados precisam atender à rubrica da auditoria, não só preservar o texto que já existia.

## O que a Sessão 2 entregou

- Zip completo da V3 (43 arquivos) inspecionado por inteiro: 24 capítulos lidos por completo via `assets/data.js` (varredura estrutural) mais leitura integral de 5 capítulos representativos (m01, m05, m17, m19, m22), glossário (126 termos), prompts (28), documentação V3.
- `AUDITORIA_CONTEUDO_DIDATICA_V4.md` criado: o que está em nível bom (voz, perguntas de reunião, red flags, prompts, capítulos 19 e 22 como padrão-ouro), o que é frágil (camadas rasas sem marcação real, glossário com "why" genérico repetido nos 126 termos, quiz com distratores triviais/binários ainda presentes, fatos datados sem data de verificação), e uma rubrica objetiva de "excelente nível" por capítulo.
- Governança atualizada: D-015 registrada, B-030 a B-034 abertos, ROADMAP_V4.md com o Sprint 1 dividido em Parte A (auditoria, concluída) e Parte B (extração técnica, ainda não iniciada), Sprints 4 a 6 com a rubrica como critério de aceite adicional.
- Extração técnica (Parte B) deliberadamente NÃO iniciada nesta sessão: começar a copiar o conteúdo para o formato de dados antes de fechar com o Paulo o volume-alvo por capítulo seria repetir o mesmo trabalho depois.

## O que ficou pendente e por quê

- **Extração técnica (Parte B do Sprint 1):** só começa depois que o Paulo confirmar 3 pontos de escopo que mudam o tamanho do trabalho de redação (volume-alvo por capítulo, timing da verificação factual dos casos Brasil, escopo da reescrita do glossário). Ver as perguntas feitas na conversa da Sessão 2 e D-016 a D-018 quando respondidas.
- **URL do site publicado:** GitHub Pages foi ativado pelo Paulo, mas ainda não há conteúdo de produto na raiz do repositório (só a governança da Sessão 1). Isso só muda quando a Parte B do Sprint 1 gerar o site.

## O que o Paulo precisa fazer antes da próxima sessão

- [ ] Responder as 3 perguntas de escopo da auditoria (volume por capítulo, timing da verificação factual, escopo da reescrita do glossário).
- [ ] Quando o site tiver conteúdo real publicado, testar no celular e no notebook e registrar aqui (D-009).

## Riscos abertos

- A extração dos capítulos do HTML para Markdown é scriptável, mas blocos com estrutura irregular podem exigir revisão manual. O Sprint 1 registra em INVENTARIO_V3.json o que foi extraído automaticamente e o que ficou marcado para revisão (pendente de receber os arquivos da V3).
- Imagens de fornecedores: mesmo com nova estratégia, pode não haver foto licenciável para todo equipamento. Nesses casos o cartão de fonte substitui a foto, sem imagem quebrada.

## Histórico de sessões

| Sessão | Data | Entregou | Próximo passo definido |
|---|---|---|---|
| 0 | 06/09/2026 | Diagnóstico da V3, kit de governança V4 (9 documentos), roadmap por sprints; zip da V3 recebido e inspecionado | Paulo publica a V3 para teste, decide D-004a/D-005/D-006; Sprint 1 |
| 1 | 07/09/2026 | Repositório GitHub organizado: pasta `/governanca/` com os 9 .md, esqueleto `/src/`, `.nojekyll`, README raiz reescrito; D-004a, D-005 e D-006 decididas pelo Paulo (público, pipeline adotado, design aprovado) | Paulo reenvia zip completo da V3 e ativa GitHub Pages; próxima sessão escreve build.py e extrai conteúdo |
| 2 | 07/09/2026 | Zip completo da V3 recebido e inspecionado por inteiro; GitHub Pages ativado pelo Paulo; auditoria de conteúdo/didática/UX/gamificação conduzida (AUDITORIA_CONTEUDO_DIDATICA_V4.md); D-015 registrada; B-030 a B-034 abertos | Paulo decide volume-alvo por capítulo, timing da verificação factual e escopo da reescrita do glossário; próxima sessão inicia Parte B do Sprint 1 (extração técnica) |
