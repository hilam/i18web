# language:pt

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
