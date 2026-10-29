from operator import inv

from pyproj import Geod
from shapely.creation import points
from shapely.geometry import geo

lat1 = float(input("Introduce la latitud de origen: "))
lon1 = float(input("Introduce la longitud de origen: "))

lat2 = float(input("Introduce la latitud de destino: "))
lon2 = float(input("Introduce la longitud de destino: "))
geod=Geod(ellps="WGS84")
az1, az2, dist = geod.inv(lon1,lat1,lon2,lat2)
print(az1,az2,dist)
points=geod.npts(lon1,lat1,lon2,lat2,4)
print(points)
lon2, lat2, dist = geod.fwd(lon1,lat1,az1,15000)
print(lon2,lat2)