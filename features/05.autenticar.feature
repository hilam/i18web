# language:pt

Funcionalidade: Autenticação de usuário
  Como uma pessoa que navega na internet
  Que precisa autenticar-se como usuário
  Para realizar ações só permitidas para usuários registrados

Cenário: Autenticar usuário
  Dado que o formulário de "Login" está carregado
  Quando preencher os dados requeridos no formulário e confirmar o registro
  Então a aplicação redireciona para o Painel do Usuário
