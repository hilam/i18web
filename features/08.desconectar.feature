# language:pt

Funcionalidade: Desconexão da aplicação
  Como uma pessoa autenticada na aplicação
  Que precisa desconectar sua conta
  Para ver apenas as opções gerais

Cenário: Desconexão da aplicação
  Dado que o Painel do Usuário está carregado
  Quando a pessoa clicar no link de Desconexão
  Então a aplicação desconecta a pessoa e redireciona para a "homepage"
