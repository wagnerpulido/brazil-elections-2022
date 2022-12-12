import streamlit as st
import folium
from streamlit_folium import st_folium

states_center = {
	'AC': [-8.77, -70.55],
	'AL': [-9.62, -36.82],
	'AM': [-3.47, -65.10],
	'AP': [1.41, -51.77],
	'BA': [-13.29, -41.71],
	'CE': [-5.20, -39.53],
	'DF': [-15.83, -47.86],
	'ES': [-19.19, -40.34],
	'GO': [-15.98, -49.86],
	'MA': [-5.42, -45.44],
	'MT': [-12.64, -55.42],
	'MS': [-20.51, -54.54],
	'MG': [-18.10, -44.38],
	'PA': [-3.79, -52.48],
	'PB': [-7.28, -36.72],
	'PR': [-24.89, -51.55],
	'PE': [-8.38, -37.86],
	'PI': [-6.60, -42.28],
	'RJ': [-22.25, -42.66],
	'RN': [-5.81, -36.59],
	'RO': [-10.83, -63.34],
	'RS': [-30.17, -53.50],
	'RR': [1.99, -61.33],
	'SC': [-27.45, -50.95],
	'SE': [-10.57, -37.45],
	'SP': [-22.19, -48.79],
	'TO': [-9.46, -48.26]
}

state_number = {#Região Norte
	'AC' : 12,
	'AM' : 13,
	'AP' : 16,
	'PA' : 15,
	'RO' : 11,
	'RR' : 14,
	'TO' : 17,
	#'Região Nordeste
	'AL' : 27,
	'BA' : 29,
	'CE' : 23,
	'MA' : 21,
	'PB' : 25,
	'PE' : 26,
	'PI' : 22,
	'RN' : 24,
	'SE' : 28,
	#Região Sudeste
	'ES' : 32,
	'MG' : 31,
	'RJ' : 33,
	'SP' : 35,
	#Região Sul
	'PR' : 41,
	'RS' : 43,
	'SC' : 42,
	#Região Centro-Oeste
	'DF' : 53,
	'GO' : 52,
	'MT' : 51,
	'MS' : 50
}



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

show_map('RJ')