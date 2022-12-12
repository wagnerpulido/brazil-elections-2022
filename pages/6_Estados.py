import streamlit as st
import altair as alt
from vega_datasets import data

counties = alt.topo_feature(data.us_10m.url, 'counties')
source = data.unemployment.url

mapa = alt.Chart(counties).mark_geoshape().encode(
    color='rate:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(source, 'id', ['rate'])
).project(
    type='albersUsa'
).properties(
    width=500,
    height=300
)
st.altair_chart(mapa)

root_host = 'https://raw.githubusercontent.com/jonates/opendata/master/arquivos_geoespaciais/'
file_name = 'geojs-100-mun.json'
mapa_url = root_host + file_name


counties = alt.topo_feature(mapa_url, '')

mapa = alt.Chart(
    counties
).mark_geoshape(
).encode(
).properties(
    width=500,
    height=300
)

st.altair_chart(mapa)