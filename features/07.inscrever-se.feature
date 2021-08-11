# language:pt

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
