from shapely.geometry import Polygon

p1 = Polygon([
    (0, 0), (6, 0), (6, 6), (0, 6)
])

p2 = Polygon([
    (4, 4), (9, 4), (9, 8), (4, 8)
])

print("¿Se intersecan?", p1.intersects(p2))

comun = p1.intersection(p2)

print ("Area poligno 1",p1.area)
print ("Area poligno 2\n\n",p2.area)

print("Geometría común:", comun.geom_type)
print("Área común:", comun.area)
print("Perímetro común:", comun.length)

