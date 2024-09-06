from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import pandas as pd

# Exemplo de dados de treinamento
base_dados = pd.read_csv('data/base_tratada_refinada2.csv')

# Separar previsores (X) e classe (y)
X = base_dados.drop(columns=['vulnerabilidade_social'])
y = base_dados['vulnerabilidade_social']
X = X.drop(['nome', 'endereco', 'numero'], axis=1)

# Definindo as colunas categóricas e numéricas
categorical_features = X.select_dtypes(include=['object']).columns
numeric_features = X.select_dtypes(include=['float64']).columns

# Pipelines para pré-processamento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=True), categorical_features)
    ]
)

# Pipeline final
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Treinar o modelo
model.fit(X, y)

# Salvar o modelo
joblib.dump(model, 'modelo_treinado.pkl')

import joblib

# Carregar o modelo
modelo = joblib.load('modelo_treinado.pkl')






