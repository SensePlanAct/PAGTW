from shapely.geometry import Point
from shapely.geometry import LineString


pUnto = Point(30, 10, 5)
pUnto2 = LineString((Point(30, 10, 5), Point(30, 10, 5), Point(30, 10, 5), Point(300, 10, 5)))
#############################################################
# Crear POLIGONO con [-5,43][-6,41][-76,41] Distancia y Área
###########################################################
linea = LineString(pUnto2)

wkt = pUnto.wkt

print(wkt, linea.wkt, linea.length)