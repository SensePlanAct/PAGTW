from pyproj import Geod

#Defino un geod con el elipsoide WGS 84

geod = Geod(ellps="WGS84")

"""
Método inv() permite calcular distancia geodésica entre 2 puntos
y los azimuts inicial y final

Hay que darle Lon1,Lat1 (longitud y latitud del punto inicial)
Hay que darle Lon2,Lat2 (longitud y latitud del punto final)

az1: Azimut inicial (ángulo desde el punto inicial hacia el punto final)
az2: Azimut final (ángulo desde el punto final de vuelta al punto inicial)
Dist: distancia geodésica entre los puntos
"""

az1,az2,dist = geod.inv(12.4924,41.8902,2.3522,48.8566)
print(az1,az2,dist)

"""
Permite generar una serie de puntos equidistantes en una línea geodésica entre dos puntos dados

Hay que darle lon1,lat1 (longitud y latitud del punto inicial)
Hay que darle lon2,lat2 (longitud y latitud del punto final)
ntps: Número de puntos intermedios que se desean generar (sin contar inicial y final)

Devuelve point_list (lista de longitudes y latitudes de los puntos intermedios generados (lista de tuplas)

"""

points = geod.npts(12.9424,41.8902,2.3522,48.8566,4)
print (points)

"""

Nos permite, dado un azimut y una distancia, calcular la ubicación final.

Hay que darle lon1, lat1 (longitud y latitud del punto incial)

az1 Azimut inicial

Dist: Distancia a la que se desea mover desde el punto inicial en la dirección del azimut

Devuelve Lon2,lat2 longitud y latitud del punto final.
az2: Azimut en el punto final de vuelva al punto inicial

"""

lon2,lat2,az2 = geod.fwd(12.4924,41.8902,az1,150000)

print (lon2,lat2)