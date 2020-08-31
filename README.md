# I18web

Esteira de tradução de conteúdos de links (artigos, páginas).

[![Python Version][python-image]][python-url]
[![FastAPI Version][fastapi-image]][fastapi-url]

## Intro

Projeto para viabilizar uma esteira de tradução de conteúdos de links (artigos, páginas). Os links são incluídos por usuários, cadastrados ou não, que votam nos mesmos, para indicação de prioridade para os tradutores. Se o usuário for cadastrado, pode acompanhar a tradução de suas indicações ou daquelas em que votou. Usando o Transifex como ferramenta de tradução, o conteúdo dos links são baixados e incluídos na plataforma. Lá são traduzidos e revisados. Eventualmente, os textos concluídos são carregados para um site estático, que disponibiliza o conteúdo dos links indicados e atualiza no aplicativo de indicação o estado e a URL do conteúdo já traduzido.

## Arquitetura

### Repositório de dados e API de acesso (API)

Acesso aos dados do banco PostgreSQL, através de uma API REST

### Web App (WEB)

Aplicação para submissão de links, votação para priorização, lista de links submetidos e, quando o conteúdo estiver traduzido, link para a tradução.

### Scripts para o transifex (SCRIPTS)

Baixar, tratar o html, categorizar, enviar os textos para o Transifex, receber os textos traduzidos (transifex-cli), montar a parte estática com as traduções

## Meta

Licensed by MIT License . See [``LICENSE``](LICENSE) for more details.

## Contribute

See [``CONTRIBUTING``](CONTRIBUTING.md) for more details.

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/python-v3.8-blue
[fastapi-image]: https://img.shields.io/badge/fastapi-0.61.0-green
[python-url]: https://www.python.org/downloads/release/python-385/
[fastapi-url]: https://fastapi.tiangolo.com/
[fastsql-url]: https://github.com/mfreeborn/fastapi-sqlalchemy
[python_dotenv-url]: https://github.com/theskumar/python-dotenv
[uvicorn-url]: https://www.uvicorn.org/
[psycopg2-url]: https://www.psycopg.org/
