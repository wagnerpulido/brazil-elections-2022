import streamlit as st
import folium
from streamlit_folium import st_folium
from util import *
from prepare_geo_code import get_code_ibge_tse

def show_map(state):
    mapa = folium.Map(
        location= states_center[state] ,
        zoom_start=6,
        tiles='CartoDB positron'
    )
    ibge_url= f'https://servicodados.ibge.gov.br/api/v3/malhas/estados/{state_number[state]}?formato=application/vnd.geo+json&intrarregiao=municipio'
    choro = folium.Choropleth(
        geo_data=ibge_url
    )
    choro.geojson.add_to(mapa)
    st_mapa = st_folium(mapa, width=500, height=500)

selected_state = st.selectbox('Estado', state_number.keys())

show_map(selected_state)

get_code_ibge_tse(selected_state)