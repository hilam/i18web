# language:pt

Funcionalidade: Acompanhamento de indicações
  Como uma pessoa registrada na aplicação
  Que precisa consultar suas indicações de tradução
  Para conhecer o status de suas indicações

Cenário: Consultar as indicações com status
  Dado que o Painel do Usuário está carregado
  Quando o usuários realizou indicações ateriores
  Então a aplicação mostra a lista de indicações
  E o status de cada uma (Priorizando, selecionado, autorizado pelo autor, traduzindo, disponibilizado)
