"""
    @autor: Rodrigo
    @date: 30/10/2026
    @email: uo312563@uniovi.es

"""
#Hay que ir hasta el aeropuerto de Moscú y solo puedo volar 400km
#Mirar los aeropuertos en 400km y escoger el que mas cerca vaya hacia Moscú
from pyproj import Geod
import csv
import folium
import pyproj
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely import transform
aeropuertos= []
c = open("airports_criba.csv", encoding="utf-8")
with c as file:
    contenido = csv.DictReader(file, delimiter=',')
    campos = (contenido.fieldnames)
    for fila in contenido:
        aeropuerto=[float(fila["latitude_deg"]),float(fila["longitude_deg"]),fila["name"],fila["municipality"]]
        aeropuertos.append(aeropuerto)
# Instancia de Clase
geod = Geod(ellps="WGS84")
max= 400000
moscu=(55.756862519582285, 37.61504856949836)
asturias=(43.24212697758314, -5.776344222967733)

def dist_acimut(a, b):
    az1, az2, dist = geod.inv(a[1], a[0], b[1], b[0])
    return dist, az1, az2
def aeropuerto_mas_cercano(a,b):
    mejor = a
    mejor_dist = 0
    for aeropuerto in b:
        dist = dist_acimut(a, aeropuerto)[0]
        if mejor == a or dist < mejor_dist:
            mejor = aeropuerto
            mejor_dist = dist
    return mejor, mejor_dist
def circulo(p):
    puntos = []
    for az in range(0, 360):
        lon, lat, dist = geod.fwd(p[1], p[0], az, max)
        puntos.append((lon, lat))
    return Polygon.puntos
def aeropuerto_ruta(origen,destino):
    destino,mejor_dist = aeropuerto_mas_cercano(destino, aeropuertos)
    actual,mejor_dist = aeropuerto_mas_cercano(origen, aeropuertos)
    ruta = [actual]
    visitados = [actual]
    while actual != destino:
        lista = [ap for ap in aeropuertos if ap not in visitados and dist_acimut(actual, ap)[0] <= max]
        actual = min(lista, key=lambda ap: dist_acimut(ap, destino)[0])
        visitados.append(actual)
        ruta.append(actual)
    return ruta
ruta = aeropuerto_ruta(asturias,moscu)
print(ruta)