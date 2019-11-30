# Dividendus

Este é um app para organização de ações, à princípio, no Brasil e Estados Unidos.

- api
  - Python 3.8
- web
  - React 16.12.0
- mobile
  - React-native 0.61.5
- Banco de dados
  - PostgreSQL 12

### Como rodar

#### Pre requisitos

- Docker
- Docker-compose

Dentor do projeto `dividendus`, rodar os comandos:
```shell script
$ cd docker
$ docker-compose up
```

O comando acima inicializará o banco de dados, a api e o módulo web.
