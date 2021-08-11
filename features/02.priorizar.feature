# language:pt

Funcionalidade: Priorização de indicações
  Como uma pessoa navegando na internet
  Que quer aumentar a prioridade de links indicados
  Para que a indicação seja traduzida primeiro

Cenário: Priorizar indicação
  Dado que é mostrada a página inicial
  Quando clicar no botão de priorização, na lista de indicações
  Então a indicação exibirá a quantidade anterior+1 na prioridade do mesmo
