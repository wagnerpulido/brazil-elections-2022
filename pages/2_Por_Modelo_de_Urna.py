import streamlit as st
import altair as alt
from mapa import *
from prepare_data import *
from prepare_geo_code import *

col1, col2, col3 = st.columns(3)
with col1:
    #selecionar cargo
    cargo_selecionado = st.selectbox('Escolha o cargo', cargos)
with col2:
    #selecionar estado
    uf_escolhida = st.selectbox('Estado', estados)
with col3:
    #selecionar turno
    turnos = ['1t', '2t']
    turno_escolhido = st.selectbox('Turno', turnos)

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
    zona_escolhida = st.multiselect('Selecione a zona', zonas)
    dataframe = dataframe[dataframe['NR_ZONA'].isin(zona_escolhida)]

# Selecionar Seção
filtrar_por_secao = st.checkbox('filtrar por seção')
secoes = dataframe['NR_SECAO'].unique().tolist()
if filtrar_por_secao:
    secao_escolhida = st.multiselect('Selecione a seção', secoes)
    dataframe = dataframe[dataframe['NR_SECAO'].isin(secao_escolhida)]


# Selecionar Modelo de Urna
filtrar_por_modelo_urna = st.checkbox('filtrar por modelo de urna')
modelos_urna = dataframe['DS_MODELO_URNA'].unique().tolist()
if filtrar_por_modelo_urna:
    modelo_escolhido = st.multiselect('Selecione o modelo', modelos_urna)
    dataframe = dataframe[dataframe['DS_MODELO_URNA'].isin(modelo_escolhido)]

# Show Map
#df_by_city = add_ibge_code(dataframe, uf_escolhida)
#show_map(df_by_city, uf_escolhida)

# Mapa locais de votação
places = do_places(uf_escolhida, dataframe)
show_map_urnas(places, uf_escolhida)

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

