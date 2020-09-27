# language:pt

Funcionalidade: Home page do projeto
  Como uma pessoa navegando na internet
  É necessário apontar um navegador para a "homepage"
  Para ter acesso às funcionalidades da aplicação

Cenário: Acessar a "homepage"
  Dado que o endereço da "homepage" foi apontado
  Quando o navegador apresentar a resposta
  Então é mostrada a página inicial da aplicação

Cenário: Acessar um endereço inexistente
  Dado que um endereço inexistente foi apontado
  Quando o navegador apresentar a resposta
  Então é mostrada a página de endereço não encontrado


Funcionalidade: Indicação de link
  Como uma pessoa navegando na internet
  Que precisa indicar um link
  Para conseguir a tradução do mesmo

Cenário: Indicar link
  Dado que a página inicial está carregada
  Quando escrever o link e confirmar a indicação
  Então o link será armazenado
  E mostrado na página, na lista de indicações


Funcionalidade: Priorização de indicações
  Como uma pessoa navegando na internet
  Que quer aumentar a prioridade de links indicados
  Para que a indicação seja traduzida primeiro

Cenário: Priorizar indicação
  Dado que é mostrada a página inicial
  Quando clicar no botão de priorização, na lista de indicações
  Então a indicação exibirá a quantidade anterior+1 na prioridade do mesmo


Funcionalidade: Consultar indicações por categoria
  Como uma pessoa que navega na internet
  Que precisa ver as indicações por categoria
  Para poder priorizar ou indicar algo não listado

Cenário: Consultar indicações
  Dado que a página de consulta de indicações está carregada
  Quando selecionar uma categoria
  Então a lista de indicações é filtrada e exibida para aquela categoria


Funcionalidade: Registro de Usuário
  Como uma pessoa que navega na internet
  Que precisa registrar-se na aplicação
  Para poder acompanhar suas indicações ou inscrever-se como tradutor

Cenário: Registrar usuário
  Dado que a página de registro está carregada
  Quando preencher os dados requeridos no formulário e confirmar o registro
  Então o sistema envia um e-mail com o link de confirmação de registro

Cenário: Confirmação de registro
  Dado que uma pessoa recebeu o e-mail de confirmação de registro
  Quando a pessoa acessar o link de confirmação presente no e-mail
  Então o seu registro na aplicação é confirmado
  E a aplicação redireciona para o Painel de Usuário
  E exibe abaixo do nome do usuário o selo de registrado


Funcionalidade: Autenticação de usuário
  Como uma pessoa que navega na internet
  Que precisa autenticar-se como usuário
  Para realizar ações só permitidas para usuários registrados

Cenário: Autenticar usuário
  Dado que o formulário de "Login" está carregado
  Quando preencher os dados requeridos no formulário e confirmar o registro
  Então a aplicação redireciona para o Painel do Usuário


Funcionalidade: Acompanhamento de indicações
  Como uma pessoa registrada na aplicação
  Que precisa consultar suas indicações de tradução
  Para conhecer o status de suas indicações

Cenário: Consultar as indicações com status
  Dado que o Painel do Usuário está carregado
  Quando o usuários realizou indicações ateriores
  Então a aplicação mostra a lista de indicações
  E o status de cada uma (Priorizando, selecionado, autorizado pelo autor, traduzindo, disponibilizado)


Funcionalidade: Inscrição para tradutor
  Como uma pessoa registrada na aplicação
  Que precisa voluntariar-se como tradutor
  Para ter acesso às ferramntas de tradução

Cenário: Inscrição para tradutor
  Dado que o Painel do Usuário está carregado
  Quando o botão de inscrição para tradutor for acionado
  Então o sistema envia um e-mail com as condições para tradução
  E um link de confirmação para possibilitar a tradução

Cenário: Confirmação de inscrição para tradutor
  Dado que uma pessoa recebeu o e-mail de confirmação para tradução
  Quando a pessoa acessar o link de confirmação presente no e-mail
  Então a sua inscrição para traduto é confirmada
  E a aplicação redireciona para o Painel de Usuário
  E exibe abaixo do nome do usuário o selo de tradutor


Funcionalidade: Desconexão da aplicação
  Como uma pessoa autenticada na aplicação
  Que precisa desconectar sua conta
  Para ver apenas as opções gerais

Cenário: Desconexão da aplicação
  Dado que o Painel do Usuário está carregado
  Quando a pessoa clicar no link de Desconexão
  Então a aplicação desconecta a pessoa e redireciona para a "homepage"


Funcionalidade: Inclusão de categorias de indicações
  Como um editor
  Que precisa criar categorias de indicações
  Para que as indicações fiquem organizadas em categorias

Cenário: Inclusão de categoria
  Dado que o Painel do Usuário é exibido
  E abaixo do seu nome a aplicação exibe o selo de Editor
  Quando a pessoa clicar no botão de incluir categorias
  Então a aplicação abre uma janela com o formulário de categorias
  E registra as categorias confirmadas


Funcionalidade: Seleção de indicações para tradução
  Como um editor
  Que precisa selecionar uma indicação priorizada
  Para acionar o envio para a plataforma de tradução

Cenário: Seleção de indicação
  Dado que o Painel do Usuário é exibido
  E abaixo do seu nome a aplicação exibe o selo de Editor
  E a lista de indicações priorizadas é exibida
  Quando a pessoa clicar no botão de seleção
  Então a aplicação aciona a tarefa de envio de conteúdo para a plataforma de tradução
  E registra os endereços de tradução na plataforma


Funcionalidade: Auto atribuição numa tradução
  Como um tradutor
  Que precisa atribuir-se uma tradução
  Para receber as orientações por e-mail

Cenário: Atribuição de tradução
  Dado que a lista de traduções selecionadas é exibida no Painel do Usuário
  Quando a pessoa clicar no botão de atribuição
  Então a aplicação manda as orientações para aquela tradução ao e-mail registrado


Funcionalidade: Receber traduções da plataforma de tradução
  Como um editor
  Que precisa trazer o conteúdo traduzido
  Para disponibilizar a tradução na aplicação

Cenário: Seleção de conteúdo
  Dado que o Painel do Usuário é exibido
  E abaixo do seu nome a aplicação exibe o selo de Editor
  E a lista de traduções é exibida
  Quando a pessoa clicar no botão de obter conteúdo traduzido
  Então a aplicação aciona a tarefa de recepção de conteúdo para a plataforma de tradução
  E registra os endereços de tradução na aplicação
  E atualiza o status da indicação para disponibilizado
