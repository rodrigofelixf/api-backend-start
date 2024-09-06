import joblib
from sklearn.model_selection import cross_val_score
import pandas as pd

# Carregar o modelo treinado
modelo = joblib.load('modelo_treinado.pkl')

# Carregar o conjunto de dados (ajuste conforme necessário)
# Aqui estamos apenas criando um DataFrame de exemplo
# Substitua isso pelo carregamento do seu conjunto de dados real
df = pd.read_csv('../data/base_tratada_refinada2.csv')

# Dividir os dados em variáveis preditoras (X) e variável alvo (y)
X = df.drop('vulnerabilidade_social', axis=1)  # Substitua 'target' pelo nome da coluna da variável alvo
y = df['vulnerabilidade_social']  # Substitua 'target' pelo nome da coluna da variável alvo

# Realizar o k-fold cross-validation (k=5)
scores = cross_val_score(modelo, X, y, cv=5)


# Exibir a precisão de cada fold
for i, score in enumerate(scores, start=1):
    print(f"Precisão do fold {i}: {score}")

# Exibir a precisão média e o desvio padrão
print(f"Precisão média: {scores.mean()}")
print(f"Desvio padrão: {scores.std()}")
