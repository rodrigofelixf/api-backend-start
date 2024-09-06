# api-backend-start
<h1 align="center">
  Api Backend Projeto Start+ IA
</h1>

<p align="center">
 <a href="https://www.linkedin.com/in/rodrigofelixf/" target="_blank">
    <img src="https://img.shields.io/static/v1?label=Linkedin&message=@rodrigofelixf&color=8257E5&labelColor=000000" alt="@rodrigofelixf" />
</a>
 <img src="https://img.shields.io/static/v1?label=Tipo&message=Projeto&color=8257E5&labelColor=000000" alt="Projeto" />
</p>

# API de Previsão de Vulnerabilidade Social

Esta API utiliza um modelo de machine learning treinado para prever se uma pessoa é socialmente vulnerável ou não, com base em dados fornecidos, como sexo, faixa etária, renda, estado civil, escolaridade, e outros fatores.

Referência do projeto [Rede Cidadã](https://www.redecidada.org.br).

## Tecnologias
 
- [Python](https://www.python.org/)
- [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Swagger](https://swagger.io/docs/)


## Práticas adotadas

- API REST
- Alguns conceitos do SOLID
- Responses / Response
- Geração automática do Swagger

## Como Executar

- Clonar repositório git
- Navegar ate o projeto:
```bash
$ cd api-backend-start
```
- Executar a aplicação:
- Instalar as Dependências

1 - O projeto possui um arquivo requirements.txt com todas as dependências necessárias. Para instalar, execute o seguinte comando no terminal:
```bash
$ pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, como FastAPI, scikit-learn, joblib, entre outras.

2 - Rodar a API

Depois de instalar as dependências, você pode rodar a API usando o Uvicorn, que é o servidor ASGI recomendado para FastAPI. Execute o seguinte comando:

```bash
$ uvicorn main:app --reload
```


Isso iniciará a API no modo de desenvolvimento com recarregamento automático (hot reload) no endereço http://127.0.0.1:8000.

O Swagger poderá ser visualizado em http://127.0.0.1:8000/docs


## API Endpoints

Para fazer as requisições HTTP abaixo, foi utilizada a ferramenta [httpie](https://httpie.io):
(Você pode usar o swagger e outros como: Insomnia, postman, etc.)

- Prever Vulerabilidade
```
$ http POST :<Porta>/prever/>

{
  "nome": "string",
  "sexo": "feminino",
  "faixa_etaria": "0 a 19 anos",
  "idade": 0,
  "raca_cor": "amarela",
  "grupo": "caminhoneiros",
  "renda": 0,
  "estado": "casado",
  "escolaridade": "curso tecnico / tecnologo",
  "endereco": "string",
  "numero": 0,
  "bairro": "string",
  "cidade": "abreu e lima",
  "uf": "pe",
  "cep": 0,
  "n_moradores": 0
}
```

## - todos os dados tem que ser em minusculo. Os imputs padrões esta na pasta app/model/enums.py