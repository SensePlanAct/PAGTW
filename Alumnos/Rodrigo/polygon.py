"""
    @autor: Rodrigo
    @date: 29/10/2026
    @email: uo312563@uniovi.es

"""
import shapely
from folium import Polygon
from shapely.geometry import LineString
import pyproj
from shapely.ops import transform
from shapely.geometry import Point

proyecto = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32630")

punto_wgs84_1 = Point(-5, 41)
punto_wgs84_2 = Point(-6, 43)
punto_wgs84_3 = Point(-76, 43)


#############################################################
# TRANFORMAR con [-5,43][-6,41][-76,41] Distancia y Área
###########################################################

print((f'{transform(proyecto.transform,punto_wgs84_1)}\n{transform(proyecto.transform,punto_wgs84_2)}\n{transform(proyecto.transform,punto_wgs84_3)}'))
poligono= shapely.Polygon([transform(proyecto.transform,punto_wgs84_1),transform(proyecto.transform,punto_wgs84_2),transform(proyecto.transform,punto_wgs84_3)])
print(f'area: {poligono.area}, perimetro: {poligono.length}')
poligonoM= shapely.Polygon([(5935950.567989731, -768869.6756130814), (6232373.215840384, -954383.5030179297),(1624462.1281824398, -8901117.457167761)])
print(f'area: {poligonoM.area}, perimetro: {poligonoM.length}')
"""
pUnto = Point(30, 10, 5)
pUnto2 = LineString((Point(30, 10, 5), Point(30, 10, 5), Point(30, 10, 5), Point(300, 10, 5)))

linea = LineString(pUnto2)

#############################################################
# Crear POLIGONO con [-5,43][-6,41][-76,41] Distancia y Área
#############################################################
poligono= shapely.Polygon([(43,-76),(43,-6),(41,-5)])
poligono1= Polygon([(43,-76),(43,-6),(41,-5)])

print(pUnto.wkt, linea.wkt, linea.length)
print(f'{poligono.area},{poligono.length}\n{poligono1}')
"""