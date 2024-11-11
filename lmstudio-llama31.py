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


# Carregar o CSV
#df = pd.read_parquet('sample_teste_nlp.parquet')

# Visualizar as primeiras linhas do DataFrame
print(df.head())

# Obter informações gerais sobre o DataFrame
print(df.info())

# Análise descritiva das colunas
print(df.describe(include='all'))

# Carregar o modelo de linguagem
nlp = spacy.load('pt_core_news_sm')

# Extrair palavras-chave
palavras_chave = []
for texto in df['processed_text']:
    doc = nlp(texto)
    palavras_chave.extend([token.text for token in doc if token.is_alpha and not token.is_stop])

# Mostrar as palavras-chave mais comuns
print("palavras chaves mais comum:")
from collections import Counter
contagem = Counter(palavras_chave)
print(contagem.most_common(300))
print("\n")

print("frequencia...")
# Calcular frequência de palavras
frequencia = df['processed_text'].str.split().explode().value_counts()
print(frequencia.nlargest(10))


