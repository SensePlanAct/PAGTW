from shapely.geometry import Polygon

exterior = Polygon([
    (0, 0), (10, 0), (10, 10), (0, 10)
])

interior = Polygon([
    (2, 2), (5, 2), (5, 5), (2, 5)
])

parcial = Polygon([
    (8, 8), (12, 8), (12, 12), (8, 12)
])

#uso el poligono exterior, y pregunto si interior está dentro
print("Interior contenido:", exterior.contains(interior))
#uso poligono interior y pregunto si está dentro de exterior
print("Interior dentro:", interior.within(exterior))
#Uso poligono exterior y pregunto si está dentro uno que no está completo dentro
print("Parcial contenido:", exterior.contains(parcial))
#uso exterior y pregunto si cubre el interior
print("Área cubierta:", exterior.covers(interior))

