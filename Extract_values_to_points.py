#Besmellaherrahmanerahim

#-------------------------Install Packages in CoLab
!pip install geopandas
!pip install rasterio

#-------------------------Extract value to points
#import required libraries
%matplotlib inline
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio
from rasterio.plot import show
import pandas as pd

#open point shapefile
pointData = gpd.read_file(r'C:\Arash\harris_nsi\48201.shp')
print(pointData.crs)
pointData.plot()

#open raster file
ndviRaster = rasterio.open(r'C:\Arash\flooddepth\floodmap_sbg_0.1_hmin_500yr.tif')
print(ndviRaster.crs)
#count number of bands
print(ndviRaster.count)

#show point and raster on a matplotlib plot
fig, ax = plt.subplots(figsize=(12,12))
pointData.plot(ax=ax, color='orangered')
show(ndviRaster, ax=ax)

#extract xy from point geometry
for point in pointData['geometry']:
    print(point.xy[0][0],point.xy[1][0])

#extract point value from raster
#put the results in a data frame
rows_list = []
for point in pointData['geometry']:
    x = point.xy[0][0]
    y = point.xy[1][0]
    row, col = ndviRaster.index(x,y)
    try:
        ndvi_value = ndviRaster.read(1)[row,col]
    except:
        print(x, y,)
    print(x, y,)
    rows_list.append({'row': row, 'col': col, 'ndvi_value': ndvi_value})

df = pd.DataFrame(rows_list)



print(pointData.crs)
print(ndviRaster.crs)


#points epsg:4326
#reaster EPSG:32615

import geopandas as gpd
gdf = gpd.read_file(r'C:\Arash\harris_nsi\48201.shp')  # read in the shapefile
gdf.to_crs('EPSG:32615')
print(gdf.head())



#-------------------------Convert shapefile data (e.g., NSI) to csv
import geopandas as gpd
import pandas as pd

# Read the shapefile
shapefile_path = r'C:\Arash\harris_nsi\48201.shp'
gdf = gpd.read_file(shapefile_path)

# Convert the geometry column to WKT (Well-Known Text) format
gdf['geometry'] = gdf['geometry'].apply(lambda geom: geom.wkt)

# Convert the GeoDataFrame to a DataFrame
df = pd.DataFrame(gdf)

# Save the DataFrame to a CSV file
csv_file_path = 'path/to/your/output.csv'
df.to_csv(csv_file_path, index=False)

#-----------------------------Bard code

import geopandas as gpd
import rasterio

# Load your GeoDataFrame containing the points
gdf = gpd.read_file(r'C:\Arash\harris_nsi\48201.shp')

# Load the raster data
with rasterio.open(r'C:\Arash\flooddepth\floodmap_sbg_0.1_hmin_500yr.tif') as src:
    # Check for matching CRS (Coordinate Reference System)
    if src.crs != gdf.crs:
        print("Warning: CRS of points and raster don't match. Reprojecting points...")
        gdf = gdf.to_crs(src.crs)

    # Extract coordinates as required by Rasterio
    coord_list = [(X, Y) for X, Y in zip(gdf["geometry"].X, gdf["geometry"].Y)]

    # Extract values and add them to the GeoDataFrame
    gdf["value"] = [X for X in src.sample(coord_list)]

# Print the results
print(gdf)

#-----------------------------Bard code

import geopandas as gpd
import rasterio

# Load your GeoDataFrame containing the points
gdf = gpd.read_file(r'C:\Arash_SP\Flood AAL\Data\NSI\NSI Brays Bayou\c_NSI_Points2.shp')

# Load the raster data
with rasterio.open(r'C:\Arash_SP\Flood AAL\Data\aal_data_pipeline_example\flood_probability_data\Mosaic\500.tif') as src:
    # Check for matching CRS (Coordinate Reference System)
    if src.crs != gdf.crs:
        print("Warning: CRS of points and raster don't match. Reprojecting points...")
        gdf = gdf.to_crs(src.crs)

    # Extract coordinates as required by Rasterio
    coord_list = [(x, y) for x, y in zip(gdf["geometry"].x, gdf["geometry"].y)]

    # Extract values and add them to the GeoDataFrame
    gdf["value"] = [x for x in src.sample(coord_list)]

# Print the results
print(gdf)

#-------------------------Extract value to points
#import required libraries
%matplotlib inline
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio
from rasterio.plot import show
import pandas as pd

#open point shapefile
pointData = gpd.read_file(r'C:\Arash_SP\Flood AAL\Data\NSI\NSI Brays Bayou\c_NSI_Points2.shp')
print(pointData.crs)
pointData.plot()

#open raster file
ndviRaster = rasterio.open(r'C:\Arash_SP\Flood AAL\Data\aal_data_pipeline_example\flood_probability_data\Mosaic\500.tif')
print(ndviRaster.crs)
#count number of bands
print(ndviRaster.count)

#show point and raster on a matplotlib plot
fig, ax = plt.subplots(figsize=(12,12))
pointData.plot(ax=ax, color='orangered')
show(ndviRaster, ax=ax)

#extract xy from point geometry
for point in pointData['geometry']:
    print(point.xy[0][0],point.xy[1][0])

#extract point value from raster
#put the results in a data frame
rows_list = []
for point in pointData['geometry']:
    x = point.xy[0][0]
    y = point.xy[1][0]
    row, col = ndviRaster.index(x,y)
    ndvi_value = ndviRaster.read(1)[row,col]
    rows_list.append({'row': row, 'col': col, 'ndvi_value': ndvi_value})

df = pd.DataFrame(rows_list)

df.to_csv(r"C:\Arash IDRT\e v t p.csv")

#------------------------------------gpt2
import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask

# Load the shapefile with points
points_gdf = gpd.read_file(r'C:\Arash_SP\Flood AAL\Data\NSI\NSI Brays Bayou\c_NSI_Points2.shp')

# Load the raster file
raster_path = r'C:\Arash_SP\Flood AAL\Data\aal_data_pipeline_example\flood_probability_data\Mosaic\500.tif'
raster = rasterio.open(raster_path)

# Extract pixel values at points
points_gdf['raster_value'] = points_gdf.apply(
    lambda row: list(raster.sample([(row.geometry.x, row.geometry.y)]))[0],
    axis=1
)

# Close the raster file
raster.close()

# Print the GeoDataFrame with raster values
print(points_gdf)

points_gdf.to_csv(r"C:\Arash IDRT\e v t p.csv")

#----------------------------------------------
import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask
from shapely.geometry import Point

# Load your GeoDataFrame containing the points
gdf = gpd.read_file(r'C:\Arash_SP\Flood AAL\Data\NSI\NSI Brays Bayou\c_NSI_Points2.shp')

# Load the raster data
raster_path = r'C:\Arash_SP\Flood AAL\Data\aal_data_pipeline_example\flood_probability_data\Mosaic\500.tif'
with rasterio.open(raster_path) as src:
    # Check for matching CRS (Coordinate Reference System)
    if src.crs != gdf.crs:
        print("Warning: CRS of points and raster don't match. Reprojecting points...")
        gdf = gdf.to_crs(src.crs)

    # Create Point geometries from the x, y coordinates in the GeoDataFrame
    geometry = [Point(xy) for xy in zip(gdf['x_column'], gdf['y_column'])]  # Replace 'x_column' and 'y_column'

    # Update the GeoDataFrame with the new Point geometries
    gdf = gpd.GeoDataFrame(gdf, geometry=geometry, crs=src.crs)

    # Extract pixel values at points
    gdf['raster_value'] = list(src.sample(gdf.geometry))

# Print the updated GeoDataFrame with raster values
print(gdf)








#C:\Arash_SP\Flood AAL\Data\NSI\NSI Brays Bayou\c_NSI_Points2.shp
#C:\Arash_SP\Flood AAL\Data\aal_data_pipeline_example\flood_probability_data\Mosaic\500.tif

#C:\Arash IDRT\e v t p.csv







