'''
    @autor: Pachi
    @date: 29/10/26
    @email: sanchezbfrancisco

    DESCRIPTION Uso de La librería PYPROJ
    https://pypi.org/project/pyproj/
'''
from pyproj import Transformer
import shapely
from shapely.ops import transform
from shapely.geometry import Point

proyecto = Transformer.from_crs("EPSG:4326", "EPSG:3857")

punto_wgs84_1 = Point(-5, 41)
punto_wgs84_2 = Point(-6, 43)
punto_wgs84_3 = Point(-76, 43)

#############################################################
# TRANFORMAR con [-5,43][-6,41][-76,41] Distancia y Área
###########################################################

print(transform(proyecto.transform, punto_wgs84_1))
print(transform(proyecto.transform, punto_wgs84_2))
print(transform(proyecto.transform, punto_wgs84_3))


poligono = shapely.Polygon([transform(proyecto.transform, punto_wgs84_1), transform(proyecto.transform, punto_wgs84_2),transform(proyecto.transform, punto_wgs84_3),])
print(poligono.wkt)
print(poligono.length, poligono.area)