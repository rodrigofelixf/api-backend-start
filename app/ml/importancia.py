import pandas as pd
import joblib


# Carregar o modelo treinado
modelo = joblib.load('modelo_treinado.pkl')

# Obter o pré-processador do pipeline
preprocessor = modelo.named_steps['preprocessor']

# Obter os nomes das features transformadas
numeric_feature_names = preprocessor.named_transformers_['num'].get_feature_names_out()
categorical_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out()

# Unir todos os nomes das features
feature_names = numeric_feature_names.tolist() + categorical_feature_names.tolist()

# Obter a importância das features
importancias = modelo.named_steps['classifier'].feature_importances_

# Criar um DataFrame para visualizar
importancia_df = pd.DataFrame({'Feature': feature_names, 'Importância': importancias})

# Ordenar as features pela importância
importancia_df = importancia_df.sort_values(by='Importância', ascending=False)

# Exibir o DataFrame
print(importancia_df)

# # Opcional: Plotar a importância das features
# plt.figure(figsize=(10, 6))
# plt.barh(importancia_df['Feature'], importancia_df['Importância'])
# plt.xlabel('Importância')
# plt.ylabel('Feature')
# plt.title('Importância das Features no Modelo de Random Forest')
# plt.gca().invert_yaxis()