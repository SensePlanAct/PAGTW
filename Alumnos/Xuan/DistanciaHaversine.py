from idlelib import tooltip

import folium
#funcion distancia haversen long lat entre dos puntos
# funcion euclidea mismpos puntos
m = folium.Map(location=[43,-5], zoom_start=3)
distanciahaversine=6420
distanciaeuclidea=838
puntos=[]
folium.Marker(location=[43,-5],icon=folium.Icon(color="red"),popup='Oviedo').add_to(m)
folium.Marker(location=[41,-76],icon=folium.Icon(color="red"),popup='Portugal').add_to(m)
folium.Marker(location=[41,-76],icon=folium.Icon(color="red"),popup='America').add_to(m)
folium.PolyLine(locations=[[41,-6],[41,-76]], color="red", tooltip=f'Distancia euclidea:{distanciaeuclidea}' ).add_to(m)
folium.PolyLine(locations=[[41,-6],[42,-26],[42,-46],[41,-76]], color="yellow", tooltip=f'Distancia Haversen:{distanciahaversine}' ).add_to(m)
folium.PolyLine(locations=[[43,-5],[41,-76]], color="yellow").add_to(m)
m.save("mapa.html")