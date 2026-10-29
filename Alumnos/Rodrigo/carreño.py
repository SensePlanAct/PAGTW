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
transformer = pyproj.Transformer.from_crs("EPSG:4326","EPSG:3857",always_xy=True)
print(puntos)

# Crear mapa centrado aproximadamente en Asturias.
m = folium.Map(
    location=[43.35, -5.85],
    zoom_start=10,
    tiles="OpenStreetMap"
)
folium.Polygon(
    locations=puntos,
    color="red",
    fillcolor="purple",
    weight=4,
    opacity=0.8
).add_to(m)
m.save("mapa_carreño.html")