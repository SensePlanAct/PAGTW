import csv
import folium
import pyproj
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely import transform
from shapely.geometry import LineString
from shapely.ops import unary_union, polygonize
from collections import Counter
import csv
puntos=[]
c = open("carreno_lat_lon.csv")
with c as file:
    contenido = csv.DictReader(file, delimiter=',') #si el fichero tiene una fila con los nombres de las columnas no necesito ponerlo, en caso contrario tengo que añadir
    #un parámetro que sea fieldnames=['campo1','campo2','campo3',...] para que me cree las entradas correctas en los diccionarios.
    campos = (contenido.fieldnames) #me guarda los nombres de las columnas en el caso de que el fichero las tenga
    for fila in contenido:  #recorro todas las filas que he leido del fichero
        punto=[float(fila[campos[0]]),float(fila[campos[1]])]
        puntos.append(punto)

# ARREGLO: el CSV son varios trozos de frontera pegados sin orden. Los empalmes entre
# trozos son segmentos que unen dos puntos que aparecen repetidos en el fichero
# (cada trozo empieza y acaba en un punto compartido). Se descartan esos segmentos y
# shapely une el resto solo (polygonize).
pts = [(lon, lat) for lat, lon in puntos]   #shapely trabaja con (x=lon, y=lat)
veces = Counter(pts)
tramos = [LineString([a, b]) for a, b in zip(pts, pts[1:])
          if not (veces[a] > 1 and veces[b] > 1)]
poligonos = list(polygonize(unary_union(tramos)))      # contorno principal + 2 anillos pequeños
poligono_wgs84 = max(poligonos, key=lambda p: p.area)  # el contorno principal

transformer = pyproj.Transformer.from_crs("EPSG:4326","EPSG:3857",always_xy=True)
print(puntos)
proyeccion = lambda x, y: transformer.transform(x,y)
poligono = transform(poligono_wgs84, proyeccion,interleaved=False)

print(poligono)
# Crear mapa centrado aproximadamente en Asturias.
m = folium.Map(
    location=[43.35, -5.85],
    zoom_start=10,
    tiles="OpenStreetMap"
)
for p in poligonos:   # el contorno principal y los dos anillos pequeños
    folium.Polygon(
        locations=[(lat, lon) for lon, lat in p.exterior.coords],
        color="red",
        fillcolor="purple",
        weight=4,
        opacity=0.8
    ).add_to(m)
m.save("mapa_carreño.html")
