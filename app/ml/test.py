import pandas as pd
import joblib

# Carregar o modelo treinado (que inclui o pré-processador e o modelo)
pipeline = joblib.load('modelo_treinado.pkl')

# Dados de entrada para previsão
dados_entrada = pd.DataFrame([{
    "nome": "rodrigo felix",
    "sexo": "masculino",
    "faixa_etaria": "0 a 19 anos",
    "idade": 25,
    "raca_cor": "amarela",
    "grupo": "caminhoneiros",
    "renda": 35000,
    "estado": "casado",
    "escolaridade": "curso tecnico / tecnologo",
    "endereco": "rua d",
    "numero": 2,
    "bairro": "fundao",
    "cidade": "abreu e lima",
    "uf": "PE",
    "cep": 52160170,
    "n_moradores": 40
}])

# Fazer a previsão com o pipeline
previsao = pipeline.predict(dados_entrada)

# Exibir o resultado
print("Previsão:", "Vulnerável" if previsao[0] else "Não Vulnerável")
