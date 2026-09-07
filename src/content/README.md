# src/content/

Os 24 capítulos em Markdown, extraídos da V3 pelo script `src/scripts/extrair_capitulos.py` (Sprint 1 Parte B, Sessão 3).

## Front-matter

Cada arquivo `mNN.md` começa com YAML: `id`, `n` (posição no curso), `level` (fase/dificuldade herdada da V3), `title`, `subtitle`.

## Seções

Cada capítulo tem estas seções, nesta ordem: **Express** (candidato à camada "5 minutos"), **Corpo técnico** (candidato às camadas "Gerente de Projetos" e "Técnica"), **Painel PM** (Pontos de atenção / Perguntas / Documentos), **Red flags**, **Assistente LLM**, **Mini quiz**, **Aprofundamento** (candidato à camada "Deep dive").

## Comentários `<!-- REESCREVER(...) -->` e `<!-- DIAGRAMA-INTERATIVO-ORIGINAL -->` / `<!-- IMAGEM-HOTLINK-ORIGINAL -->`

A extração não reescreveu conteúdo técnico — apenas reorganizou o que já existia na V3, preservando-o integralmente (ver `AUDITORIA_CONTEUDO_DIDATICA_V4.md` para a comparação de fidelidade). Três tipos de comentário HTML marcam o que os Sprints 4 a 6 precisam resolver:

- `REESCREVER(profundidade)`: a V3 tinha um texto único servindo às quatro camadas de profundidade ao mesmo tempo; D-016 exige conteúdo próprio e completo em cada camada.
- `REESCREVER(quiz)`: distratores triviais ou binários ainda presentes (D-008); falta feedback por opção errada, não só um feedback único pela resposta correta.
- `DIAGRAMA-INTERATIVO-ORIGINAL`: a V3 tinha um diagrama SVG+JS interativo neste ponto (título, motivo pedagógico e etapas preservados no comentário); precisa ser recriado como componente de diagrama do Sprint 2/3, não copiado.
- `IMAGEM-HOTLINK-ORIGINAL`: a V3 tinha uma foto hotlinkada de fornecedor neste ponto (provavelmente quebrada); D-007 decide o tratamento no Sprint 7.

Esses comentários não aparecem no site publicado (são removidos ou ignorados no build) — servem para orientar a reescrita nos Sprints 4 a 6.

## O que NÃO fazer com estes arquivos

Não editar o HTML gerado à mão (não existe HTML gerado ainda; quando existir, via `src/build.py`, a regra do CLAUDE.md 0.4 item 3 vale: editar aqui, nunca no HTML de saída). Não apagar os comentários de reescrita antes de efetivamente reescrever o conteúdo apontado.
