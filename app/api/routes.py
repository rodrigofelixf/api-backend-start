from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
from joblib import load
from app.models.enums import Sexo, FaixaEtaria, RacaCor, Grupo, EstadoCivil, Escolaridade, Cidade, Uf


modeloTreinadoRandomForest = load('./model/modelo_treinado.pkl')


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
async def prever_vulnerabilidade_social(dados: UserInput):
    # Converter dados de entrada para DataFrame
    dados_usuario = pd.DataFrame([dados.model_dump()])

    # Remover colunas desnecessárias
    dados_usuario = dados_usuario.drop(['nome', 'endereco', 'numero'], axis=1)

    # Fazer a previsão com o modelo
    previsao = modeloTreinadoRandomForest.predict(dados_usuario)

    # Retornar True ou False diretamente
    return bool(previsao[0])

