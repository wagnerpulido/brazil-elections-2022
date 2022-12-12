import streamlit as st
import json
import topojson as tp
import os.path
import wget
import altair as alt

rr_url = 'https://servicodados.ibge.gov.br/api/v2/malhas/14?formato=application/json'
rr_url = 'https://servicodados.ibge.gov.br/api/v2/malhas/14?formato=application/vnd.geo+json'



states = alt.topo_feature(rr_url, feature='geometry')

c2 = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa').properties(
    width=800,
    height=600
)
st.altair_chart(c2)
