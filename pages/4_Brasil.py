import altair as alt
import streamlit as st
import topojson as tp
import json

# retirando limite de linhas
alt.data_transformers.enable('default', max_rows=None)

with open("geojs-100-mun.json", 'r') as f:
    data = json.load(f)

assert data['type'] == 'FeatureCollection'
topo = tp.Topology(data)

# to visualize we use the (optional!) package Altair.
#topo.toposimplify(4).to_alt()

c0 = alt.Chart(
    topo
).mark_circle(
).encode(
).properties(
    width=800,
    height=600
)
st.altair_chart(c0)


