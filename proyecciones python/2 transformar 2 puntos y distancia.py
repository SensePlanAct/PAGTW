import pyproj

#Inicializar un CRS usando EPSG
crs_wgs84=pyproj.CRS("EPSG:4326")

#Podemos transformar un punto en coordenadas WSG-84 y vamos a transformarlo a Mercator

transformer = pyproj.Transformer.from_crs("EPSG:4326","EPSG:3857",always_xy=True)

facultad =  (43.242200, -5.776861)
mcdonalds = (43.237472, -5.778420)


x_facultad, y_facultad = transformer.transform(facultad[0], facultad[1])
x_mcdonadls, y_mcdonalds = transformer.transform(mcdonalds[0], mcdonalds[1])

distancia = ((x_mcdonadls-x_facultad)**2 + (y_mcdonalds-y_facultad)**2)**0.5

# Es el teorema de pitágoras 

print (f"Distancia en metros desde la facultad a McDonalds: {distancia} metros")

