import pandas as pd
import re
import spacy

# Carregue o modelo spacy inglês
# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('pt_core_news_sm')

# ler arquivo lematizado
df = pd.read_csv('sample_teste_nlp_got_lematizado.csv')



# Exemplo de DataFrame com prontuários
data = {
    'prontuario': [
        'Paciente com diabetes e hipertensão Paciente',
        'Paciente com diabetes',
        'Paciente com hipertensão e diabetes Paciente',
        'Paciente com asma',
        'Paciente com diabetes e asma'
    ]
}

dftxt = pd.DataFrame(data)

# Lista de palavras a serem contadas
#palavras = frequencia
palavras = ['diabetes', 'hipertensão', 'Paciente']

# Função para contar palavras únicas em cada prontuário
def contar_palavras_unicas(prontuario, palavras):
    contagem = {palavra: 0 for palavra in palavras}
    for palavra in palavras:
        if re.search(r'\b' + re.escape(palavra) + r'\b', prontuario, re.IGNORECASE):
            contagem[palavra] = 1
    return contagem

# Aplicar a função a cada prontuário e somar os resultados
contagem_total = {palavra: 0 for palavra in palavras}
for prontuario in dftxt['prontuario']:
    contagem = contar_palavras_unicas(prontuario, palavras)
    for palavra in palavras:
        contagem_total[palavra] += contagem[palavra]

# Criar um novo DataFrame com a contagem de pacientes para cada palavra
df_contagem = pd.DataFrame(list(contagem_total.items()), columns=['Palavra', 'Contagem'])

print(df_contagem)

dflista = pd.read_csv('sample_conta_palavras_frequencia.csv')
print(dflista.head(100),"\n")

# Converter DataFrame para JSON 
json_resultado = dflista.to_json(orient='records', lines=True)
#print(json_resultado)

# Função para contar as palavras sem considerar repetições
def conta_palavras_sem_repetir(prontuario):
    doc = nlp(str(prontuario))
    return len(set([token.text for token in doc]))

# Contagem de palavras sem repetições
nmtexto = 'processed_text_gpt_lematizado'
contagem_palavras = dflista[nmtexto].apply(lambda x: conta_palavras_sem_repetir(x))

print("contagem_palavras:")
print(contagem_palavras)
#contagem_palavras.to_csv("contagem_teste.csv")
