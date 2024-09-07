from joblib import load
import pandas as pd

from app.models.requests.Paciente_Dto import PacienteDto

modeloTreinadoRandomForest = load('app/ml/modelo_treinado.pkl')

def prever_vulnerabilidade(dados):

    dados_usuario = pd.DataFrame([dados.model_dump()])


    remover_colunas_nao_treinadas(dados_usuario)

    previsao = modeloTreinadoRandomForest.predict(dados_usuario)


    return bool(previsao[0])



def remover_colunas_nao_treinadas(dados_usuario) :
    dados_usuario = dados_usuario.drop(['nome', 'endereco', 'numero'], axis=1)