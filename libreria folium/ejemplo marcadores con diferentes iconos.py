import folium

m = folium.Map(
    location=[43.3614, -5.8593],
    zoom_start=13
)

# Marcador 1
folium.Marker(
    location=[43.3614, -5.8593],        #Los marcadores pueden crearse solamente poniendo location[]
    popup=folium.Popup(                 #Le añadimos un texto para cuando pulsemos el marcador
        """
        <b>Oviedo</b><br>
        Asturias, España<br>
        <br>
        <b>Población:</b> 215.000 hab.<br>
        <b>Tipo:</b> Ciudad
        """,
        max_width=300
    ),
    tooltip="Oviedo",                   #Nombre del marcador
    icon=folium.Icon(                   #Icono, no es obligatorio, para el marcador
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

m.save("mapa.html")
