import pandas as pd
import openai
import json

openai.api_key = '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'
                                             
# Funções
def feature_product(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "assistant",
              "content": text
            },
            {
              "role": "user",
              "content": "What is the category, model, material, color and functions. Format the final response in json with the following keys: category, model, material, functions. Keep the format."
            },
        ],
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
        
    feature = response['choices'][0]['message']['content']
    
    return feature


def feature_more_product(df):
    
    feature_list = []
    
    for index, row in df.iterrows():
        
        value = row['user_message']
        user_message = str(value)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "assistant",
                    "content": user_message
                },
                {
                    "role": "assistant",
                    "content": "What is the category, model, material, color and functions. Format the final response in json with the following keys: category, model, material, color, functions. Keep the format."
                },
            ],
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        
        feature = response['choices'][0]['message']['content']
        feature_list.append(feature)
    
    return feature_list


def create_json(feature_sample):
    lista_de_objetos_json = []
    lista_de_linhas_ignoradas = []

    for json_string in feature_sample:
        try:
            objeto_json = json.loads(json_string)
            lista_de_objetos_json.append(objeto_json)
        except json.JSONDecodeError as e:
            print(f"Erro ao analisar JSON: {str(e)}. Ignorando a linha: {json_string}")
            lista_de_linhas_ignoradas.append(json_string)

    return lista_de_objetos_json, lista_de_linhas_ignoradas

def generate_image(category_value):
    # Generate image based on the category value
    response = openai.Image.create(
        prompt=category_value,
        n=1,
        size="1024x1024"
    )

    # Get the image URL
    image_url = response['data'][0]['url']
    return image_url