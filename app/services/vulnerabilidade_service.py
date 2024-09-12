import pandas as pd
from joblib import load
from sklearn.exceptions import NotFittedError

from app.models.schemas import schemas
from app.utils.utils import converter_para_paciente_request

modeloTreinadoRandomForest = load('app/ml/modelo_treinado.pkl')


def prever_vulnerabilidade(dadosUsuario: schemas.CriarUsuario):
    try:
        dados = converter_para_paciente_request(dadosUsuario)

        print(dados)


        dados_usuario = pd.DataFrame([dados.model_dump()])


        colunasRemovidas = remover_colunas_nao_treinadas(dados_usuario)

        print(colunasRemovidas)


        previsao = modeloTreinadoRandomForest.predict(colunasRemovidas)

        return bool(previsao[0])

    except (ValueError, KeyError, NotFittedError) as e:

        print(f"Erro ao tentar prever vulnerabilidade: {e}")
        return None


def remover_colunas_nao_treinadas(dados_usuario: pd.DataFrame) -> pd.DataFrame:
    """
    Remove as colunas que não foram usadas no treinamento do modelo.
    """
    colunas_para_remover = ['nome', 'endereco', 'numero']

    colunas_existentes = [col for col in colunas_para_remover if col in dados_usuario.columns]


    return dados_usuario.drop(columns=colunas_existentes, axis=1)



