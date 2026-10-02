import folium       #hay que importar folium para poder usarlo

m = folium.Map(
    location=[43.3614, -5.8593],  #Coordenadas del centro del mapa
    zoom_start=13                 #Zoom original del mapa, luego puede variarse
)

m.save("mapa.html") #con m.save guardamos el mapa que genera folium en un fichero html
