import os
import pandas as pd
import openai
import json


from functions import feature_more_product, create_json

# Dataframe de referência
df = pd.read_csv('components/datasets/df_sample_description.csv')
sample = df['user_message'].iloc[:100]
df_sample = pd.DataFrame({'user_message': sample})

# Gerando as características
feature_sample = feature_more_product(df_sample)

# Selecionando as características que obdeceram a estrutura json solicitada no LLM ChatGPT na função feature_more_product
objetos_json, linhas_ignoradas = create_json(feature_sample)

# Criando um Dataframe das caracteríticas a partir dos objetos_json
df_feature_0_a_100 = pd.DataFrame(objetos_json)

# Salvando as características em .csv
df_feature_0_a_100.to_csv('output/df_feature_0_a_100.csv', index=False)
