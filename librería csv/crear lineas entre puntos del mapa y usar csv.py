import folium
import csv

puntos = []

c = open("coordenadas")
with c as file:
    r = csv.DictReader(file, delimiter=',', fieldnames=['latitud', 'longitud'])
    print(r.line_num)
    for linea in r:
        print(linea)
        puntos.append([float(linea['latitud']), float(linea['longitud'])])

c = open("coordenadas")
with c as file:
    for linea in c:
        print(linea)
c.close()

m = folium.Map(
    location=[43.3614, -5.8593],
    zoom_start=13
)

# puntos = [
#     [43.3614, -5.8593],
#     [43.3650, -5.8500],
#     [43.3700, -5.8450],
#     [43.3750, -5.8550]
# ]

"""
Puedo usar solo un par de puntos para una línea, pasándolos como una lista de 2 elementos, o tantos puntos como quiera
para crear un polinomio
"""


folium.PolyLine(
    locations=puntos,
    color="purple",
    weight=4,
    opacity=0.8
).add_to(m)

"""
Atributos de la línea
"""

m.save("mapa.html")
