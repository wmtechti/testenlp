import re

import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from bs4 import BeautifulSoup
from striprtf.striprtf import rtf_to_text

# Função para converter RTF para texto
def convert_rtf_to_text(rtf):
    return rtf_to_text(rtf)

# Função para converter HTML para texto
def convert_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

# Função para processar a última colunapi
def process_text_column(text):
    if text.startswith('{\\rtf'):
        return convert_rtf_to_text(text)
    elif '<html>' in text or '</html>' in text:
        return convert_html_to_text(text)
    else:
        return text

# Função para carregar e processar os dados (usando cache_data)
#@st.cache_data
def load_data(file_path):
    df = pd.read_parquet(file_path, engine='pyarrow')  # Usando Parquet para carregamento rápido
    df['processed_text'] = df['text'].apply(process_text_column)
    return df

# Carregar o arquivo Parquet
df = load_data('sample_teste_nlp.parquet')

# Visualizar as primeiras linhas do DataFrame
print(df.head())

# Obter informações gerais sobre o DataFrame
print(df.info())

# Análise descritiva das colunas
print(df.describe(include='all'))

print(df.info())
print("\n")

# Função para filtrar registros pelo termo de pesquisa
def search_term(df, term):
    if term:
        return df[df['processed_text'].str.contains(term, case=False, na=False)]
    else:
        return df

# print("contains....")    
# doenca = search_term(df, "doença")

# print("Total de registros encontrados:", {len(df)}, {len(doenca)})

#print(doenca.value_counts().head(10))
# Exportando o DataFrame para um arquivo CSV
#doenca.to_csv('doencas-teste.csv', index=False)

#df.to_csv('sample_teste_nlp_gpt_convetido_para_texto.csv')
print(df.info())
print("\n")