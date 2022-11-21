import plotly.express as px
import pandas as pd
import matplotlib

#info = pd.read_csv('./Nuevo.csv')
info = pd.read_csv('./filtered_stars.csv')
stars = pd.DataFrame(info)
stars.info()

names = stars["Star_name"].to_list()
Masses = stars["Mass"].to_list()
Radius = stars["Radius"].to_list()
Distance = stars["Distance"].to_list()
Gravity = stars["Gravity"].to_list()

fig = px.bar(x=names, y=Masses,title="Nombre y Masa")
fig.show()

fig = px.bar(x=names, y=Radius,title="Nombre y Raadio")
fig.show()

fig = px.bar(x=names, y=Distance,title="Nombre y Distancia")
fig.show()

fig = px.bar(x=names, y=Gravity,title="Nombre y Gravedad")
fig.show()