import pyproj
from shapely.ops import transform
from shapely.geometry import Point

proyecto = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32630")

punto_wgs84 = Point(-5, 43)

#############################################################
# TRANFORMAR con [-5,43][-6,41][-76,41] Distancia y Área
###########################################################

print(transform(proyecto.transform, punto_wgs84))
