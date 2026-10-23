from pyproj import Geod

geodesia = Geod(ellps="WGS84")

# Coordenadas aproximadas: Gijón y Oviedo
gijon = (-5.6615, 43.5322)
oviedo = (-5.8494, 43.3614)

azimut_inicial, azimut_final, distancia = (
    geodesia.inv(
        gijon[0], gijon[1],
        oviedo[0], oviedo[1]
    )
)

print("Distancia en metros:", distancia)
print("Azimut inicial:", azimut_inicial)
print("Azimut final:", azimut_final)