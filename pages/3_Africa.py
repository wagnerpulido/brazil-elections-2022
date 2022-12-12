import altair as alt
import streamlit as st
import topojson as tp
from vega_datasets import data

airports = data.airports()
airports.head()

c1 = alt.Chart(airports).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(10),
    tooltip='name'
).project(
    "albersUsa"
).properties(
    width=500,
    height=400
)
st.altair_chart(c1)

states = alt.topo_feature(data.us_10m.url, feature='states')
print(states)

c2 = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa').properties(
    width=500,
    height=300
)
st.altair_chart(c2)


states = alt.topo_feature(data.us_10m.url, feature='states')
airports = data.airports()

background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa').properties(
    width=500,
    height=300
)

points = alt.Chart(airports).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(10),
    tooltip='name'
)
st.altair_chart(background + points)


import geopandas as gpd
import altair as alt

gdf = gpd.read_file(
    'https://raw.githubusercontent.com/vega/vega/master/docs/data/us-10m.json',
    driver='TopoJSON'
)
alt.Chart(gdf).mark_geoshape().encode(color='id:Q').project('albersUsa')


import altair as alt
import geopandas as gpd
import gpdvega

#alt.renderers.enable('notebook')

world = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres')
)

c5 = alt.Chart(
    world[world.continent=='Africa']
).mark_geoshape(
).encode(
    color='pop_est',
    tooltip=['name','pop_est']
).properties(
    width=500,
    height=300
)
st.altair_chart(c5)