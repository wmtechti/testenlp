import pandas as pd
from striprtf.striprtf import rtf_to_text
import datetime

# Função para carregar e processar os dados (usando cache_data)
#@st.cache_data
def load_data(file_path):
    df = pd.read_parquet(file_path, engine='pyarrow')  # Usando Parquet para carregamento rápido
    return df

# Carregar os dados do parquet
# Imprime a data e hora no início da execução inicio = datetime.datetime.now() print(f"Início: {inicio}")
inicio = datetime.datetime.now() 
print("carregando dataset parquet...")
print(f"Início: {inicio}")
# Carregar o arquivo Parquet
df = load_data('sample_teste_nlp.parquet')
# Imprime a data e hora no final da execução 
fim = datetime.datetime.now() 
print(f"Fim: {fim}")
# Calcula e imprime o tempo consumido 
tempo_consumido = fim - inicio
print(f"Tempo consumido: {tempo_consumido}")
print("\n")

# Visualizar as primeiras linhas do DataFrame
# Imprime a data e hora no início da execução inicio = datetime.datetime.now() print(f"Início: {inicio}")
inicio = datetime.datetime.now() 
print("Visualizar as primeiras linhas do DataFrame...")
print(f"Início: {inicio}")
print(df.head())
# Imprime a data e hora no final da execução 
fim = datetime.datetime.now() 
print(f"Fim: {fim}")
# Calcula e imprime o tempo consumido 
tempo_consumido = fim - inicio
print(f"Tempo consumido: {tempo_consumido}")
print("\n")


# Obter informações gerais sobre o DataFrame
# Imprime a data e hora no início da execução inicio = datetime.datetime.now() print(f"Início: {inicio}")
inicio = datetime.datetime.now() 
print("Obter informações gerais sobre o DataFrame...")
print(f"Início: {inicio}")
print(df.info())
# Imprime a data e hora no final da execução 
fim = datetime.datetime.now() 
print(f"Fim: {fim}")
# Calcula e imprime o tempo consumido 
tempo_consumido = fim - inicio
print(f"Tempo consumido: {tempo_consumido}")
print("\n")


# Análise descritiva das colunas
# Imprime a data e hora no início da execução inicio = datetime.datetime.now() print(f"Início: {inicio}")
inicio = datetime.datetime.now() 
print("Obter informações gerais sobre o DataFrame...")
print(f"Início: {inicio}")
print(df.info())
print(df.describe(include='all'))
# Imprime a data e hora no final da execução 
fim = datetime.datetime.now() 
print(f"Fim: {fim}")
# Calcula e imprime o tempo consumido 
tempo_consumido = fim - inicio
print(f"Tempo consumido: {tempo_consumido}")
print("\n")
