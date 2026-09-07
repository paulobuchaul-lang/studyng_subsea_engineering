# GUIA_PUBLICACAO.md — Como publicar, atualizar e fazer backup

Este guia é operacional. É para o Paulo executar, sem linha de comando, apenas com o navegador.

## 1. Por que não usar o Google Drive como site

O Drive é um armazenamento de arquivos. Ao abrir um HTML pelo Drive, ele mostra uma pré-visualização isolada: o CSS em `assets/` não carrega, o JavaScript não roda, e os links para outras páginas não funcionam. Isso vale para notebook e, com mais força, para celular. Foi a causa do problema "o CSS não funcionou".

O Drive continua útil para uma coisa: guardar o .zip de cada versão publicada e os documentos de governança. Nunca como meio de uso.

## 2. GitHub Pages: o que é, quanto custa, quem acessa

GitHub Pages hospeda sites estáticos gratuitamente a partir de um repositório público, em contas gratuitas. Para publicar a partir de repositório privado é necessário plano pago (GitHub Pro); e uma página privada, acessível só com login, exige organização com GitHub Enterprise Cloud. Ou seja: na conta gratuita, o repositório e o site são públicos. (Verificado em 06/09/2026 na documentação do GitHub; limites podem mudar.)

Quem acessa: qualquer pessoa com o link, sem conta, em qualquer dispositivo. A Rafaela não precisa de conta GitHub; ela só recebe a URL e pode adicionar à tela inicial do celular. O link não é divulgado por nenhum índice do GitHub, mas também não é secreto: quem tiver a URL abre.

Limites relevantes: repositório de até 1 GB e tráfego de 100 GB por mês, muito acima do que este projeto usa.

Regra de conteúdo: nada confidencial de Petrobras, contrato ou pessoal no site. O conteúdo é educacional e feito de fontes públicas.

## 3. Alternativa com login (se D-004a = B)

Cloudflare Pages publica de um repositório privado do GitHub e permite proteger o site com Cloudflare Access (login por e-mail com código), gratuito para um número pequeno de usuários. Exige duas contas (GitHub e Cloudflare) e uns 20 minutos a mais de configuração. Só vale a pena se a exposição pública for um incômodo real.

## 4. Passo a passo: publicar a V3 hoje no GitHub Pages

1. Criar conta em github.com (gratuita). Escolha um nome de usuário que você aceite ver na URL, pois ela será `https://SEU_USUARIO.github.io/NOME_DO_REPO/`.
2. Clicar em **New repository**. Nome sugerido: `subsea-rafaela`. Visibilidade: **Public**. Marcar "Add a README file". Criar.
3. Na página do repositório, clicar em **Add file → Upload files**. Arrastar para a área de upload o CONTEÚDO da pasta `Portal_Subsea_Rafaela_V3_COMPLETO` (as pastas `assets/`, `capitulos/`, `documentacao/` e os arquivos `.html`), não a pasta em si. O navegador aceita arrastar pastas inteiras. Escrever "V3 inicial" na mensagem e clicar em **Commit changes**.
4. Ir em **Settings → Pages**. Em "Build and deployment", Source: **Deploy from a branch**; Branch: **main**, pasta **/ (root)**. Salvar.
5. Aguardar 1 a 3 minutos. A própria página Settings → Pages mostra a URL quando estiver no ar.
6. Abrir a URL no celular e no notebook. Testar: Home → capítulo 17 → glossário → voltar; marcar "estudado"; recarregar e ver se o XP permaneceu. Registrar o resultado no ESTADO_ATUAL.md.
7. Copiar a URL e o endereço do repositório para o ESTADO_ATUAL.md. A partir daí o Claude busca os arquivos correntes diretamente do repositório em toda sessão.

Se a URL abrir mas sem estilo, o motivo mais comum é a pasta `assets/` ter sido enviada dentro de uma subpasta. O caminho correto é `https://.../subsea-rafaela/assets/styles.css`.

## 5. Como atualizar a cada sprint

O Claude entrega um .zip com a versão nova. Você:

1. Extrai o zip.
2. No repositório, **Add file → Upload files**, arrasta o conteúdo. Arquivos com o mesmo nome são substituídos; arquivos novos são adicionados.
3. Escreve a versão na mensagem (por exemplo "V4.0-sprint3") e confirma.
4. Aguarda a publicação e testa no celular e no notebook conforme o critério de aceite do sprint.

Arquivos removidos numa versão nova não somem sozinhos pelo upload. Quando um sprint remover arquivos, o CHANGELOG dirá quais; você os apaga pelo próprio GitHub (abrir o arquivo → ícone de lixeira → confirmar).

## 6. Backup no Google Drive

Pasta sugerida: `Subsea Rafaela / Releases / V3.0`, `V4.0-sprint1`, etc. Guardar em cada uma o .zip entregue pelo Claude. Pasta `Subsea Rafaela / Governança` com a cópia corrente dos .md. O GitHub já guarda o histórico de todas as versões; o Drive é redundância.

## 7. Conhecimento do Projeto (Claude)

O que fica no Projeto: apenas os documentos de governança em Markdown. O que NÃO fica: HTML, CSS, JS, imagens. Esses vivem no repositório e o Claude os busca por URL.

Ordem de leitura que o CLAUDE.md impõe: ESTADO_ATUAL → ROADMAP_V4 → DECISOES → BACKLOG → demais.

## 8. Fluxo completo de uma sessão (visão do Paulo)

1. Abrir o Projeto e escrever: "Vamos ao Sprint N" (ou o que precisar).
2. O Claude lê a governança, busca os arquivos correntes no repositório, executa e entrega: .zip da versão + governança atualizada.
3. Você sobe o zip no GitHub, testa, e substitui os .md no Projeto.
4. Qualquer ajuste ou ideia vai para o BACKLOG na sessão seguinte, não perde.
