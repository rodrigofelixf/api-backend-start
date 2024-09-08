from fastapi.openapi.models import Schema
from joblib import load
import pandas as pd

from app.models.requests.Paciente_Request import PacienteRequest
from app.models.schemas import schemas

from app.models.requests.Paciente_Dto import PacienteDto
from app.utils.utils import converter_para_paciente_request

modeloTreinadoRandomForest = load('app/ml/modelo_treinado.pkl')

def prever_vulnerabilidade(dadosUsuario: schemas.CriarUsuario):

    dados = converter_para_paciente_request(dadosUsuario)

    dados_usuario = pd.DataFrame([dados.model_dump()])


    remover_colunas_nao_treinadas(dados_usuario)

    previsao = modeloTreinadoRandomForest.predict(dados_usuario)


    return bool(previsao[0])



def remover_colunas_nao_treinadas(dados_usuario) :
    dados_usuario = dados_usuario.drop(['nome', 'endereco', 'numero'], axis=1)