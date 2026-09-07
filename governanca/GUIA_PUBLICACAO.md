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

## 5. Como atualizar a cada sprint (D-021: o Claude cuida do fluxo inteiro)

O Paulo decidiu não configurar nenhuma trava manual no GitHub (nem branch protection, nem PR obrigatório): o custo de operar isso a cada atualização não compensa o ganho, e a alternativa escolhida foi automação sem fricção (D-021). Na prática:

- **Quando é uma sessão do Claude com acesso de push** (o caso normal): o próprio Claude cria a branch, commita, abre o PR, confere se o check `qa-governanca` passou e mergeia para a `main` sozinho. O Paulo não precisa clicar em nada. Se o check falhar, o Claude corrige antes de mergear — nunca força merge com CI vermelho.
- **Se o Paulo quiser subir algo manualmente** (por exemplo, um zip novo recebido fora de uma sessão): pode usar **Add file → Upload files** direto na `main`, sem passo extra de branch/PR. O CI roda do mesmo jeito e sinaliza qualquer problema na aba **Actions**; se algo ficar incompleto, a auditoria de fim de sessão (seção 5a) pega isso na próxima vez que o Claude trabalhar no repositório.

Nenhuma ação em Settings → Branches é necessária.

## 5a. Auditoria de consistência a cada sessão (D-021, substitui a trava manual)

Em vez de uma trava técnica que bloqueia merge, a garantia de qualidade vem de um hábito: toda sessão do Claude que mexe no repositório fecha com uma checagem de consistência antes de reportar a entrega como concluída — não um agendamento à parte, faz parte do encerramento normal do trabalho. A checagem cobre:

- Os 10 documentos de governança existem e estão sem link interno quebrado (o CI já confere isso automaticamente a cada push).
- `CHANGELOG.md` e `ESTADO_ATUAL.md` refletem o que a sessão realmente fez.
- Nenhum item do `BACKLOG.md` ficou esquecido sem classificação ou destino.
- Quando fizer sentido (sessões que tocam referências externas), uma amostra de links externos ainda resolve.

Se alguma sessão encontrar inconsistência deixada por uma sessão anterior, ela corrige e registra em `DECISOES.md`, sem esperar uma auditoria formal agendada.

## 6. Backup no Google Drive

Pasta sugerida: `Subsea Rafaela / Releases / V3.0`, `V4.0-sprint1`, etc. Guardar em cada uma o .zip entregue pelo Claude. Pasta `Subsea Rafaela / Governança` com a cópia corrente dos .md. O GitHub já guarda o histórico de todas as versões; o Drive é redundância.

## 7. Conhecimento do Projeto (Claude)

O que fica no Projeto: apenas os documentos de governança em Markdown. O que NÃO fica: HTML, CSS, JS, imagens. Esses vivem no repositório e o Claude os busca por URL.

Ordem de leitura que o CLAUDE.md impõe: ESTADO_ATUAL → ROADMAP_V4 → DECISOES → BACKLOG → demais.

## 8. Fluxo completo de uma sessão (visão do Paulo)

1. Abrir o Projeto e escrever: "Vamos ao Sprint N" (ou o que precisar).
2. O Claude lê a governança, busca os arquivos correntes no repositório, executa, sobe a mudança (branch, commit, PR, confere o CI, mergeia para a `main`) e reporta o que foi feito.
3. Você testa a URL publicada quando houver sprint com critério de aceite (D-009), e substitui os .md no Projeto pela cópia mais recente de `/governanca/` se estiver usando o Conhecimento do Projeto do Claude.
4. Qualquer ajuste ou ideia vai para o BACKLOG na sessão seguinte, não perde.

Você não precisa subir zip nem clicar em merge — isso é trabalho do Claude (D-021).
