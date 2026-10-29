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
poligonoS = shapely.Polygon([(43,-76), (43,-6),(41,-5),])
poligonoM = shapely.Polygon([(4564099.122524217, -557305.2572745769), (4786738.104110763, -669141.0570442461),(4786738.104110763, -13377019)])

print(pUnto.wkt, linea.wkt, linea.length)
print(poligonoS.wkt, poligonoS.length, poligonoS.area)
print(poligonoM.wkt, poligonoM.length, poligonoM.area)