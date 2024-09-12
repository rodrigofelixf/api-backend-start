import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Carregar o modelo treinado
modelo = joblib.load('modelo_treinado.pkl')

# Carregar e preparar os dados de teste
# Exemplo com dados de teste, substitua 'data/test_data.csv' e ajuste as colunas conforme necessário
dados_teste = pd.read_csv('data/base_tratada_refinada2.csv')

# Preparar os dados de teste
X_teste = dados_teste.drop(columns=['vulnerabilidade_social'])
y_teste = dados_teste['vulnerabilidade_social']
X_teste = X_teste.drop(['nome', 'endereco', 'numero'], axis=1)

# Fazer previsões com o modelo carregado
previsoes = modelo.predict(X_teste)

# Avaliar a acurácia
acuracia = accuracy_score(y_teste, previsoes)

print(f'Acurácia do modelo: {acuracia:.2f}')
