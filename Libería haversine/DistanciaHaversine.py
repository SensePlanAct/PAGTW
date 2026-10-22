from idlelib import tooltip
import folium
import haversine

#funcion distancia haversine [lat. long] entre dos puntos
distanciahaversine = haversine.haversine((43,-5),(41,-76))
print("DISTANCIA HAVERSINE", distanciahaversine)

# funcion euclíedea-cartesian mismos puntos
import math
from typing import Tuple

# Constante para el radio de la Tierra en kilómetros.
RADIO_TIERRA = 6371.0

def distancia_tierra_plana(coord1, coord2):

    # Extraer latitudes y longitudes
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convertir todas las coordenadas de grados a radianes
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon1_rad = math.radians(lon1)
    lon2_rad = math.radians(lon2)

    # Calcular la latitud media para corregir el estrechamiento de los meridianos
    lat_media = (lat1_rad + lat2_rad) / 2.0

    # Calcular la diferencia en el eje X (Longitud) corregida por la latitud
    x = (lon2_rad - lon1_rad) * math.cos(lat_media)

    # 4. Calcular la diferencia en el eje Y (Latitud)
    y = lat2_rad - lat1_rad

    # 5. Aplicar el Teorema de Pitágoras (hipotenusa) y multiplicar por el radio
    distancia = math.sqrt(x ** 2 + y ** 2) * RADIO_TIERRA

    return distancia

#coordenadas de Gijón y Valencia
#Gijón 43.534102, -5.664592
#Oviedo 43.360432, -5.843853
#Valencia 39.459940, -0.377993

print ("Gijón - Valencia Tierra plana",distancia_tierra_plana([43.534102,-5.664592], [39.459940, -0.377993]))
print ("Valencia", haversine.haversine([43.534102,-5.664592],[39.459940, -0.377993]))
print ("Gijón - Oviedo Tierra plana",distancia_tierra_plana([43.534102,-5.664592], [43.360432, -5.843853]))
print ("Oviedo",haversine. haversine([43.534102,-5.664592],[43.360432, -5.843853]))


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