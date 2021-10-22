import folium
from numpy.lib.shape_base import tile

import pandas

# to view a map in html  with latitude and longitude

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif elevation>=100 and elevation<3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.89],zoom_start=6, tile="Mapbox Bright")

# To add feature to the map

fgv = folium.FeatureGroup(name="Volcanoes")
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])
name = list(data["NAME"])


# adding html on pop up 

html = """ 
Volcano Name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>

Height: %s m

"""


# Adding marker to the map green colored  with pop up a text 
for ln,lt,el,name in zip(lat,lon,ele,name):
    iframe = folium.IFrame(html=html %(name,name,el),width=200,height=100)
    fgv.add_child(folium.CircleMarker(location=[ln,lt],radious=6,popup=folium.Popup(iframe),fill_color=color_producer(el),color="grey",fill_opacity=0.7))



fgp = folium.FeatureGroup(name="Population")
# adding popultion in map by country
fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else "orange" if 10000000<=x['properties']['POP2005'] <20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
#map.save("Map_popup_advanced.html")





