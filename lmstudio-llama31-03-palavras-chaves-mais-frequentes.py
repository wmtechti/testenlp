import pandas as pd
import spacy
from collections import Counter
import re
# a linha abaix foi testa para um filtro de dataset de doenças
#df = pd.read_csv('doencas-teste-gpt-lematizado.csv')

# df = pd.read_csv('sample_teste_nlp-gpt-lematizado.csv')
# df = pd.read_csv('doenca_teste_nlp-gpt-lematizado.csv')
# df = pd.read_csv('sample_teste_nlp_gpt_convetido_para_texto.csv')
df = pd.read_csv('sample_teste_nlp_got_lematizado.csv')

# print total number of rows for data
print(' total number of rows for data: ', len(df.index))
#print(contagem)
print("\n")
# Carregar o CSV
#df = pd.read_parquet('sample_teste_nlp.parquet')

# Visualizar as primeiras linhas do DataFrame
print("Visualizar as primeiras linhas do DataFrame\n", df.head())
#print(contagem)
print("\n")
# Obter informações gerais sobre o DataFrame
print("Obter informações gerais sobre o DataFrame\n",df.info())
#print(contagem)
print("\n")
# Análise descritiva das colunas
print("Análise descritiva das colunas\n",df.describe(include='all'))
#print(contagem)
print("\n")
#unique
print("nunique\n", df.nunique())

# Carregar o modelo de linguagem
nlp = spacy.load('pt_core_news_sm')

#texto a ser usado
# nmtexto = 'processed_text'
nmtexto = 'processed_text_gpt_lematizado'

# Extrair palavras-chave
palavras_chave = []
for texto in df[nmtexto]:
    doc = nlp(texto)
    # palavras_chave.extend([token.text for token in doc if token.is_alpha])
    palavras_chave.extend([token.text for token in doc if token.is_alpha and not token.is_stop])

#palavras_chave = df['processed_text_gpt_lematizado']

#palavras_chave gerada
#print("\npalavras chaves geradas:\n", palavras_chave)


# Mostrar as palavras-chave mais comuns
print("\npalavras chaves mais comum:")
contagem = Counter(palavras_chave)
print(contagem.most_common(100))

# Mostrar as palavras-chave mais comuns
#print("\npalavras chaves mais comum:", contagem)

#dftxt = pd.DataFrame(contagem)

#print(contagem)
print("\n")

print("frequencia...")
# Calcular frequência de palavras
frequencia = df[nmtexto].str.split().explode().value_counts()
print("info: ")
print(frequencia.info())
print("\n")

print("index 0:\n")

print(frequencia.head(100))
frequencia.to_csv('sample_conta_palavras_frequencia.csv')

#print("treinar modelo...")
# Treinar o modelo
#vectorizer = TfidfVectorizer()
#X_train, X_test, y_train, y_test = train_test_split(df['processed_text'], df['categoria'], test_size=0.2, random_state=42)
#modelo = MultinomialNB()
#modelo.fit(vectorizer.fit_transform(X_train), y_train)

# Avaliar o modelo
#acuracia = modelo.score(vectorizer.transform(X_test), y_test)
#print(f'Acurácia: {acuracia:.2f}')





