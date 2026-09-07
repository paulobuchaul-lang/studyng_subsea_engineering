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
| B-011 | P2 | interação | Exportar/importar progresso em JSON | Diagnóstico 3.1 | Sprint 3 |
| B-012 | P2 | QA | Definition of Done com teste em dispositivo real (D-009) | Diagnóstico 3.5 | Sprint 9 |
| B-013 | P2 | técnico | Consolidar ARQUITETURA_MESTRE_V4 (corrigir seção 16 duplicada, referências a V2) | Diagnóstico 3.5 | Sprint 2 |
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
| B-026 | P2 | didática | Reavaliar a ementa de 24 capítulos e sua ordem contra o escopo do CLAUDE.md seção 5 e as seis fases; decidir se há capítulos a fundir, dividir ou criar | D-013 | Sprint 2 |
| B-027 | P2 | técnico | Extração dos capítulos V3 para Markdown estruturado; revisão manual dos blocos irregulares | D-013 | Sprint 1 |
| B-028 | concluído | técnico | Reenviar o zip completo da V3 (43 arquivos: HTML, assets/data.js, styles.css, app.js, imagens) ao repositório de trabalho | Sessão 1 | recebido na Sessão 2 |
| B-029 | concluído | técnico | Ativar GitHub Pages em Settings → Pages do repositório (D-004a decidida: público) | Sessão 1 | feito pelo Paulo |
| B-030 | P1 | didática | Reescrever as 4 camadas de profundidade de cada capítulo como blocos com conteúdo próprio e profundidade completa em Técnica/Deep dive (D-016); hoje é um texto corrido único de 534-1202 palavras; rubrica em AUDITORIA_CONTEUDO_DIDATICA_V4.md seção 4 | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-031 | P1 | didática | Reescrever individualmente o campo "why" dos 126 termos do glossário (hoje idêntico em todos) E fechar a cobertura de termos técnicos usados em cada capítulo migrado (D-018, D-019); incremental por lote de capítulos | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-032 | P1 | didática | Revisar quiz do capítulo 17 (distratores "Nada"/"Somente pintura do winch" ainda presentes) e do capítulo 19 (pergunta binária Sim/Não); ampliar checagem de consistência de qualidade entre os 24 capítulos, não só reescrever enunciados | Auditoria Sessão 2 | Sprints 4 a 6 (parte de D-008) |
| B-033 | P1 | Petrobras/Brasil | Registrar data de verificação em todo fato datado (contrato, valor, caso nomeado) nos capítulos 4, 9, 15, 17, 19, 21, 22 (D-017: entra em V4.1, não bloqueia V4.0) | Auditoria Sessão 2 | V4.1 |
| B-034 | P2 | Petrobras/Brasil | Ampliar casos Brasil/Petrobras nos capítulos sem nenhuma menção nacional hoje, priorizando os que têm literatura pública disponível (poços/ANM m05, flow assurance m12, materiais/corrosão m13) | Auditoria Sessão 2 | Sprints 4 a 6 |
| B-035 | P1 | técnico | Corrigir o popover de termo em `assets/app.js`: remover o teto fixo de 18 ocorrências clicáveis por capítulo (hoje trunca silenciosamente) e reconstruir a lógica no build da V4 para marcar todo termo distinto presente no glossário, sem limite artificial; adicionar ao QA um relatório de "termos citados sem entrada de glossário" por capítulo (D-019) | Pedido do Paulo, Sessão 2 | Sprint 1B (QA) e Sprint 2/3 (popover no shell novo) |
| B-036 | fechado sem ação | técnico | Ativar branch protection na `main`. Revertido: o Paulo decidiu não ter nenhuma trava manual recorrente; o Claude assume o fluxo de branch/PR/merge sozinho (D-021) | Pedido do Paulo, Sessão 2 | superado por D-021 |
