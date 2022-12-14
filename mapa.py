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


def show_map_urnas(places, state):
    mapa = folium.Map(
        location= states_center[state] ,
        zoom_start=6,
        tile='MapQuest Open Aerial',
        scrollWheelZoom=False
    )
    for _, plc in places.iterrows():
        folium.Marker(
            location=[plc['latitude'], plc['longitude']],
            icon=folium.Icon(color=colors[plc['DS_MODELO_URNA']]),
            tooltip=f"""
            Municipio: {plc['NM_MUNICIPIO']},<BR>
            Nome: {plc['nome'] if plc['nome'] is not None else ''},<BR> 
            Zona: {plc['zona']}, Seção: {plc['secao']},<BR> 
            Modelo Urna: {plc['DS_MODELO_URNA']}"""
        ).add_to(mapa)
    st_mapa = st_folium(mapa, width=500, height=500)
