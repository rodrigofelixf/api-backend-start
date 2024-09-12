from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import pandas as pd

# Carregar os dados
base_dados = pd.read_csv('data/base_tratada_refinada2.csv')

# Preparar os dados
X = base_dados.drop(columns=['vulnerabilidade_social'])
y = base_dados['vulnerabilidade_social']
X = X.drop(['nome', 'endereco', 'numero'], axis=1)

# Identificar colunas categóricas e numéricas
categorical_features = X.select_dtypes(include=['object']).columns
numeric_features = X.select_dtypes(include=['float64']).columns

# Criar o pré-processador
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=True), categorical_features)
    ]
)

# Criar o pipeline com MLPClassifier
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42))
])

# Treinar o modelo
model.fit(X, y)

# Salvar o modelo treinado
joblib.dump(model, 'modelo_treinado.pkl')
