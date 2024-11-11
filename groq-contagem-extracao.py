import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

arquivo_csv = 'sample_teste_nlp_got_lematizado.csv'

nmtexto = 'processed_text_gpt_lematizado'   
# Carregue o DataFrame
df = pd.read_csv(arquivo_csv)

# Preparar o texto
df['prontuario_groq'] = df[nmtexto].astype(str)

# Remover caracteres especiais
df['prontuario_groq'] = df['prontuario_groq'].str.replace('[^a-zA-Z0-9\s]', '')

# Tokenizar o texto
df['prontuario_groq'] = df['prontuario_groq'].apply(word_tokenize)

# Remover palavras comuns
stop_words = set(stopwords.words('portuguese'))
df['prontuario_groq'] = df['prontuario_groq'].apply(lambda x: [word for word in x if word not in stop_words])

# Contar frequência de palavras
word_freq = Counter()
for prontuario in df['prontuario_groq']:
    word_freq.update(prontuario)

print(word_freq, "\n")

# Extrair palavras-chave
key_words = [word for word, freq in word_freq.most_common(1000) if freq > 0]

# print(key_words)

# Criar um DataFrame com as palavras-chave e frequências
df = pd.DataFrame({'Palavras-Chave': key_words, 'Frequência': [freq for word, freq in word_freq.most_common(1000) if freq > 0]})

# Visualizar o DataFrame
print(df)


# Crie um DataFrame com as palavras-chave
#df = pd.DataFrame({'Palavras-Chave': key_words})

# Salve o DataFrame em um arquivo CSV
df.to_csv('groq_palavras_chave_freq.csv', index=False)