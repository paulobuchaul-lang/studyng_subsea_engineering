# ROADMAP_V4.md — Plano de evolução por sprints

Princípio: **uma sessão = um sprint = uma entrega testável**. Cada sprint tem entrada (o que precisa existir antes), saída (o que o Paulo recebe) e critério de aceite. Nenhum sprint começa sem o anterior aceito, salvo decisão registrada em DECISOES.md.

Estimativa de sessões é indicativa. Sprints de conteúdo podem se dividir em duas sessões se a qualidade exigir.

---

## Sprint 0 — Governança · CONCLUÍDO em 06/09/2026
Saída: diagnóstico, kit de governança, roadmap, direção de design, guia de publicação.

## Sprint 1 — Fundação técnica e extração de conteúdo
**Entrada:** D-004a e D-005 decididas. (Zip da V3 já recebido.)
**Faz:**
1. Inventário automatizado da V3 (páginas, blocos por capítulo, termos, quizzes, prompts, links, imagens) salvo como `INVENTARIO_V3.json`, marcando o que foi extraído limpo e o que exige revisão.
2. Estrutura do repositório: `/` (site publicado), `/src/content/` (capítulos em Markdown com seções nomeadas), `/src/data/` (glossario.json, prompts.json, aliases.json, biblioteca.json), `/src/templates/`, `/src/build.py`, `/governanca/` (cópia dos .md), `.nojekyll`, `README.md`.
3. Extração do conteúdo da V3 para o formato de dados. Glossário, prompts e aliases vêm prontos do `data.js`; capítulos são extraídos do HTML por bloco (express, corpo, PM, quiz, prompts, referências). Texto técnico não é alterado neste sprint; apenas reorganizado.
4. Esqueleto do shell V4 (sem design final): template de capítulo e de hub que já obedece à estrutura da seção 6 da arquitetura e às camadas `data-layer`. Build gera as 33 páginas em versão "sem estilo bonito, com estrutura certa".
5. Script de QA: links locais, IDs duplicados, blocos obrigatórios por capítulo, `<img>` externo, overflow.
**Saída:** zip do repositório inicial (src + site gerado) e INVENTARIO_V3.json.
**Aceite:** build roda sem erro; 24 capítulos gerados com todos os blocos obrigatórios; QA zero falhas; Paulo abre 3 capítulos na URL e confirma que nenhum texto técnico se perdeu em relação à V3 (comparação por amostragem).
**Pré-condição paralela (do Paulo, independente do Claude):** publicar a V3 como está no repositório para provar que celular e notebook funcionam com hospedagem HTTP. Se funcionar, o diagnóstico está confirmado; se não, o Sprint 1 começa investigando.
**Se D-005 for recusada:** o sprint entrega apenas o inventário, o script de QA e o esqueleto de shell aplicado manualmente a Home + capítulo 17, e o custo de regeneração permanece nos sprints seguintes.

## Sprint 2 — Design system e protótipo
**Entrada:** Sprint 1 aceito; D-006 decidida.
**Faz:** tokens CSS (cores, tipografia, espaçamento, raio, sombra, motion); componentes base (header, tab bar mobile, sidebar desktop, cartão, botão, chip de termo, popover/bottom sheet, quiz, medidor de profundidade, badge, toast, frame de diagrama, cartão de prompt, cartão de foto/fonte); ícones SVG; light/dark; reduced-motion. Aplica ao protótipo: Home nova + capítulo 17 novo + glossário novo. Consolida ARQUITETURA_MESTRE_V4.md.
**Saída:** protótipo publicado em `/v4-preview/` na mesma URL, sem tocar na V3.
**Aceite:** Paulo (e Rafaela, se possível) aprovam a direção visual e a navegação no celular e notebook. Ajustes registrados no BACKLOG antes do Sprint 3.

## Sprint 3 — Shell e hubs
**Faz:** aplica o design aprovado a Ementa, Treinamento, Busca, Glossário completo, Prompts, Biblioteca Visual (estrutura; imagens no Sprint 7), Progresso, Referências. Busca com índice gerado e aliases. Exportar/importar progresso em JSON.
**Aceite:** todos os hubs navegáveis nos dois dispositivos; busca "pull in" abre capítulo 17; exportar/importar funciona entre celular e notebook.

## Sprint 4 — Capítulos 01 a 08 no novo shell
**Faz:** migração com camadas de profundidade navegáveis, painel PM em abas, quiz revisado (D-008), "Para onde isso está indo" onde aplicável, termos com popover. Sem alterar o sentido do conteúdo técnico; melhorias de conteúdo entram como itens explícitos no CHANGELOG.
**Aceite:** QA automatizado (links, IDs, JS) + leitura de amostra pelo Paulo em 2 capítulos.

## Sprint 5 — Capítulos 09 a 16
Mesmo padrão. Inclui reauditoria dos diagramas de riser, flexível, controle, flow assurance, lay systems, marine operations e load path.

## Sprint 6 — Capítulos 17 a 24
Mesmo padrão. Inclui Pull-In (já prototipado), IMR, decommissioning, tecnologias emergentes, interfaces, FAT/SIT/SAT.

## Sprint 7 — Biblioteca Visual licenciada
**Faz:** pesquisa de imagens com licença verificável (Wikimedia Commons, Flickr CC, agências governamentais, Petrobras quando os termos permitirem); cópia local com crédito; cartões de fonte para o restante; diagramas SVG próprios onde não houver foto; distribuição nos capítulos (FOTO → O QUE OBSERVAR → DIAGRAMA → IMPLICAÇÃO). Registro de licença e data por item.
**Aceite:** nenhuma tag `<img>` apontando para domínio externo; nenhuma imagem quebrada; toda imagem com fonte e licença.

## Sprint 8 — Gamificação e constância
**Faz:** medidor de profundidade, fases com marcos visíveis, badges em SVG, "missão do dia", celebrações discretas, página de progresso redesenhada, "isso não ficou claro" em cada seção.
**Aceite:** próximo marco sempre visível na Home; nenhuma função bloqueada por gamificação; XP não duplica em resposta repetida.

## Sprint 9 — QA completo e release V4.0
**Faz:** checklist do CLAUDE.md seção 23 item a item; auditoria de animações; validação de links externos com data; acessibilidade básica; performance; teste real em celular e notebook pelo Paulo; MATRIZ_ACEITE_V4 preenchida; CHANGELOG fechado; V3 arquivada em `/v3/`.
**Aceite:** todos os itens da matriz com evidência; Definition of Done (D-009) cumprida.

## V4.x — Após o release (ordem sugerida, a validar com uso real da Rafaela)
- V4.1 Aprofundamento Petrobras/Brasil por capítulo (casos públicos, terminologia, especificações públicas).
- V4.2 Novos prompts do backlog (MOC, handover, steering committee, weather window, punch list).
- V4.3 PWA leve (manifest + service worker) para tela inicial e leitura offline.
- V4.4 Novos capítulos por demanda (ex.: logística offshore e readiness como capítulo próprio; HAZID/HAZOP para PM; contratos EPCI e modelos de contratação).
- V4.5 Sincronização de progresso entre dispositivos (avaliar custo/benefício; pode ser desnecessário com exportar/importar).

## Regras do roadmap
- Um sprint pode encolher; não pode pular o aceite.
- Ideias novas entram no BACKLOG, não no sprint corrente, salvo bloqueio.
- Toda sessão termina com ESTADO_ATUAL.md, CHANGELOG.md e BACKLOG.md atualizados, mesmo que o sprint não tenha fechado.
