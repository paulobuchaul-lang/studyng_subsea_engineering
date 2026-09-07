# BACKLOG.md — Pendências e oportunidades

Classificação: conteúdo · didática · visual · interação · técnico · Petrobras/Brasil · tecnologia emergente · UX · gamificação · LLM · performance · QA.
Prioridade: P1 (bloqueia release) · P2 (V4.0) · P3 (V4.x) · P4 (avaliar).
Itens promovidos a sprint saem daqui e entram no ROADMAP; itens concluídos vão para o CHANGELOG.

| ID | Prioridade | Classe | Item | Origem | Destino previsto |
|---|---|---|---|---|---|
| B-001 | concluído | técnico | Obter zip completo da V3 (recebido em 06/09/2026) | Sessão 0 | feito |
| B-002 | P1 | técnico | Publicar como site estático (D-004) | Sessão 0 | Sprint 1 |
| B-003 | P1 | técnico | Remover ponte window.name após hospedagem HTTP | Sessão 0 | Sprint 1 |
| B-004 | P2 | UX | Home: reduzir 24 pontos de entrada para um fluxo (Continuar · Hoje eu preciso · Trilha · Consultar) | Diagnóstico 3.3 | Sprint 2 |
| B-005 | P2 | UX | Bottom tab bar no mobile; sidebar no desktop; "Neste capítulo" | Diagnóstico 3.3 | Sprint 2 |
| B-006 | P2 | visual | Substituir ícones Unicode por SVG | Diagnóstico 3.1 | Sprint 2 |
| B-007 | P2 | didática | Camadas de profundidade como controle segmentado (5 min · Gerente · Técnica · Deep dive) | Diagnóstico 3.3 | Sprint 2/4 |
| B-008 | P2 | didática | Reescrever distratores triviais das 72 questões; feedback por opção (D-008) | Diagnóstico 3.3 | Sprints 4 a 6 |
| B-009 | P2 | visual | Biblioteca Visual com licenciamento (D-007) | Diagnóstico 3.2 | Sprint 7 |
| B-010 | P2 | gamificação | Medidor de profundidade; próximo marco visível; badges SVG | Diagnóstico 3.3 | Sprint 8 |
| B-011 | concluído | interação | Exportar/importar progresso em JSON | Diagnóstico 3.1 | feito na Sessão 6 (Sprint 3) |
| B-012 | P2 | QA | Definition of Done com teste em dispositivo real (D-009) | Diagnóstico 3.5 | Sprint 9 |
| B-013 | concluído | técnico | Consolidar ARQUITETURA_MESTRE_V4 (corrigir seção 16 duplicada, referências a V2) | Diagnóstico 3.5 | feito na Sessão 5 |
| B-014 | P2 | conteúdo | "Para onde isso está indo" por capítulo, não só no 22 | Diagnóstico 3.4 | Sprints 4 a 6 |
| B-015 | P3 | didática | Exemplos de ordem de grandeza (cargas, profundidades, durações) marcados como ilustrativos | Diagnóstico 3.4 | V4.1 |
| B-016 | P3 | Petrobras/Brasil | Ampliar casos públicos por capítulo (Búzios, Mero, Sépia, Albacora, descomissionamento) com data de verificação | CLAUDE.md seção 8 | V4.1 |
| B-017 | P3 | LLM | Novos prompts: MOC, handover, steering committee, weather window, punch list, comunicação com cliente | ARQUITETURA seção 12 | V4.2 |
| B-018 | P3 | técnico | PWA leve (manifest, service worker, tela inicial, offline do texto) | Sessão 0 | V4.3 |
| B-019 | P3 | UX | "Isso não ficou claro" por seção (mailto ou formulário) | Sessão 0 | Sprint 8 |
| B-020 | P3 | gamificação | "Missão do dia" (10 a 15 min) sem streak compulsivo | Sessão 0 | Sprint 8 |
| B-021 | P3 | conteúdo | Capítulos candidatos: logística offshore e readiness; HAZID/HAZOP para PM; modelos de contratação EPCI | ARQUITETURA seção 3 | V4.4 |
| B-022 | P4 | técnico | Sincronização de progresso entre dispositivos | Sessão 0 | V4.5 (avaliar) |
| B-023 | P3 | QA | Validação periódica de links externos com data (script) | CLAUDE.md seção 9 | Sprint 9 e recorrente |
| B-024 | P3 | performance | Lazy load de mídia; fontes com fallback local | ARQUITETURA seção 14 | Sprint 2 |
| B-025 | P4 | tecnologia emergente | Revisar classificação de maturidade (all-electric, TCP, resident ROV, digital twin) a cada 6 meses | ARQUITETURA seção 13 | recorrente |
| B-026 | P1 | didática | Reavaliar a ementa de 24 capítulos e sua ordem contra o escopo do CLAUDE.md seção 5 e as seis fases; decidir se há capítulos a fundir, dividir ou criar. Bloqueia o mapeamento real da Trilha/medidor de profundidade da Home (hoje provisório, D-024) | D-013 | Sprints 4 a 6 (é decisão de currículo, cabe junto da reescrita de conteúdo, não como plumbing de hub — não resolvida no Sprint 3) |
| B-027 | concluído | técnico | Extração dos capítulos V3 para Markdown estruturado (src/scripts/extrair_capitulos.py); fidelidade verificada por contagem de palavras, sem perda | D-013 | feito na Sessão 3 |
| B-028 | concluído | técnico | Reenviar o zip completo da V3 (43 arquivos: HTML, assets/data.js, styles.css, app.js, imagens) ao repositório de trabalho | Sessão 1 | recebido na Sessão 2 |
| B-029 | concluído | técnico | Ativar GitHub Pages em Settings → Pages do repositório (D-004a decidida: público) | Sessão 1 | feito pelo Paulo |
| B-030 | P1 | didática | Reescrever as 4 camadas de profundidade de cada capítulo como blocos com conteúdo próprio e profundidade completa em Técnica/Deep dive (D-016); hoje é um texto corrido único de 534-1202 palavras; rubrica em AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 4 | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-031 | P1 | didática | Reescrever individualmente o campo "why" dos 126 termos do glossário (hoje idêntico em todos) E fechar a cobertura de termos técnicos usados em cada capítulo migrado (D-018, D-019); incremental por lote de capítulos | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-032 | P1 | didática | Revisar quiz do capítulo 17 (distratores "Nada"/"Somente pintura do winch" ainda presentes) e do capítulo 19 (pergunta binária Sim/Não); ampliar checagem de consistência de qualidade entre os 24 capítulos, não só reescrever enunciados | Auditoria Sessão 2 | Sprints 4 a 6 (parte de D-008) |
| B-033 | P1 | Petrobras/Brasil | Registrar data de verificação em todo fato datado (contrato, valor, caso nomeado) nos capítulos 4, 9, 15, 17, 19, 21, 22 (D-017: entra em V4.1, não bloqueia V4.0) | Auditoria Sessão 2 | V4.1 |
| B-034 | P2 | Petrobras/Brasil | Ampliar casos Brasil/Petrobras nos capítulos sem nenhuma menção nacional hoje, priorizando os que têm literatura pública disponível (poços/ANM m05, flow assurance m12, materiais/corrosão m13) | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-035 | concluído | técnico | Corrigir o popover de termo: `src/build.py` marca todo termo distinto do glossário presente no texto de cada capítulo, sem limite artificial (testado via Playwright: m17 tem 43 termos marcados, mais que o teto de 18 da V3); `src/scripts/qa.py` cataloga heuristicamente siglas sem entrada de glossário por capítulo (167 candidatas encontradas, alimenta B-031) | Pedido do Paulo, Sessão 2 | feito na Sessão 3 |
| B-036 | fechado sem ação | técnico | Ativar branch protection na `main`. Revertido: o Paulo decidiu não ter nenhuma trava manual recorrente; o Claude assume o fluxo de branch/PR/merge sozinho (D-021) | Pedido do Paulo, Sessão 2 | superado por D-021 |
| B-037 | P3 | QA | Adicionar `src/scripts/test_e2e.py` (Playwright/Chromium) ao CI quando o custo de configurar o browser no runner do GitHub Actions compensar; hoje roda manualmente a cada sessão de trabalho, não automatizado no CI | Sessão 3 | avaliar em sprint futuro |
| B-038 | P3 | performance | Baixar/hospedar localmente as fontes Inter e Sora em `assets/fonts/` (DESIGN_SYSTEM_V4.md seção 3.2 exige cópia local para funcionar offline); sem acesso à internet nesta sessão para baixar, o CSS já declara `font-family: "Inter", "Sora", system-ui` mas cai no fallback do sistema até os arquivos existirem | Sessão 5 (Sprint 2) | quando houver acesso de rede numa sessão futura |
| B-039 | P2 | UX | Ajustar detalhes visuais do protótipo do Sprint 2 apontados pelo Paulo após ver o site publicado (D-012: ajustes entram aqui antes do Sprint 3) | Sessão 5 (Sprint 2) | aguardando feedback do Paulo |
| B-040 | P1 | conteúdo/didática | Revisar todo o conteúdo extraído no Sprint 1 pelo critério mais rígido de uso de inglês (D-025): traduzir por default tudo que não tem uso oral real comprovado em reuniões no Brasil (ex.: "transfer load"→transferência de carga, "hydraulic power"→força/potência hidráulica, nomes de etapa de tabela inteiros em inglês), mantendo só sobreviventes legítimos (pull-in, riser, jumper, ROV etc.) com glossário obrigatório (D-019). Evidência concreta: tabela "Sequência didática de second-end pull-in" do m17. Amplia B-030/B-031, não é item isolado — mesmo critério se aplica aos 24 capítulos durante a reescrita | Pedido do Paulo, Sessão 5 | Sprints 4 a 6 (m17 primeiro, por já ter evidência levantada) |
| B-041 | concluído | técnico | Corrigir falso positivo em `src/scripts/qa.py`: o checador de links locais lia `href="..."` no arquivo inteiro, inclusive dentro de `<script>` que monta HTML por concatenação de string (ex.: `'<a href="capitulos/' + id + '.html">'` em `search.html`), reportando link quebrado que não existe no HTML renderizado | Achado durante o Sprint 3, Sessão 6 | feito na Sessão 6 (blocos `<script>` agora são removidos antes da checagem) |
