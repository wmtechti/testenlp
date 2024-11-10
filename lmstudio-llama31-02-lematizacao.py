import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

df = pd.read_csv('doencas-teste.csv')

# Criar um lematizador
lemmatizer = WordNetLemmatizer()

# Remover stopwords
stop_words = set(stopwords.words('portuguese'))

def processar_texto(texto):
    # Lowercase text, remove non-alphabet characters, and split into words
    words = re.sub(r'[^a-zA-Záéíóúâêîôûãõç\s]', '', texto.lower()).split()

    # Tokenizar o texto
    tokens = word_tokenize(texto)

    tokens_filtrados = [token for token in tokens if token not in stop_words]
    
    # Realizar a lematização
    texto_lematizado = ' '.join([lemmatizer.lemmatize(token) for token in tokens_filtrados])
    
    return texto_lematizado

# Aplicar a função em cada linha do dataframe
print("lematizado:")
df['processed_text_llama_lematizado'] = df['processed_text'].astype(str).apply(processar_texto)

df.to_csv('doencas-teste-llama-lematizado.csv', index=False)
print(df['processed_text'].head(10),  df['processed_text_llama_lematizado'].head(10)) 

print({len(df)})


