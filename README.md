# Plataforma Subsea Rafaela

Plataforma digital de aprendizagem em Engenharia Submarina aplicada à gestão de projetos offshore, desenvolvida para uso pessoal de estudo e consulta técnica.

O produto funciona simultaneamente como curso estruturado, referência técnica de consulta imediata, ferramenta de apoio ao trabalho diário, biblioteca visual de equipamentos e operações, biblioteca de prompts profissionais para uso de LLMs e ambiente de aprendizagem gamificado. Todo o conteúdo é educacional e baseado em fontes públicas; nenhuma informação confidencial de contrato ou de empresa é publicada.

## Status atual

Projeto em redesign (V4.0). Ainda não há site publicado. Ver `/governanca/ESTADO_ATUAL.md` para o estado detalhado, decisões pendentes e o que falta para a primeira publicação.

## Estrutura do repositório

```
/governanca/       documentos de governança do projeto (fonte de verdade dos requisitos e do processo)
/src/content/       capítulos em Markdown (a popular no Sprint 1)
/src/data/          glossário, prompts, aliases e biblioteca visual em JSON (a popular no Sprint 1)
/src/templates/     templates de página do build (a popular após decisão de pipeline)
```

A raiz do repositório é o site publicado por GitHub Pages quando a hospedagem for ativada.

## Governança do projeto

Este repositório segue um protocolo de continuidade entre sessões descrito em `/governanca/CLAUDE.md`. Antes de qualquer mudança no produto, a ordem de leitura é:

1. `governanca/ESTADO_ATUAL.md` — onde o projeto está agora.
2. `governanca/ROADMAP_V4.md` — o sprint corrente e seu critério de aceite.
3. `governanca/DECISOES.md` — decisões vigentes e pendentes.
4. `governanca/BACKLOG.md` — pendências classificadas.
5. `governanca/DESIGN_SYSTEM_V4.md` — tokens e componentes visuais.
6. `governanca/DIAGNOSTICO_V3.md` e `governanca/CHANGELOG.md` — histórico e o que não pode regredir.
7. `governanca/GUIA_PUBLICACAO.md` — como publicar e atualizar o site.

## Licença de conteúdo

Conteúdo educacional de uso pessoal. Nenhuma imagem é publicada por hotlink de terceiros; imagens seguem a política de licenciamento registrada em `governanca/DECISOES.md` (D-007).
