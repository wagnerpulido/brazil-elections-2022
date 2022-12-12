import streamlit as st
import os.path
import wget
import geopandas as gpd
import altair as alt

st.set_page_config(
    page_title="Mapas"
)

st.write("# Welcome to Streamlit! 👋")

root_host = 'https://raw.githubusercontent.com/jonates/opendata/master/arquivos_geoespaciais/'
file_name = 'geojs-100-mun.json'

def down_geo_data():
    if not os.path.exists(file_name):
        wget.download(f'{root_host}{file_name}')

down_geo_data()

url_geojson_munic = 'geojs-100-mun.json'
geo_munic = gpd.read_file(url_geojson_munic,)
geo_munic = geo_munic.astype({'id':int})
geo_munic = geo_munic.astype({'geometry':str})

geo_munic.info()

chart_mapa = alt.Chart(
    geo_munic
).mark_geoshape().encode(
    #color='QT_VOTOS:Q'
).properties(
    width=800,
    height=600
)

#st.altair_chart(chart_mapa, use_container_width=True)

african_countries = alt.topo_feature(
        'geojs-100-mun.json',
        'id',
    )

africa_chart = (
    alt.Chart(african_countries)
    .mark_geoshape(stroke="white", strokeWidth=2)
)
st.altair_chart(africa_chart)
