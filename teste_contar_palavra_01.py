import pandas as pd

def contar_palavras(palavras, arquivo_csv):
    # Carrega o arquivo CSV
    df = pd.read_csv(arquivo_csv)
    
    nmtexto = 'processed_text_gpt_lematizado'
    #nmtexto = 'processed_text'    
    # Cria um dicionário para armazenar a contagem de palavras
    contagem = {}
    
    # Percorre a lista de palavras
    for palavra in palavras:
        # Conta a quantidade de documentos que têm a palavra na coluna "prontuario"
        contagem[palavra] = df[df[nmtexto].str.contains(palavra)].shape[0]
        
    
    return contagem

palavras = ['paciente', '<html']

arquivo_csv = 'sample_teste_nlp_got_lematizado.csv'
#arquivo_csv = 'sample_teste_nlp_gpt_convetido_para_texto.csv'

contagem = contar_palavras(palavras, arquivo_csv)
print("contagem:")
print(contagem, "\n")

def somar_palavras(palavras, arquivo_csv):
    # nmtexto = 'processed_text_gpt_lematizado'    
    nmtexto = 'processed_text'    
    # Carrega o arquivo CSV
    df = pd.read_csv(arquivo_csv)
    
    # Cria um dicionário para armazenar a soma de palavras
    soma = {}
    
    # Percorre a lista de palavras
    for palavra in palavras:
        # Soma a quantidade de ocorrências de cada palavra em todos os documentos
        # soma[palavra] = df[nmtexto].str.count(palavra).sum()
        soma[palavra] = df[nmtexto].str.count(palavra).sum()
    
    return soma

palavras = ['paciente', 'alergia', 'temperatura', 'exame']
soma = somar_palavras(palavras, arquivo_csv)
print(soma)