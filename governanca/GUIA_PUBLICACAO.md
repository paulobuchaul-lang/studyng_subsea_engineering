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

Válido para a primeira publicação, antes da proteção de branch da seção 5a existir.

1. Criar conta em github.com (gratuita). Escolha um nome de usuário que você aceite ver na URL, pois ela será `https://SEU_USUARIO.github.io/NOME_DO_REPO/`.
2. Clicar em **New repository**. Nome sugerido: `subsea-rafaela`. Visibilidade: **Public**. Marcar "Add a README file". Criar.
3. Na página do repositório, clicar em **Add file → Upload files**. Arrastar para a área de upload o CONTEÚDO da pasta `Portal_Subsea_Rafaela_V3_COMPLETO` (as pastas `assets/`, `capitulos/`, `documentacao/` e os arquivos `.html`), não a pasta em si. O navegador aceita arrastar pastas inteiras. Escrever "V3 inicial" na mensagem e clicar em **Commit changes**.
4. Ir em **Settings → Pages**. Em "Build and deployment", Source: **Deploy from a branch**; Branch: **main**, pasta **/ (root)**. Salvar.
5. Aguardar 1 a 3 minutos. A própria página Settings → Pages mostra a URL quando estiver no ar.
6. Abrir a URL no celular e no notebook. Testar: Home → capítulo 17 → glossário → voltar; marcar "estudado"; recarregar e ver se o XP permaneceu. Registrar o resultado no ESTADO_ATUAL.md.
7. Copiar a URL e o endereço do repositório para o ESTADO_ATUAL.md. A partir daí o Claude busca os arquivos correntes diretamente do repositório em toda sessão.

Se a URL abrir mas sem estilo, o motivo mais comum é a pasta `assets/` ter sido enviada dentro de uma subpasta. O caminho correto é `https://.../subsea-rafaela/assets/styles.css`.

## 5. Como atualizar a cada sprint (com PR obrigatório na main — D-020)

A `main` agora exige pull request e o check `qa-governanca` passando antes de qualquer merge (seção 5a). Isso não exige linha de comando — o próprio GitHub oferece o caminho pela tela de upload:

1. Extrai o zip que o Claude entregou.
2. No repositório, **Add file → Upload files**, arrasta o conteúdo. Arquivos com o mesmo nome são substituídos; arquivos novos são adicionados.
3. Escreve a versão na mensagem de commit (por exemplo "V4.0-sprint3").
4. Logo abaixo da mensagem, o GitHub mostra duas opções: "Commit directly to the main branch" (vai aparecer bloqueada ou avisando que a branch é protegida) e **"Create a new branch for this commit and start a pull request"**. Selecione a segunda — pode aceitar o nome de branch sugerido — e clique em **Propose changes**.
5. Você cai na tela de abrir PR. Revise o resumo do que mudou e clique em **Create pull request**.
6. Aguarde. Na parte de baixo do PR aparece o check `qa-governanca` rodando (1-2 minutos). Se ficar verde, o botão **Merge pull request** habilita — clique nele e depois em **Confirm merge**.
7. Se o check ficar vermelho, não force o merge: clique em "Details" ao lado do check para ver o que falhou (documento de governança faltando, link quebrado, ou CHANGELOG/ESTADO_ATUAL não atualizado). O mais simples nesse caso é colar o erro numa sessão do Claude e pedir a correção antes de tentar mergear de novo.
8. Depois do merge, teste no celular e no notebook conforme o critério de aceite do sprint. A tela de PR mergeado oferece um botão **Delete branch** — pode apagar a branch temporária, o histórico fica preservado no PR.

Arquivos removidos numa versão nova não somem sozinhos pelo upload. Quando um sprint remover arquivos, o CHANGELOG dirá quais; você os apaga pela mesma lógica (branch → PR → merge), abrindo o arquivo e usando o ícone de lixeira.

## 5a. Proteção da branch main (já configurada — como foi feita)

O repositório roda uma checagem automática (GitHub Actions, `qa-governanca`) a cada mudança: confere se os documentos de governança existem, se não há link quebrado entre eles, e se toda mudança de conteúdo ou código veio acompanhada de atualização do CHANGELOG ou do ESTADO_ATUAL. Configuração feita em **Settings → Branches → Add branch protection rule**, branch pattern `main`, com **Require status checks to pass before merging** (check `qa-governanca`) e **Require a pull request before merging** ambos marcados (decisão do Paulo, D-020: preferiu rigor a conveniência de upload direto).

Consequência prática, já refletida na seção 5 acima: não é mais possível commitar direto na `main` pela tela simples de upload. Todo upload passa a virar uma branch temporária + PR, com 2 a 3 cliques a mais, mas nada incompleto entra na `main` sem o CI aprovar e sem você (ou o Claude) confirmar o merge.

## 6. Backup no Google Drive

Pasta sugerida: `Subsea Rafaela / Releases / V3.0`, `V4.0-sprint1`, etc. Guardar em cada uma o .zip entregue pelo Claude. Pasta `Subsea Rafaela / Governança` com a cópia corrente dos .md. O GitHub já guarda o histórico de todas as versões; o Drive é redundância.

## 7. Conhecimento do Projeto (Claude)

O que fica no Projeto: apenas os documentos de governança em Markdown. O que NÃO fica: HTML, CSS, JS, imagens. Esses vivem no repositório e o Claude os busca por URL.

Ordem de leitura que o CLAUDE.md impõe: ESTADO_ATUAL → ROADMAP_V4 → DECISOES → BACKLOG → demais.

## 8. Fluxo completo de uma sessão (visão do Paulo)

1. Abrir o Projeto e escrever: "Vamos ao Sprint N" (ou o que precisar).
2. O Claude lê a governança, busca os arquivos correntes no repositório, executa e entrega: .zip da versão + governança atualizada.
3. Você sobe o zip no GitHub pelo fluxo de branch + PR da seção 5, confirma que o check `qa-governanca` passou, mergeia, testa, e substitui os .md no Projeto.
4. Qualquer ajuste ou ideia vai para o BACKLOG na sessão seguinte, não perde.

Quando é uma sessão do Claude com acesso de push ao repositório (como esta), o próprio Claude abre a branch e o PR; o passo 3 vira "você confirma o merge do PR depois de ver o check verde", não "você sobe o zip".
