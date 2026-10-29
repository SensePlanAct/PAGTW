
import folium
from shapely.geometry import Polygon
from shapely.ops import transform
from pyproj import Transformer

# Cada polígono está definido en (longitud, latitud).
parcelas_coords = {
    "P1 - Oviedo": [
        (-5.870, 43.350),
        (-5.840, 43.350),
        (-5.840, 43.375),
        (-5.870, 43.375),
        (-5.870, 43.350)
    ]
}

# Crear geometrías Shapely.
parcelas_geo = {
    nombre: Polygon(coords)
    for nombre, coords in parcelas_coords.items()
}

# Crear mapa centrado aproximadamente en Asturias.
mapa = folium.Map(
    location=[43.35, -5.85],
    zoom_start=10,
    tiles="OpenStreetMap"
)

colores = {
    "P1 - Oviedo": "blue",
    "P2 - Oviedo": "green",
    "P3 - Gijón": "orange",
    "P4 - Gijón": "red",
    "P5 - Mieres": "purple"
}

# Folium espera las coordenadas como [latitud, longitud].
for nombre, poligono in parcelas_geo.items():
    folium.GeoJson(
        data={
            "type": "Feature",
            "properties": {"nombre": nombre},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [lon, lat] for lon, lat
                    in parcelas_coords[nombre]
                ]]
            }
        },
        name=nombre,
        style_function=lambda feature, n=nombre: {
            "color": colores[n],
            "fillColor": colores[n],
            "weight": 3,
            "fillOpacity": 0.30
        },
        tooltip=nombre
    ).add_to(mapa)

folium.LayerControl().add_to(mapa)
mapa.fit_bounds([
    [43.24, -5.89],
    [43.56, -5.63]
])

mapa.save("parcelas_asturias.html")

print("Mapa creado: parcelas_asturias.html")
