'''
    @autor: Pachi
    @date: 29/10/26
    @email: sanchezbfrancisco

'''
import shapely
from folium import Polygon
from shapely.geometry import Point
from shapely.geometry import LineString


pUnto = Point(30, 10, 5)
pUnto2 = LineString((Point(30, 10, 5), Point(30, 10, 5), Point(30, 10, 5), Point(300, 10, 5)))

linea = LineString(pUnto2)

#############################################################
# Crear POLIGONO con [-5,43][-6,41][-76,41] Distancia y Área
#############################################################
poligonoF = Polygon([(43,-76), (43,-6),(41,-5),])
poligono = shapely.Polygon([(43,-76), (43,-6),(41,-5),])

print(pUnto.wkt, linea.wkt, linea.length)
print(poligono.wkt, poligono.length, poligono.area)