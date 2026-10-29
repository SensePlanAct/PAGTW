import geopandas as gpd

# Sustituir por la ruta al archivo descargado.
archivo = "asturias.gpkg"

gdf = gpd.read_file(archivo)

# Inspeccionar la estructura antes de filtrar.
print(gdf.columns)
print(gdf.head())
print("CRS:", gdf.crs)