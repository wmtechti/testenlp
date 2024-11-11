import pandas as pd

# Extrair palavras-chave
key_words = [word for word, freq in word_freq.most_common(1000) if freq > 2]

# Criar um DataFrame com as palavras-chave e frequências
df = pd.DataFrame({'Palavras-Chave': key_words, 'Frequência': [freq for word, freq in word_freq.most_common(1000) if freq > 2]})

# Visualizar o DataFrame
print(df)