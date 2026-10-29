"""
    @autor: Rodrigo
    @date: 29/10/2026
    @email: uo312563@uniovi.es

"""
from pyproj import Geod

geodesia = Geod(ellps="WGS84")
punto_wgs84_1 = (-5, 43)
punto_wgs84_3 = (-76, 43)
azimut_inicial, azimut_final, distancia = (
    geodesia.inv(
        punto_wgs84_1[0], punto_wgs84_1[1],
        punto_wgs84_3[0], punto_wgs84_3[1]
    )
)
print("Distancia en metros:", distancia)
print("Azimut inicial:", azimut_inicial)
print("Azimut final:", azimut_final)
print(geodesia.fwd(-5,43,azimut_inicial,distancia))
print(geodesia.npts(-5,43,-76,43,4))