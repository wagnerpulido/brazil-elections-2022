from benfordslaw import benfordslaw
import pandas as pd
import streamlit as st
from prepare_data import *
from prepare_geo_code import *

#selecionar cargo
cargo_selecionado = st.sidebar.selectbox('Escolha o cargo', cargos)
#selecionar estado
uf_escolhida = st.sidebar.selectbox('Estado', estados)
#selecionar turno
turnos = ['1t', '2t']
turno_escolhido = st.sidebar.selectbox('Turno', turnos)

# tratamento dos dados
file_name = get_file_name(turno_escolhido, uf_escolhida)
call_data(file_name)
dataframe = read_df(file_name, cargo_selecionado, [])
add_modelo_urna(dataframe)
add_is2020(dataframe)

# Selecionar candidato
filtrar_candidato = st.checkbox('filtrar por canditado')
candidatos = dataframe['NM_VOTAVEL'].unique().tolist()
if filtrar_candidato:
    candidato_escolhido = st.multiselect('Selecionar candidatos', candidatos)
    dataframe = dataframe[dataframe['NM_VOTAVEL'].isin(candidato_escolhido)]

# Selecionar Modelo de Urna
filtrar_por_modelo_urna = st.checkbox('filtrar por modelo de urna')
modelos_urna = dataframe['DS_MODELO_URNA'].unique().tolist()
if filtrar_por_modelo_urna:
    modelo_escolhido = st.multiselect('Selecione o modelo', modelos_urna)
    dataframe = dataframe[dataframe['DS_MODELO_URNA'].isin(modelo_escolhido)]

list_pos = [1,2,-1,-2]
digito = st.sidebar.selectbox(
    'Digito',
    options=list_pos)

bl = benfordslaw(alpha=0.05, pos=digito)
X = pd.DataFrame(dataframe.groupby(['NM_MUNICIPIO'])['QT_VOTOS'].sum())
results = bl.fit(X)
fig, ax = bl.plot(title='Votos por município')
st.pyplot(fig)

st.dataframe(X)