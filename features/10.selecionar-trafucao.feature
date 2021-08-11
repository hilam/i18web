# language:pt

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
