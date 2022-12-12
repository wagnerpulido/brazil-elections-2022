import streamlit as st
import altair as alt
import json
import topojson as tp
import os.path
import wget

acre_url = 'https://github.com/tbrugz/geodata-br/blob/master/geojson/geojs-12-mun.json'
acre_file = 'geojs-12-mun.json'

brasil_url = 'https://github.com/tbrugz/geodata-br/blob/master/geojson/geojs-100-mun.json'
brasil_file = 'geojs-100-mun.json'

rr_url = 'https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-14-mun.json'
rr_file = 'geojs-14-mun.json'

if not os.path.exists(rr_file):
    wget.download(rr_url)

with open(rr_file, 'r') as gj_1:
    geojson_1 = json.load(gj_1)

# geojson_1['features'][1]

# Desabilitanto o limite de 5.000 linhas de df do Altair
alt.data_transformers.enable('default', max_rows=None)

# criando o mapa
mapa = alt.Chart(geojson_1).mark_geoshape(
    stroke='grey',
    strokeWidth=0.1
  ).properties(
    width=600,
    height=400
)

# Exibindo o mapa
st.altair_chart(mapa)
#(mapa_altair).configure_view(strokeWidth=0)