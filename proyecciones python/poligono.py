import pyproj
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely import transform
import csv
puntos=[]
c = open("../carreno_lat_lon.csv")
with c as file:
    contenido = csv.DictReader(file, delimiter=',') #si el fichero tiene una fila con los nombres de las columnas no necesito ponerlo, en caso contrario tengo que añadir
    #un parámetro que sea fieldnames=['campo1','campo2','campo3',...] para que me cree las entradas correctas en los diccionarios.
    campos = (contenido.fieldnames) #me guarda los nombres de las columnas en el caso de que el fichero las tenga
    for fila in contenido:  #recorro todas las filas que he leido del fichero
        punto=fila[campos[0]],fila[campos[1]]
        puntos.append(punto)
transformer = pyproj.Transformer.from_crs("EPSG:4326","EPSG:3857",always_xy=True)
print(puntos)
poligono_wgs84 = Polygon([latitud,longitud])

proyeccion = lambda x, y: transformer.transform(x,y)
poligono = transform(poligono_wgs84, proyeccion,interleaved=False)

print(poligono)

area = poligono.area
print (f"Área del polígono: {area} metros cuadrados")

punto = Point((43.3623,-5.8475))

punto_con_buffer=transform(punto,proyeccion,interleaved=False)

buffer_punto = punto_con_buffer.buffer(500)

print (buffer_punto)

#rabilar = lambda x, y: (x+y)**2
#print (rabilar(3,2))


otro_poligono = Polygon([(43.3600, -5.8500),
                         (43.3650, -5.8500),
                         (43.3650, -5.8450),
                         (43.3600, -5.8450)])

poligono2_proyectado = transform(otro_poligono,proyeccion,interleaved=False)

if otro_poligono.intersects(poligono):
    #Obtener la geometría de la proyección
    interseccion = otro_poligono.intersection(poligono)
    print ("Si intersecta")
    print (interseccion)
else:
    print ("No intersecan")