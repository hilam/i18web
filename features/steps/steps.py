from behave import given, when, then


@given(u'que o endereço da "homepage" foi apontado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que o endereço da "homepage" foi apontado')


@when(u'o navegador apresentar a resposta')
def step_impl(context):
    raise NotImplementedError(u'STEP: When o navegador apresentar a resposta')


@then(u'é mostrada a página inicial da aplicação')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then é mostrada a página inicial da aplicação')


@given(u'que um endereço inexistente foi apontado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que um endereço inexistente foi apontado')


@then(u'é mostrada a página de endereço não encontrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then é mostrada a página de endereço não encontrado')


@given(u'que a página inicial está carregada')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que a página inicial está carregada')


@when(u'escrever o link e confirmar a indicação')
def step_impl(context):
    raise NotImplementedError(u'STEP: When escrever o link e confirmar a indicação')


@then(u'o link será armazenado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o link será armazenado')


@then(u'mostrado na página, na lista de indicações')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then mostrado na página, na lista de indicações')


@given(u'que é mostrada a página inicial')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que é mostrada a página inicial')


@when(u'clicar no botão de priorização, na lista de indicações')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicar no botão de priorização, na lista de indicações')


@then(u'a indicação exibirá a quantidade anterior+1 na prioridade do mesmo')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a indicação exibirá a quantidade anterior+1 na prioridade do mesmo')


@given(u'que a página de consulta de indicações está carregada')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que a página de consulta de indicações está carregada')


@when(u'selecionar uma categoria')
def step_impl(context):
    raise NotImplementedError(u'STEP: When selecionar uma categoria')


@then(u'a lista de indicações é filtrada e exibida para aquela categoria')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a lista de indicações é filtrada e exibida para aquela categoria')


@given(u'que a página de registro está carregada')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que a página de registro está carregada')


@when(u'preencher os dados requeridos no formulário e confirmar o registro')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When preencher os dados requeridos no formulário e confirmar o registro')


@then(u'o sistema envia um e-mail com o link de confirmação de registro')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then o sistema envia um e-mail com o link de confirmação de registro')


@given(u'que uma pessoa recebeu o e-mail de confirmação de registro')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given que uma pessoa recebeu o e-mail de confirmação de registro')


@when(u'a pessoa acessar o link de confirmação presente no e-mail')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When a pessoa acessar o link de confirmação presente no e-mail')


@then(u'o seu registro na aplicação é confirmado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o seu registro na aplicação é confirmado')


@then(u'a aplicação redireciona para o Painel de Usuário')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a aplicação redireciona para o Painel de Usuário')


@then(u'exibe abaixo do nome do usuário o selo de registrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then exibe abaixo do nome do usuário o selo de registrado')


@given(u'que o formulário de "Login" está carregado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que o formulário de "Login" está carregado')


@then(u'a aplicação redireciona para o Painel do Usuário')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a aplicação redireciona para o Painel do Usuário')


@given(u'que o Painel do Usuário está carregado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que o Painel do Usuário está carregado')


@when(u'o usuários realizou indicações ateriores')
def step_impl(context):
    raise NotImplementedError(u'STEP: When o usuários realizou indicações ateriores')


@then(u'a aplicação mostra a lista de indicações')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a aplicação mostra a lista de indicações')


@then(
    u'o status de cada uma (Priorizando, selecionado, autorizado pelo autor, traduzindo, disponibilizado)')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then o status de cada uma (Priorizando, selecionado, autorizado pelo autor, traduzindo, disponibilizado)')


@when(u'o botão de inscrição para tradutor for acionado')
def step_impl(context):
    raise NotImplementedError(u'STEP: When o botão de inscrição para tradutor for acionado')


@then(u'o sistema envia um e-mail com as condições para tradução')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then o sistema envia um e-mail com as condições para tradução')


@then(u'um link de confirmação para possibilitar a tradução')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then um link de confirmação para possibilitar a tradução')


@given(u'que uma pessoa recebeu o e-mail de confirmação para tradução')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given que uma pessoa recebeu o e-mail de confirmação para tradução')


@then(u'a sua inscrição para traduto é confirmada')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a sua inscrição para traduto é confirmada')


@then(u'exibe abaixo do nome do usuário o selo de tradutor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then exibe abaixo do nome do usuário o selo de tradutor')


@when(u'a pessoa clicar no link de Desconexão')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pessoa clicar no link de Desconexão')


@then(u'a aplicação desconecta a pessoa e redireciona para a "homepage"')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a aplicação desconecta a pessoa e redireciona para a "homepage"')


@given(u'que o Painel do Usuário é exibido')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que o Painel do Usuário é exibido')


@given(u'abaixo do seu nome a aplicação exibe o selo de Editor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given abaixo do seu nome a aplicação exibe o selo de Editor')


@when(u'a pessoa clicar no botão de incluir categorias')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pessoa clicar no botão de incluir categorias')


@then(u'a aplicação abre uma janela com o formulário de categorias')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a aplicação abre uma janela com o formulário de categorias')


@then(u'registra as categorias confirmadas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then registra as categorias confirmadas')


@given(u'a lista de indicações priorizadas é exibida')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a lista de indicações priorizadas é exibida')


@when(u'a pessoa clicar no botão de seleção')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pessoa clicar no botão de seleção')


@then(u'a aplicação aciona a tarefa de envio de conteúdo para a plataforma de tradução')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a aplicação aciona a tarefa de envio de conteúdo para a plataforma de tradução')


@then(u'registra os endereços de tradução na plataforma')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then registra os endereços de tradução na plataforma')


@given(u'que a lista de traduções selecionadas é exibida no Painel do Usuário')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given que a lista de traduções selecionadas é exibida no Painel do Usuário')


@when(u'a pessoa clicar no botão de atribuição')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pessoa clicar no botão de atribuição')


@then(u'a aplicação manda as orientações para aquela tradução ao e-mail registrado')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a aplicação manda as orientações para aquela tradução ao e-mail registrado')


@given(u'a lista de traduções é exibida')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a lista de traduções é exibida')


@when(u'a pessoa clicar no botão de obter conteúdo traduzido')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pessoa clicar no botão de obter conteúdo traduzido')


@then(u'a aplicação aciona a tarefa de recepção de conteúdo para a plataforma de tradução')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a aplicação aciona a tarefa de recepção de conteúdo para a plataforma de tradução')


@then(u'registra os endereços de tradução na aplicação')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then registra os endereços de tradução na aplicação')


@then(u'atualiza o status da indicação para disponibilizado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then atualiza o status da indicação para disponibilizado')
