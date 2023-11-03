import streamlit as st
import pandas as pd
import openai
import json

from functions import feature_product, generate_image

def product_feature_generator():

    # Dataframe de referência
    df = pd.read_csv('components\datasets\df_sample_description.csv')

    # Sidebar
    st.title('Product Feature Generator')
    # Allow user to select a row
    selected_text = st.selectbox('Select a message:', df['user_message'])

    # Display the selected text
    st.write(selected_text)

    # Button to trigger feature generation
    if st.button('Generate Feature'):
        # Generate features for the selected text
        feature = feature_product(selected_text)
        st.write('Generated Features:')
        st.json(feature)
                
        # Create JSON para um DataFrame
        data = json.loads(feature)
        df_feature = pd.DataFrame(data, index=[0])
                
        # Display the resulting DataFrame
        st.write('Feature DataFrame:')
        st.write(df_feature)

        # Generate and display an image based on the category
        category_value = df_feature['category'].iloc[0]  # Replace with the appropriate column name
        image_url = generate_image(category_value)
        st.write('Generated Image:')
        st.image(image_url, width=256)

def analytics():
    # Sidebar
    st.title('Analytics')
    st.write('Em produção: Gráficos sobre as features geradas a partir do LLM ChatGPT e similaridade entre os produtos a partir das funções')

def main():
    # Streamlit app
    st.title('Dadosfera analysis and generator')

    # Sidebar navigation
    menu=["Analytics", "Product Feature Generator"]
    choice = st.sidebar.selectbox("Select a section", menu)

    if choice == "Product Feature Generator":
        product_feature_generator()
    elif choice == "Analytics":
        analytics()

if __name__ == '__main__':
    main()