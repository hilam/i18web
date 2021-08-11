# language:pt

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
