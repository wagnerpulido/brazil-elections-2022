import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from util import *

def show_map(df, state):
    mapa = folium.Map(
        location= states_center[state] ,
        zoom_start=6,
        tiles='CartoDB positron',
        #tile='Stamen Terrain',
        scrollWheelZoom=False
    )
    ibge_url= f'https://servicodados.ibge.gov.br/api/v3/malhas/estados/{state_number[state]}?formato=application/vnd.geo+json&intrarregiao=municipio'
    choro = folium.Choropleth(
        geo_data=ibge_url,
        data=df,
        columns=['id_municipio','QT_VOTOS'],
        key_on='feature.properties.codarea',
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Qt votos",
        highlight=True
    )

    choro.add_to(mapa)
    choro.geojson.add_to(mapa)

#    for feature in choro.geojson.data['features']:
#        feature['properties']['NM_MUNICIPIO'] = 'abc'

    choro.geojson.add_child(
        folium.features.GeoJsonTooltip(['codarea'], labels=False)
    )
    st_mapa = st_folium(mapa, width=500, height=500)


def read_data_places(uf):
    iter_csv = pd.read_csv('data/perfil_eleitorado_local_votacao_2022.csv', iterator=True, chunksize=10000)
    df = pd.concat(
        [chunk[
             (chunk['sigla_uf'] == uf)
             & (chunk['tipo_secao_agregada'] == 'principal')
             & (chunk['turno'] == 2)
         ] for chunk in iter_csv]
    )
    places = df.groupby(['nome']).first()
    places = places[places['latitude'].notna()]
    return places


def show_map_urnas(state):
    mapa = folium.Map(
        location= states_center[state] ,
        zoom_start=6,
        tile='MapQuest Open Aerial',
        scrollWheelZoom=False
    )
    places = read_data_places(state)
    for _, plc in places.iterrows():
        folium.Marker(
            location=[plc['latitude'], plc['longitude']],
        ).add_to(mapa)
    st_mapa = st_folium(mapa, width=500, height=500)
