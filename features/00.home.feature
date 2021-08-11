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