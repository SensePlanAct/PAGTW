from operator import inv
import csv
from pyproj import Geod
from shapely.creation import points
from shapely.geometry import geo

import math

import csv

def aeropuerto_cercano_salida(lat1, lon1):

    mejor = 0
    mejor_distancia=4500000000
    for elemento in aeropuertos:
        az1,az2,dist = geod.inv(lon1,lat1,elemento[2],elemento[1])
        if dist < mejor_distancia:
            mejor_dist = dist
            mejor = elemento
    return mejor




aeropuertos = []
geod=Geod(ellps="WGS84")
c = open("airportss1.csv",encoding="utf-8")
with c as file:
    r = csv.DictReader(file, delimiter=';')
    print(r.line_num)
    for linea in r:

        aeropuertos.append([linea['name'], float(linea['latitude_deg']),float(linea['longitude_deg'])])







lat1 = float(input("Introduce la latitud de origen: "))
lon1 = float(input("Introduce la longitud de origen: "))

print(aeropuerto_cercano_salida(lat1,lon1))


def aeropuerto_cercano_llegada(lat1, lon1):
    lat1 = float(input("Introduce la latitud de destino: "))
    lon1 = float(input("Introduce la longitud de destino: "))

# geod=Geod(ellps="WGS84")
# az1, az2, dist = geod.inv(lon1a,lat1a,lon2a,lat2a)
# print(az1,az2,dist)
# xpuntos=dist/200
# points=geod.npts(lon1,lat1,lon2,lat2,xpuntos)
# print(points)