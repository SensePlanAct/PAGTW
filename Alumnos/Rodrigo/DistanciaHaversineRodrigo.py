from idlelib import tooltip
import pyproj
import shapely
from shapely.ops import transform
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
#from shapely.wtk import loads
import math
import folium
import haversine
point = Point(30,10,5)
"""wtk_representation=point.wtk
print(f'WTK del punto: {wtk_representation}')"""
project = pyproj.Transformer.from_proj(
    pyproj.Proj("EPSG:4326"),
    pyproj.Proj("EPSG:32630"),
)
point_wgs84=Point(-5.7725, 43.2502)
point_utm=transform(project.transform, point_wgs84)
print(point_utm)
poligono= Polygon([43,-5],[46,-4],[50,-1])
punto= LineString(Point(10, 30, 5), Point(20, 10, 5), Point(50, 10, 5))
linea=LineString(punto)
print(linea)

lat1 = float(input("Introduce la latitud de origen: "))
lon1 = float(input("Introduce la longitud de origen: "))
lat2 = float(input("Introduce la latitud de destino: "))
lon2 = float(input("Introduce la longitud de destino: "))
R = 6371.0  # radio tierra
def distancia_haversine(coord1, coord2):

    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
def distancia_euclidea(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
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
    distancia = math.sqrt(x ** 2 + y ** 2) * R
    return distancia

punto_origen = [lat1, lon1]
punto_destino = [lat2, lon2]
distancia_hav = distancia_haversine(punto_origen, punto_destino)
distancia_euc = distancia_euclidea(punto_origen, punto_destino)
m = folium.Map(location=[lat1, lon1], zoom_start=3)
folium.Marker(location=punto_origen, icon=folium.Icon(color="red"), popup="Península Ibérica").add_to(m)
folium.Marker(location=punto_destino, icon=folium.Icon(color="red"), popup="América").add_to(m)

punto3=[((lat1+lat2)/2)-3, ((lon1+lon2)/2)-3]
linea = [punto_origen,punto3,punto_destino]

folium.PolyLine(
    locations=linea,
    color="yellow",
    tooltip=f"Distancia Haversine: {distancia_hav} km"
).add_to(m)
folium.Marker(location=[43,-5],icon=folium.Icon(color="red"),popup='Oviedo').add_to(m)
folium.Marker(location=[41,-76],icon=folium.Icon(color="red"),popup='Portugal').add_to(m)
folium.Marker(location=[41,-76],icon=folium.Icon(color="red"),popup='America').add_to(m)
folium.PolyLine(locations=[[41,-6],[41,-76]], color="red", tooltip=f'Distancia euclidea:{distancia_euc}' ).add_to(m)
folium.PolyLine(locations=[[41,-6],[42,-26],[42,-46],[41,-76]], color="yellow", tooltip=f'Distancia Haversen:{distancia_hav}' ).add_to(m)
folium.PolyLine(locations=[[43,-5],[41,-76]], color="yellow").add_to(m)

folium.PolyLine(locations=[punto_origen, punto_destino], color="gray", dash_array="5",tooltip=f'Distancia Euclidea: {distancia_euc}').add_to(m)
m.save("mapa1.html")