from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import pandas as pd


base_dados = pd.read_csv('data/base_tratada_refinada2.csv')


X = base_dados.drop(columns=['vulnerabilidade_social'])
y = base_dados['vulnerabilidade_social']
X = X.drop(['nome', 'endereco', 'numero'], axis=1)


categorical_features = X.select_dtypes(include=['object']).columns
numeric_features = X.select_dtypes(include=['float64']).columns


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=True), categorical_features)
    ]
)


model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])


model.fit(X, y)


joblib.dump(model, 'modelo_treinado.pkl')

import joblib


modelo = joblib.load('modelo_treinado.pkl')






