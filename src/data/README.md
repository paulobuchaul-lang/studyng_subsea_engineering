# src/data/

Dados de conteúdo da Plataforma Subsea Rafaela, como arquivos JSON independentes ("conteúdo como dados"). Conforme o Sprint 1 do roadmap (`/governanca/ROADMAP_V4.md`).

## Arquivos

- **`glossario.json`** — array com os 126 termos do glossário técnico. Cada item tem `term` (termo), `full` (forma estendida), `definition` (definição), `why` (por que importa), `id` e `category`. Ordenado alfabeticamente por `term`.

- **`prompts.json`** — array com os 28 prompts profissionais prontos para uso (reuniões, fornecedores, documentos técnicos, etc.). Cada item tem `title`, `category`, `text` (o prompt completo) e `href`. Mantido na ordem original da V3.

- **`aliases.json`** — objeto (mapa de string para string) com os apelidos/sinônimos de busca usados para redirecionar termos alternativos ao id correto do glossário (ex.: `"pullin": "m17"`).

- **`biblioteca.json`** — array **vazio** (`[]`) de propósito. Ver seção abaixo.

## Origem dos dados

`glossario.json`, `prompts.json` e `aliases.json` vieram de `assets/data.js` da V3 (objeto `window.SUBSEA_DATA`), extraídos sem alteração de conteúdo — é conversão de formato (JS embutido → JSON separado), não reescrita.

## `biblioteca.json`: vazio propositalmente

Esse dado não existe na V3. Ele será populado no **Sprint 7**, quando as imagens forem licenciadas. Até lá o arquivo fica como array vazio.

Quando populado, cada item de `biblioteca.json` deve seguir este schema:

```json
{
  "id": "string",
  "titulo": "string",
  "categoria": "string",
  "capitulo_relacionado": "string",
  "tipo": "foto | cartao_fonte | diagrama_svg",
  "arquivo_local": "string ou null",
  "fonte_nome": "string",
  "fonte_url": "string",
  "licenca": "string",
  "data_verificacao": "string",
  "o_que_observar": "string",
  "por_que_importa": "string"
}
```

- `tipo` é um dos três valores: `"foto"`, `"cartao_fonte"` ou `"diagrama_svg"`.
- `arquivo_local` pode ser `null` enquanto o arquivo não tiver sido baixado/hospedado localmente.
