from shapely.geometry import Polygon
from shapely import transform
from pyproj import Transformer

# Polígono aproximado en las proximidades de Gijón
vertices = [
    (-5.67, 43.53),
    (-5.65, 43.53),
    (-5.65, 43.54),
    (-5.67, 43.54),
    (-5.67, 43.53)
]

poligono_geo = Polygon(vertices)

transformador = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:25830",
    always_xy=True
)

poligono_utm = transform(
    poligono_geo,
    transformador.transform,
    interleaved=False
)

print("Área en m²:", poligono_utm.area)
print("Área en hectáreas:", poligono_utm.area / 10000)
print("Perímetro en m:", poligono_utm.length)