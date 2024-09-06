from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
from joblib import load

# Supondo que enums.py esteja na pasta app/models
from app.models.enums import Sexo, FaixaEtaria, RacaCor, Grupo, EstadoCivil, Escolaridade, Cidade, Uf

# Carregar o modelo treinado
modelo = load('./model/modelo_treinado.pkl')

# Definir a estrutura dos dados de entrada usando Pydantic
class UserInput(BaseModel):
    nome: str
    sexo: Sexo
    faixa_etaria: FaixaEtaria
    idade: int
    raca_cor: RacaCor
    grupo: Grupo
    renda: float
    estado: EstadoCivil
    escolaridade: Escolaridade
    endereco: str
    numero: int
    bairro: str
    cidade: Cidade
    uf: Uf
    cep: int
    n_moradores: int

router = APIRouter()

@router.post("/prever/")
async def prever_vulnerabilidade(dados: UserInput):
    # Converter dados de entrada para DataFrame
    dados_usuario = pd.DataFrame([dados.dict()])

    dados_usuario = dados_usuario.drop(['nome', 'endereco', 'numero'], axis=1)

    # Fazer a previsão com o modelo
    previsao = modelo.predict(dados_usuario)

    # Interpretar o resultado
    resultado = "Vulnerável" if previsao[0] else "Não Vulnerável"
    return {"previsao": resultado}
