import math
import folium
lat1 = float(input("Introduce la latitud de origen: "))
lon1 = float(input("Introduce la longitud de origen: "))
lat2 = float(input("Introduce la latitud de destino: "))
lon2 = float(input("Introduce la longitud de destino: "))
def distancia_haversine(coord1, coord2):

    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371.0  # radio tierra
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
def distancia_euclidea(coord1, coord2):

    # Extraer latitudes y longitudes
    RADIO_TIERRA = 6371.0
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convertir todas las coordenadas de grados a radianes
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon1_rad = math.radians(lon1)
    lon2_rad = math.radians(lon2)

    # Calcular la latitud media para corregir el estrechamiento de los meridianos
    lat_media = (lat1_rad + lat2_rad) / 2.0

    # Calcular la diferencia en el eje X (Longitud) corregida por la latitud
    x = (lon2_rad - lon1_rad) * math.cos(lat_media)

    # 4. Calcular la diferencia en el eje Y (Latitud)
    y = lat2_rad - lat1_rad

    # 5. Aplicar el Teorema de Pitágoras (hipotenusa) y multiplicar por el radio
    distancia = math.sqrt(x ** 2 + y ** 2) * RADIO_TIERRA


    return distancia
punto_origen = [lat1, lon1]
punto_destino = [lat2, lon2]
distancia_hav = distancia_haversine(punto_origen, punto_destino)
distancia_euc = distancia_euclidea(punto_origen, punto_destino)
m = folium.Map(location=[lat1, lon1], zoom_start=3)
folium.Marker(location=punto_origen, icon=folium.Icon(color="red"), popup="Península Ibérica").add_to(m)
folium.Marker(location=punto_destino, icon=folium.Icon(color="red"), popup="América").add_to(m)

punto3=[((lat1+lat2)/2)-3, ((lon1+lon2)/2)-1]
linea = [punto_origen,punto3,punto_destino]

folium.PolyLine(
    locations=linea,
    color="yellow",
    tooltip=f"Distancia Haversine: {distancia_hav} km"
).add_to(m)


folium.PolyLine(locations=[punto_origen, punto_destino], color="gray", dash_array="5",tooltip=f'Distancia Euclidea: {distancia_euc}').add_to(m)
m.save("mapa1.html")