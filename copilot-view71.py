import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from striprtf.striprtf import rtf_to_text

#st.set_option('devel.show_script_run_states', True)

arquivo_csv = "sample_teste_nlp_got_lematizado.csv"
# Carrega o arquivo CSV
df = pd.read_csv(arquivo_csv)
dfall = df

# nmtexto = 'processed_text'
nmtexto = 'processed_text_gpt_lematizado'

# Função para converter RTF para texto
def convert_rtf_to_text(rtf):
    return rtf_to_text(rtf)

# Função para converter HTML para texto
def convert_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
# Título do aplicativo
st.title("Visualização de Documentos Médicos")

# Inicializar o índice do registro
if 'index' not in st.session_state:
    st.session_state.index = 0

# Inicializar o termo de pesquisa
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""

# Função para exibir o registro atual
def show_record(index):
    st.write(f"Registro {index + 1} de {len(df)}")
    st.write("patient_id:", df.iloc[index]['patient_id'])
    st.write("age:", df.iloc[index]['age'])
    st.write("sex:", df.iloc[index]['sex'])
    st.write("ehr_date:", df.iloc[index]['ehr_date'])
    st.write("Texto Processado:", df.iloc[index]['processed_text'])

# Função para filtrar registros pelo termo de pesquisa
def search_term(df, term):
    if term:
        return df[df[nmtexto].str.contains(term, case=False, na=False)]
    else:
        return df

# Campo de entrada para o termo de pesquisa
search_query = st.text_input("Digite o termo de pesquisa:", st.session_state.search_query)

# Atualizar o DataFrame filtrado
df = search_term(df, search_query)
st.write(f"Total de registros encontrados: {len(df)}")

# Atualizar o termo de pesquisa na sessão e forçar a atualização da página
#if search_query != st.session_state.search_query:
#    st.session_state.search_query = search_query
#    st.experimental_rerun()

# Botão para limpar o filtro
if st.button("Limpar Filtro"):
    st.session_state.search_query = ""
    df = dfall
    st.session_state.index = 0
    st.write(f"Total de registros encontrados: {len(df)}")

# Botões de navegação
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("Primeiro"):
        st.session_state.index = 0
with col2:
    if st.button("Anterior"):
        if st.session_state.index > 0:
            st.session_state.index -= 1
with col4:
    if st.button("Próximo"):
        if st.session_state.index < len(df) - 1:
            st.session_state.index += 1
with col5:
    if st.button("Último"):
        st.session_state.index = len(df) - 1

# Exibir o registro atual
show_record(st.session_state.index)
