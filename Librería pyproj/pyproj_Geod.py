from pyproj import Geod

print(0)

# Instancia de Clase
geod = Geod(ellps="WGS84")

# Calcular azimut y distancias
az1, az2, dist = geod.inv(-5, 43, -76, 41)
print(az1, az2, dist)

# Calcular la ubicación final
puntos = geod.npts(-5, 43, -76, 41, 5)
print(puntos)

# Generar una serie de puntos equidistantes en una línea geodésica entre dos puntos dados
lonD, latD, azD = geod.fwd(-5, 43, az1, 5703703)
print(lonD, latD, azD)