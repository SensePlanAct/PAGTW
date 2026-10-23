from shapely.geometry import Polygon

coordenadas = [
    (0, 0),
    (100, 0),
    (100, 50),
    (0, 50),
    (0, 0)
]

poligono = Polygon(coordenadas)

print("¿Es válido?", poligono.is_valid)
print("Área:", poligono.area)
print("Perímetro:", poligono.length)
print("Límites:", poligono.bounds)