from pyproj import Transformer

lon = -5.6615
lat = 43.5322

#CREO UN TRANSFORMADOR

transformador = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:25830",
    always_xy=True
)

#ALWAYS XY=TRUE establece que los argumentos de entrada sean longitud y
#latitud, en ese orden, evitando confusiones con el orden de ejes

#AQUI EJECUTO EL TRANSFORMADOR

x, y = transformador.transform(lon, lat)

print("Coordenada X:", x)
print("Coordenada Y:", y)