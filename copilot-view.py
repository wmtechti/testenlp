import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import rtf_to_text

# Função para converter RTF para texto
def convert_rtf_to_text(rtf):
    return rtf_to_text.rtf_to_text(rtf)

# Função para converter HTML para texto
def convert_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

# Função para processar a última coluna
def process_text_column(text):
    if text.startswith('{\\rtf'):
        return convert_rtf_to_text(text)
    elif '<html>' in text or '</html>' in text:
        return convert_html_to_text(text)
    else:
        return text

# Função para filtrar registros pelo termo "medicamento"
def search_term(df, term):
    return df[df['processed_text'].str.contains(term, case=False, na=False)]

# Carregar o arquivo CSV
df = pd.read_csv('sample_teste_nlp.csv')

# Processar a última coluna
df['processed_text'] = df['ultima_coluna'].apply(process_text_column)

# Título do aplicativo
st.title("Visualização de Documentos Médicos")

# Campo de entrada para o termo de pesquisa
search_query = st.text_input("Digite o termo de pesquisa:", "medicamento")

# Filtrar registros pelo termo de pesquisa
filtered_df = search_term(df, search_query)

# Exibir os dados filtrados
st.write(filtered_df[['coluna1', 'coluna2', 'coluna3', 'coluna4', 'processed_text']])
