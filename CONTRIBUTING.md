# Contribute

Opcional, mas fortemente recomendado: instale o poetry (https://python-poetry.org/docs/#installation)

1. Copie o projeto para o seu usuário. Na página do repositório (<https://github.com/hilam/i18web>), use o botão "Fork", no canto superior direito
2. Clone seu repositório na máquina em que for trabalhar (`git clone https://github.com/<seu-usuario-github>/i18web.git`)
3. Localizado na pasta onde o projeto foi clonado, instale as dependências do projeto. Se tiver instalado o poetry rode `poetry install --dev`. Caso contrário, ative seu ambiente virtual e rode os comandos `pip install -r requirements.txt` e `pip install -r requirements_dev.txt`.
4. Crie um "branch" para fazer sua contribuição (`git checkout -b <indicativo>/<nome_do_branch>`). Recomendamos que o branch seja nomeado usando um indicativo ('fix', 'bug', 'feature', 'docs', 'api', 'web', 'scripts', ou outro indicador significativo) seguido de uma barra(/) e do nome_do_branch, a seu critério.
5. Após a edição da contribuição, adicione e comite os arquivos relacionados (por exemplo, `git add README.md`, `git commit -m 'README.md atualizado.'`). Procure ser objetivo na mensagem de commit, para que o revisor entenda "o que foi feito".
6. Envie o branch para seu repositório (por exemplo, `git push origin docs/upgrade_readme`)
7. Visite a página do seu repositório e faça um "Pull request" através do link que o Github vai disponibilizar.
8. Preencha o formulário de Pull request, que será revisado. Ver mais sobre o processo de revisão.

