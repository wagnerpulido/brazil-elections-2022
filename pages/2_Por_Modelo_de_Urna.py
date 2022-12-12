import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import os.path
import wget
import zipfile

bus = [
'bweb_2t_AC_311020221535', 'bweb_2t_AL_311020221535', 'bweb_2t_AM_311020221535', 'bweb_2t_AP_311020221535',
'bweb_2t_BA_311020221535', 'bweb_2t_CE_311020221535', 'bweb_2t_DF_311020221535', 'bweb_2t_ES_311020221535',
'bweb_2t_GO_311020221535', 'bweb_2t_MA_311020221535', 'bweb_2t_MG_311020221535', 'bweb_2t_MS_311020221535',
'bweb_2t_MT_311020221535', 'bweb_2t_PA_311020221535', 'bweb_2t_PB_311020221535', 'bweb_2t_PE_311020221535',
'bweb_2t_PI_311020221535', 'bweb_2t_PR_311020221535', 'bweb_2t_RJ_311020221535', 'bweb_2t_RN_311020221535',
'bweb_2t_RO_311020221535', 'bweb_2t_RR_311020221535', 'bweb_2t_RS_311020221535', 'bweb_2t_SC_311020221535',
'bweb_2t_SE_311020221535', 'bweb_2t_SP_311020221535', 'bweb_2t_TO_311020221535', 'bweb_2t_ZZ_311020221535',
'bweb_1t_AC_051020221321', 'bweb_1t_AL_051020221321', 'bweb_1t_AM_051020221321', 'bweb_1t_AP_051020221321',
'bweb_1t_BA_051020221321', 'bweb_1t_CE_051020221321', 'bweb_1t_DF_051020221321', 'bweb_1t_ES_051020221321',
'bweb_1t_GO_051020221321', 'bweb_1t_MA_051020221321', 'bweb_1t_MG_051020221321', 'bweb_1t_MS_051020221321',
'bweb_1t_MT_051020221321', 'bweb_1t_PA_051020221321', 'bweb_1t_PB_051020221321', 'bweb_1t_PE_051020221321',
'bweb_1t_PI_051020221321', 'bweb_1t_PR_051020221321', 'bweb_1t_RJ_051020221321', 'bweb_1t_RN_051020221321',
'bweb_1t_RO_051020221321', 'bweb_1t_RR_051020221321', 'bweb_1t_RS_051020221321', 'bweb_1t_SC_051020221321',
'bweb_1t_SE_051020221321', 'bweb_1t_SP_051020221321', 'bweb_1t_TO_051020221321', 'bweb_1t_ZZ_051020221321'
]

def get_file_name(turno, estado):
    if turno == '1t':
        return f'bweb_1t_{estado}_051020221321'
    else:
        return f'bweb_2t_{estado}_311020221535'

drop_not_cidade = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO',
       'NM_TIPO_ELEICAO', 'CD_PLEITO', 'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO',
       'DS_ELEICAO', 'SG_UF', 'CD_MUNICIPIO',
       'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA',
       'NM_PARTIDO',
       'DT_BU_RECEBIDO', 'QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCOES',
       'CD_TIPO_URNA', 'DS_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'DS_TIPO_VOTAVEL',
       'NR_VOTAVEL',
       'CD_CARGA_1_URNA_EFETIVADA', 'CD_CARGA_2_URNA_EFETIVADA',
       'CD_FLASHCARD_URNA_EFETIVADA', 'DT_CARGA_URNA_EFETIVADA',
       'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA',
       'DT_ENCERRAMENTO', 'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU',
       'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA',
       'DS_CARGO_PERGUNTA', 'NR_URNA_EFETIVADA', 'QT_VOTOS', 'NR_PARTIDO', 'SG_PARTIDO', 'NM_VOTAVEL', 'NR_ZONA', 'NR_SECAO']


drop_col = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO',
       'NM_TIPO_ELEICAO', 'CD_PLEITO', 'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO',
       'DS_ELEICAO', 'SG_UF', 'CD_MUNICIPIO',
       'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA',
       'NM_PARTIDO',
       'DT_BU_RECEBIDO', 'QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCOES',
       'CD_TIPO_URNA', 'DS_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'DS_TIPO_VOTAVEL',
       'NR_VOTAVEL',
       'CD_CARGA_1_URNA_EFETIVADA', 'CD_CARGA_2_URNA_EFETIVADA',
       'CD_FLASHCARD_URNA_EFETIVADA', 'DT_CARGA_URNA_EFETIVADA',
       'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA',
       'DT_ENCERRAMENTO', 'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU',
       'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA']

partidos = ['PTB', 'PL', 'PT', 'PDT', 'MDB', '#NULO#', 'NOVO', 'UNIÃO', 'PSOL',
            'PP', 'PMN', 'PODE', 'PROS', 'PATRIOTA', 'REPUBLICANOS', 'PSD',  'PMB', 'DC',
            'REDE', 'PRTB', 'SOLIDARIEDADE', 'PSC', 'CIDADANIA', 'PV', 'PSB', 'PSDB', 'PC do B',
            'PCB', 'UP', 'PSTU', 'PCO', 'Nulo', 'Branco']

cores = ['#00bfff', '#120075', '#c4122d','#FE8E6D', '#00aa4f', '#3b484e','#F3701B', '#40ccff', '#FFEE57',
         '#0067A5', '#DD3333', '#31b44b','#f48c24', '#006400', '#002cc4','#FFA500', '#DD3333', '#0065cb',
         '#00C2BB', '#2cb53f', '#ff6600','#006f41', '#0080FF', '#DA251C','#ff0000', '#000000', '#c92127',
         '#9F030A', '#3b484e', '#FEFEFE', '#FEFEFE']

# ['NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'NR_URNA_EFETIVADA', 'QT_VOTOS', 'NR_PARTIDO', 'SG_PARTIDO', 'NM_VOTAVEL', 'NR_ZONA', 'NR_SECAO']

root_host = "https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2022/buweb/"

def call_data(item):
    file_name = item + '.zip'
    if not os.path.exists(file_name):
        wget.download(f'{root_host}{file_name}')
    if not os.path.exists(item + ".csv"):
        with zipfile.ZipFile(f'{file_name}', 'r') as zip_ref:
            zip_ref.extractall('data')
    if os.path.exists(file_name):
        os.remove(file_name)

def read_df(file_name, cargo):
    iter_csv = pd.read_csv('data/' + file_name + ".csv", sep=';', encoding='latin-1', iterator=True, chunksize=10000)
    dataframe = pd.concat([chunk[chunk["DS_CARGO_PERGUNTA"] == cargo] for chunk in iter_csv])
    dataframe = dataframe.drop(columns=drop_col)
    return dataframe

def read_cidades(file_name):
    iter_csv = pd.read_csv('data/' + file_name + ".csv", sep=';', encoding='latin-1', iterator=True, chunksize=10000)
    dataframe = pd.concat([chunk[chunk["DS_CARGO_PERGUNTA"] == 'Presidente'] for chunk in iter_csv])
    dataframe = dataframe.drop(columns=drop_not_cidade)
    cidades = dataframe['NM_MUNICIPIO'].unique().tolist()
    return cidades


# create a list of our conditions
def add_modelo_urna(df):
    conditions = [
        (df['NR_URNA_EFETIVADA'] <= 1220500),
        (df['NR_URNA_EFETIVADA'] >= 1220501) & (df['NR_URNA_EFETIVADA'] <= 1345500),
        (df['NR_URNA_EFETIVADA'] >= 1368501) & (df['NR_URNA_EFETIVADA'] <= 1370500),
        (df['NR_URNA_EFETIVADA'] >= 1600000) & (df['NR_URNA_EFETIVADA'] <= 1650000),
        (df['NR_URNA_EFETIVADA'] >= 1650001) & (df['NR_URNA_EFETIVADA'] <= 1701000),
        (df['NR_URNA_EFETIVADA'] >= 1750000) & (df['NR_URNA_EFETIVADA'] <= 1950000),
        (df['NR_URNA_EFETIVADA'] >= 2000000) & (df['NR_URNA_EFETIVADA'] <= 2250000)
    ]

    # create a list of the values we want to assign for each condition
    values = ['2009', '2010', '2011', '2011', '2013', '2015', '2020']

    # create a new column and use np.select to assign values to it using our lists as arguments
    df['DS_MODELO_URNA'] = np.select(conditions, values)

    # display updated DataFrame
    df.head()


def add_is2020(df):
    df['IS_2020'] = np.where(df['DS_MODELO_URNA'] == '2020', '2020', 'OUTRAS')

capitais = ['RIO BRANCO','MACEIO','MACAPA','MANAUS','SALVADOR','FORTALEZA','VITORIA','GOIANIA','SAO LUIS','CUIABA',
'CAMPO GRANDE','BELO HORIZONTE','BELEM','JOAO PESSOA','CURITIBA','RECIFE','TERESINA','RIO DE JANEIRO','NATAL',
'PORTO ALEGRE','PORTO VELHO','BOA VISTA','FLORIANOPOLIS','SAO PAULO','ARACAJU','PALMAS']

def drop_capitais(df):
    df = df[~df['NM_MUNICIPIO'].isin(capitais)]
    return df

#selecionar cargo
cargos = ['Presidente', 'Governador', 'Senador', 'Deputado Federal', 'Deputado Estadual']
cargo_selecionado = st.selectbox('Escolha o cargo', cargos)

#selecionar estado
estados = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','ZZ']
uf_escolhida = st.selectbox('Estado', estados)

#selecionar turno
turnos = ['1t', '2t']
turno_escolhido = st.selectbox('Turno', turnos)

# Selecionar cidade
#file_2t = get_file_name('2t',uf_escolhida)
#cidades = read_cidades(file_2t)
#filtrar_por_cidade = st.checkbox('filtrar por cidade')
#cidades_escolhidas = []
#if filtrar_por_cidade:
#    cidades_escolhidas = st.multiselect('Selecione a cidade', cidades)

# df padrão
sem_capital = st.checkbox('Sem a capital')
show_distribuicao = st.checkbox('Mostrar distribuição')

# tratamento dos dados
file_name = get_file_name(turno_escolhido, uf_escolhida)
call_data(file_name)
dataframe = read_df(file_name, cargo_selecionado)
if sem_capital:
    dataframe = drop_capitais(dataframe)

add_modelo_urna(dataframe)
add_is2020(dataframe)

# Selecionar cidade
filtrar_por_cidade = st.checkbox('filtrar por cidade')
cidades = dataframe['NM_MUNICIPIO'].unique().tolist()
if filtrar_por_cidade:
    cidade_escolhida = st.multiselect('Selecione a cidade', cidades)
    dataframe = dataframe[dataframe['NM_MUNICIPIO'].isin(cidade_escolhida)]

# Selecionar candidato
filtrar_candidato = st.checkbox('filtrar por canditado')
candidatos = dataframe['NM_VOTAVEL'].unique().tolist()
if filtrar_candidato:
    candidato_escolhido = st.multiselect('Selecionar candidatos', candidatos)
    dataframe = dataframe[dataframe['NM_VOTAVEL'].isin(candidato_escolhido)]


# Selecionar Zona
filtrar_por_zona = st.checkbox('filtrar por zona')
zonas = dataframe['NR_ZONA'].unique().tolist()
if filtrar_por_zona:
    zona_escolhida = st.multiselect('Selecione a cidade', zonas)
    dataframe = dataframe[dataframe['NR_ZONA'].isin(zona_escolhida)]

# Selecionar Modelo de Urna
filtrar_por_modelo_urna = st.checkbox('filtrar por modelo de urna')
modelos_urna = dataframe['DS_MODELO_URNA'].unique().tolist()
if filtrar_por_modelo_urna:
    modelo_escolhido = st.multiselect('Selecione o modelo', modelos_urna)
    dataframe = dataframe[dataframe['DS_MODELO_URNA'].isin(modelo_escolhido)]


if show_distribuicao:
    # distribuição do modelo de urna por município
    domain = ['2020', '2015', '2013', '2011', '2010', '2009']
    range_ = ['blue', 'red', 'darkred', 'indianred', 'orangered', 'mediumvioletred']
    chart = alt.Chart(dataframe).mark_circle(size=60).encode(
        alt.OpacityValue(0.7),
        x='QT_VOTOS',
        y='NM_MUNICIPIO',
        size='QT_VOTOS',
        color=alt.Color('DS_MODELO_URNA', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=['NR_PARTIDO', 'NM_MUNICIPIO', 'DS_MODELO_URNA']
    ).properties(
        title=f'Distribuição do modelo de urna por município - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    # distribuição do modelo de urna por município
    domain = ['2020', '2015', '2013', '2011', '2010', '2009']
    range_ = ['blue', 'red', 'darkred', 'indianred', 'orangered', 'mediumvioletred']
    chart = alt.Chart(dataframe).mark_circle(size=60).encode(
        alt.OpacityValue(0.7),
        x='NR_SECAO',
        y='NM_MUNICIPIO',
        size='QT_VOTOS',
        color=alt.Color('DS_MODELO_URNA', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=['NR_PARTIDO', 'NM_MUNICIPIO', 'DS_MODELO_URNA']
    ).properties(
        title=f'Distribuição do modelo de urna por município - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)


# Gráfico de linhas por modelo de urna (Média)
df_mean = dataframe.groupby(['DS_MODELO_URNA', 'NM_VOTAVEL', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].mean()
chart_line = alt.Chart(df_mean
).mark_line().encode(
    x = alt.X('DS_MODELO_URNA', title="Modelo de urna"),
    y = alt.Y('QT_VOTOS', title="Média de votos"),
    color=alt.Color('NM_VOTAVEL'), #, scale=alt.Scale(domain=partidos, range=cores)),
    tooltip=['NM_VOTAVEL', 'SG_PARTIDO']
).properties(
    title = f"Média de votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}",
    width = 250,
    height = 250
)
st.altair_chart(chart_line, use_container_width=True)

# Gráfico de pontos dos valores absolutos
df_sum = dataframe.groupby(['IS_2020', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
chart_sum = alt.Chart(df_sum).mark_point().encode(
    x = alt.X('SG_PARTIDO', title='Sigla do partido'),
    y = alt.Y('QT_VOTOS', title='Soma de votos'),
    color=alt.Color('SG_PARTIDO', scale=alt.Scale(domain=partidos, range=cores)),
).properties(
    width = 250, height = 250
).facet(
    facet=alt.Facet('IS_2020:N', title=None),
    title=f'Soma dos votos por tipo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}',
    columns = 2
)
st.altair_chart(chart_sum, use_container_width=True)


# Gráfico normalizado IS_2020
source = dataframe.groupby(['IS_2020', 'NM_VOTAVEL', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
chart_norm = alt.Chart(source
).mark_bar(opacity=0.8).encode(
    x=alt.X('sum(QT_VOTOS)', stack="normalize", title='Soma dos votos normalizada'),
    y=alt.Y('IS_2020', title='Modelo de urna'),
    color=alt.Color('SG_PARTIDO:N', scale=alt.Scale(domain=partidos, range=cores)),
    tooltip = [alt.Tooltip('NM_VOTAVEL:N')]
).properties(
    title=f'Soma normalizada dos votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
)
st.altair_chart(chart_norm, use_container_width=True)

# Gráfico normalizado DS_MODELO_URNA
source = dataframe.groupby(['DS_MODELO_URNA', 'NM_VOTAVEL', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
chart_norm = alt.Chart(source).mark_bar(opacity=0.8).encode(
    x=alt.X('sum(QT_VOTOS)', stack="normalize", title='Soma dos votos normalizada'),
    y=alt.Y('DS_MODELO_URNA', title='Modelo de urna', sort='-x'),
    color=alt.Color('SG_PARTIDO:N', scale=alt.Scale(domain=partidos, range=cores)),
    tooltip = [alt.Tooltip('NM_VOTAVEL:N')]
).properties(
    title=f'Soma normalizada dos votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
)
st.altair_chart(chart_norm, use_container_width=True)


# Gráfico normalizado por zona
source = dataframe.groupby(['NR_ZONA', 'NM_VOTAVEL', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
chart_norm = alt.Chart(source).mark_bar(opacity=0.8).encode(
    x=alt.X('sum(QT_VOTOS)', stack="normalize", title='Soma dos votos normalizada'),
    y=alt.Y('NR_ZONA', title='Zona'),
    color=alt.Color('SG_PARTIDO:N', scale=alt.Scale(domain=partidos, range=cores)),
    tooltip = [alt.Tooltip('NM_VOTAVEL:N')]
).properties(
    title=f'Soma normalizada dos votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
)
st.altair_chart(chart_norm, use_container_width=True)

# Gráfico normalizado por seção
source = dataframe.groupby(['NR_SECAO', 'NM_VOTAVEL', 'SG_PARTIDO', 'NM_MUNICIPIO'], as_index=False)['QT_VOTOS'].sum()
chart_norm = alt.Chart(source).mark_bar(opacity=0.8).encode(
    x=alt.X('sum(QT_VOTOS)', stack="normalize", title='Soma dos votos normalizada'),
    y=alt.Y('NR_SECAO', title='Seção'),
    color=alt.Color('SG_PARTIDO:N', scale=alt.Scale(domain=partidos, range=cores)),
    tooltip = ['NM_VOTAVEL', 'NM_MUNICIPIO']
).properties(
    title=f'Soma normalizada dos votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
).interactive()
st.altair_chart(chart_norm, use_container_width=True)

# detalhar seções
detalha_secao = st.checkbox("Detalhar seção")
if detalha_secao:
    # Gráfico normalizado por zona - seção
    source = dataframe.groupby(['NR_ZONA', 'NR_SECAO', 'SG_PARTIDO', 'NM_VOTAVEL'], as_index=False)['QT_VOTOS'].sum()
    chart_norm = alt.Chart(source).mark_bar(opacity=0.8).encode(
        alt.Column('NR_ZONA'),
        y=alt.Y('sum(QT_VOTOS)', stack="normalize", title='Soma dos votos normalizada'),
        x=alt.X('NR_SECAO', title='Zona'),
        color=alt.Color('SG_PARTIDO:N', scale=alt.Scale(domain=partidos, range=cores)),
        tooltip = [alt.Tooltip('NM_VOTAVEL:N')]
    ).properties(
        title=f'Soma normalizada dos votos por modelo de urna - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
    ).interactive()
    st.altair_chart(chart_norm, use_container_width=True)



# gráfico de pizza 2020
domain = partidos #['PT', 'PL']
range_ = cores # ['red', 'blue']
df_sum = dataframe.groupby(['IS_2020', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
ue2020_to_pie = df_sum[df_sum['SG_PARTIDO'].isin(['PL', 'PT'])]
ue2020_to_pie = ue2020_to_pie[ue2020_to_pie['IS_2020'].isin(['2020'])]
ue_outras_to_pie = ue2020_to_pie[ue2020_to_pie['IS_2020'].isin(['OUTRAS'])]
ue2020_to_pie = ue2020_to_pie.drop(columns=['IS_2020'])

base = alt.Chart(ue2020_to_pie
).mark_arc(opacity=0.7).encode(
    theta=alt.Theta(field="QT_VOTOS", type="quantitative"),
    color=alt.Color(field="SG_PARTIDO", type="nominal", scale=alt.Scale(domain=domain, range=range_))
).properties(
    title=f'Quantidade de votos por partido: urna 2020 - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
)
pie = base.mark_arc(outerRadius=120)
text = base.mark_text(radius=160, size=20).encode(text="QT_VOTOS")
full_pie = pie + text
st.altair_chart(full_pie, use_container_width=True)

# gráfico de pizza OUTRAS
df_sum = dataframe.groupby(['IS_2020', 'SG_PARTIDO'], as_index=False)['QT_VOTOS'].sum()
ue_outras_to_pie = df_sum[df_sum['SG_PARTIDO'].isin(['PL', 'PT'])]
ue_outras_to_pie = ue_outras_to_pie[ue_outras_to_pie['IS_2020'].isin(['OUTRAS'])]

base = alt.Chart(ue_outras_to_pie
).mark_arc(opacity=0.7).encode(
    theta=alt.Theta(field="QT_VOTOS", type="quantitative"),
    color=alt.Color(field="SG_PARTIDO", type="nominal", scale=alt.Scale(domain=domain, range=range_))
).properties(
    title=f'Quantidade de votos por partido: outras urnas - {uf_escolhida} - {turno_escolhido} - {cargo_selecionado}'
)
pie = base.mark_arc(outerRadius=120)
text = base.mark_text(radius=160, size=20).encode(text="QT_VOTOS")
full_pie = pie + text
st.altair_chart(full_pie, use_container_width=True)

