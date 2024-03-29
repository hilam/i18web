# I18web

Esteira de tradução de conteúdos de links (artigos, páginas).

[![Python Version][python-image]][python-url]
[![FastAPI Version][fastapi-image]][fastapi-url]

## Introdução

Projeto para viabilizar uma esteira de tradução de conteúdos de links (artigos, páginas, blog posts, etc). Num aplicativo web, os links são indicados por usuários, anônimos ou registrados, que votam nos links para indicar prioridades para os tradutores. O usuário registrado pode acompanhar a tradução de suas indicações ou daquelas em que votou. O conteúdo dos links indicados e priorizados são baixados e incluídos na plataforma de tradução, onde são traduzidos e revisados. Os textos traduzidos são carregados para o aplicativo web, que disponibiliza o conteúdo traduzido, e atualiza os links indicados incluindo o endereço do conteúdo traduzido.

[![Esboço do projeto][mindmap-image]][mindmap-image]

## Arquitetura

### Repositório de dados e API de acesso (API)

* Acesso ao banco de dados, através de uma API REST

* Baixar conteúdo, tratar o html, categorizar, enviar os textos para a plataforma de tradução, receber textos traduzidos, montar páginas de tradução

### Web App (WEB)

* Aplicação para submissão de links, votação para priorização, lista de links submetidos e, quando o conteúdo estiver traduzido, link para a tradução.

### Roadmap

* Planejamento de releases

Detalhes em [``Roadmap API``](roadmap_api.md) e [``Roadmap WebApp``](roadmap_web.md). 

[![Roadmap do projeto][mindmap-roadmap-image]][mindmap-roadmap-image]

## Meta

Licensed by MIT License . See [``LICENSE``](LICENSE) for more details.

## Contribute

See [``CONTRIBUTING``](CONTRIBUTING.md) for more details.

<!-- Markdown link & img dfn's -->
[mindmap-image]: https://github.com/hilam/i18web/blob/main/docs/images/I18Web.png
[mindmap-roadmap-image]: https://github.com/hilam/i18web/blob/main/docs/images/I18Web_roadmap.png
[python-image]: https://img.shields.io/badge/python-v3.8+-blue
[fastapi-image]: https://img.shields.io/badge/fastapi-0.68.0-green
[python-url]: https://www.python.org/downloads/release/python-385/
[fastapi-url]: https://fastapi.tiangolo.com/
[fastsql-url]: https://github.com/mfreeborn/fastapi-sqlalchemy
[python_dotenv-url]: https://github.com/theskumar/python-dotenv
[uvicorn-url]: https://www.uvicorn.org/
[psycopg2-url]: https://www.psycopg.org/
