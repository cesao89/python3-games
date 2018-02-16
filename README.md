# Game with Python 3

Curso de Python 3 da Alura - Parte 1

### Como executar no Python
Executando via bash do Python, o sistema aguarda a interação do usuário para seguir com o fluxo.

```sh
$ python3 code/jogos.py
```

### Como executar no Docker 
Executando via Docker, será necessário informar os cenários via `ENVIROMENTS` do `docker-compose.yml`.

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```