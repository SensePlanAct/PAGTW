from  pyproj import CRS

crs_geo = CRS.from_epsg(4326)
crs_utm = CRS.from_epsg(25830)

print("Sistema geográfico:", crs_geo.name)
print("Sistema proyectado:", crs_utm.name)

print("Unidades geográficas:",
      crs_geo.axis_info)

print("Unidades proyectadas:",
      crs_utm.axis_info)