import csv
import folium
import pyproj
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely import transform
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

# ARREGLO: el CSV no es una única línea continua, sino varios trozos de la frontera
# pegados sin orden (y algunos al revés). Al unirlos tal cual salen las líneas que
# cruzan el mapa. Índice de la lista = fila del CSV - 2 (la fila 1 es la cabecera).
A = puntos[0:664]      # filas 2-665
B = puntos[664:670]    # filas 666-671   (va al revés)
C = puntos[671:692]    # filas 673-693   anillo pequeño cerrado, va aparte
D = puntos[692:716]    # filas 694-717
E = puntos[716:728]    # filas 718-729   anillo pequeño cerrado, va aparte
G = puntos[730:832]    # filas 732-833   (va al revés)
H = puntos[832:928]    # filas 834-929
# Las filas 730-731 solo repiten dos puntos ya existentes y dibujaban una línea falsa: se descartan.

# Cada trozo tiene que empezar donde acaba el anterior: A -> B invertido -> H -> D -> G invertido
contorno = A + B[::-1] + H + D + G[::-1]
contorno = [p for i, p in enumerate(contorno) if i == 0 or p != contorno[i-1]]  # quita puntos repetidos seguidos

transformer = pyproj.Transformer.from_crs("EPSG:4326","EPSG:3857",always_xy=True)
print(contorno)
poligono_wgs84=Polygon([(lon, lat) for lat, lon in contorno]) #shapely trabaja con (x=lon, y=lat); antes estaba (lat, lon) y la proyección salía mal
proyeccion = lambda x, y: transformer.transform(x,y)
poligono = transform(poligono_wgs84, proyeccion,interleaved=False)

print(poligono)
# Crear mapa centrado aproximadamente en Asturias.
m = folium.Map(
    location=[43.35, -5.85],
    zoom_start=10,
    tiles="OpenStreetMap"
)
for anillo in (contorno, C, E):   # el contorno principal y los dos anillos pequeños
    folium.Polygon(
        locations=anillo,
        color="red",
        fillcolor="purple",
        weight=4,
        opacity=0.8
    ).add_to(m)
m.save("mapa_carreño.html")
