import folium
from folium import plugins
import json

def magn_color(magn):
    color_ = ''
    if magn <= 3:
        color_ = "#F0BB00"
    if magn > 3 and magn <= 5:
        color_ = "#E69700"
    if magn > 5 and magn <= 7:
        color_ = "#E67700"
    if magn > 7 and magn <= 8:
        color_ = "#E64E00"
    if magn >= 8:
        color_ = "#E00000"
    
    icon_set = folium.plugins.BeautifyIcon(
        border_color=color_,
        text_color="#000000",
        number=magn,
        inner_icon_style="margin-top:0;",
    )
    return icon_set

south_map = folium.Map().add_child(folium.LatLngPopup())

with open("D:\diplom\output.json", 'r') as json_file:
    data = json.load(json_file)

json.dumps(data)

for i in range(0, len(data)):
    #html = data[i]['id'] + ' ' + data[i]['code'] + ' ' + data[i]['date'] + ' ' + data[i]['time'] + ' ' + data[i]['depth'] + ' ' + '((' + str(data[i]['magnitude']) + '))' + ' ' + data[i]['N']
    html = data[i]
    print(data[i]['latitude'],data[i]['longitude'])
    location = (data[i]['latitude'],data[i]['longitude'])
    icons = magn_color(data[i]['magnitude'])
    folium.Marker(location, popup=html, icon=icons).add_to(south_map)

south_map.save("main.html")