import folium
from folium.plugins import HeatMap

m = folium.Map(
    location=[43.3614, -5.8593],
    zoom_start=13
)

# Marcador 1
folium.Marker(
    location=[43.3614, -5.8593],
    popup=folium.Popup(
        """
        <b>Oviedo</b><br>
        Asturias, España<br>
        <br>
        <b>Población:</b> 215.000 hab.<br>
        <b>Tipo:</b> Ciudad
        """,
        max_width=300
    ),
    tooltip="Oviedo",
    icon=folium.Icon(
        color="blue",
        icon="info-sign"
    )
).add_to(m)

# Marcador 2
folium.Marker(
    location=[43.3650, -5.8500],
    popup=folium.Popup(
        """
        <b>Restaurante</b><br>
        Casa de ejemplo<br>
        <br>
        <b>Horario:</b><br>
        L-V: 13:00 - 23:00<br>
        S-D: 12:00 - 00:00
        """,
        max_width=300
    ),
    tooltip="Restaurante",
    icon=folium.Icon(
        color="red",
        icon="cutlery",
        prefix="fa"
    )
).add_to(m)

data = [[43.3650, -5.8500,1000],[43.3614, -5.8593,40]]   # Asocio a cada punto un valor de temperatura para el mapa
HeatMap(data).add_to(m)  #Añado el mapa de calor al mapa, Hay que importar la librería

m.save("mapa.html")
