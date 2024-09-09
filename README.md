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
- [Docker](https://docs.docker.com/get-started/get-docker/)
- [PostgreSql](https://www.postgresql.org/download/)


## Práticas adotadas

- API REST
- Alguns conceitos do SOLID
- Responses / Response
- Geração automática do Swagger

# Como Executar

- Clonar repositório git
- Navegar ate o projeto:
```bash
$ cd api-backend-start
```

### 1- Instalar e Ativar Ativar o ambiente de desenvolvimento:

```bash
#Instalar ambiente de desenvolvimento
$ python3 -m venv venv

#O Python tem que ser corretamente instalado. 
#Em ambiente Windows baixar a ultima versão do Python pelo Microsfot Store
```

```bash
#Ativar ambiente de deesnvolvimento: 

#Linux
$ source venv/bin/activate

#Windows
$ env\Scripts\activate

## Deve aparecer (venv) no inicio do terminal.
```

### 2 - Instalar as Dependências


 O projeto possui um arquivo requirements.txt com todas as dependências necessárias. Para instalar, execute o seguinte comando no terminal:
```bash
$ pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, como FastAPI, scikit-learn, joblib, entre outras.


### 3 - Subir o banco de dados via Docker
O projeto vai subir via container no docker. Então é preciso instalar o docker nos links de cima.
Ambiente Windows precisa instalar o Docker e o WSL do windows que ja vem dentro do instalardor - logar a conta e deixar aberto. 

Subir o banco via docker-compose.yml: 

```bash
$ docker-compose up --build
```

### 4 - Rodar a Api

Depois de instalar as dependências, você pode rodar a API usando o Uvicorn, que é o servidor ASGI recomendado para FastAPI. Execute o seguinte comando:

```bash
$ uvicorn main:app --reload
```


Isso iniciará a API no modo de desenvolvimento com recarregamento automático (hot reload) no endereço http://127.0.0.1:8000.

O Swagger poderá ser visualizado em http://127.0.0.1:8000/docs


## API Endpoints

Para fazer as requisições HTTP abaixo, foi utilizada a ferramenta [httpie](https://httpie.io):
(Você pode usar o swagger e outros como: Insomnia, postman, etc.)

- Cadastrar Usuario: 
```
$ endpoint -  http://127.0.0.1:8000/v1/api/usuarios/

{
  "nomeCompleto": "string",
  "email": "string",
  "cpf": "string",
  "dataNascimento": "2024-09-09",
  "sexo": "string",
  "rg": "string",
  "idade": 0,
  "nomeMae": "string",
  "telefone": "string",
  "cep": 0,
  "cidade": "string",
  "rua": "string",
  "uf": "string",
  "bairro": "string",
  "numeroEndereco": 0,
  "escolaridade": "string",
  "racaCor": "string",
  "faixaEtaria": "string",
  "estadoCivil": "string",
  "pcd": true,
  "tipoPcd": "string",
  "cursoSuperior": "string",
  "renda": 0,
  "emprego": "string",
  "numeroMoradores": 0,
  "grupo": "string"
}
```
### Retorno:  Ao cadastrar, o endpoint fara a previsão de vulnerabilidade e se tudo der certo retornara o Id, Nome e um Boleano 0 = nao vulneravel, 1 = vulneravel. 


## - todos os dados serão minusculos para poder funcionar. Os imputs padrões esta na pasta app/models/enums.py
