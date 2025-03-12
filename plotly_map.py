import plotly.express as px
import pandas as pd

df = pd.DataFrame({'lat': [40.7128], 'lon': [-74.0060]})
fig = px.scatter_mapbox(df, lat='lat', lon='lon', zoom=12, mapbox_style="carto-positron")
fig.show()
