#-------------------------Install Packages in CoLab
!pip install geopandas
!pip install rasterio

#-------------------------ArcGIS “Summary Statistics” in Geoprocessing  
import pandas as pd

# create example DataFrame
data = {'A': [100, 100, 200, 200, 300, 400],
        'B': [1, 3, 7, 23, 43, 12]}
df = pd.DataFrame(data)

# calculate sum of values in column 'B' for unique values in column 'A'
sums = df.groupby('A')['B'].sum().reset_index()

# merge sums with original DataFrame
df = df.merge(sums, on='A')

# drop rows with duplicate values in column 'A'
df = df.drop_duplicates(subset='A')

# rename 'B' column to 'B_orig' and 'B_y' column to 'C'
df = df.rename(columns={'B': 'B_orig', 'B_y': 'C'})

print(df)

#-------------------------Extract value to points
#import required libraries
%matplotlib inline
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio
from rasterio.plot import show
import pandas as pd

#open point shapefile
pointData = gpd.read_file(r'C:\Users\arasht\OneDrive\0-TAMU\AAL Flood\Geopandas\extractPointDatafromRasterFile\Shp\pointData.shp')
print(pointData.crs)
pointData.plot()

#open raster file
ndviRaster = rasterio.open(r'C:\Users\arasht\OneDrive\0-TAMU\AAL Flood\Geopandas\extractPointDatafromRasterFile\Rst\ndviImage.tiff')
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

#-------------------------Set shapefile or raster to specefic coordinate system
import geopandas as gpd
gdf = gpd.read_file('my_shapefile.shp')  # read in the shapefile
gdf.crs = 'EPSG:32611'  # set the CRS to UTM zone 11N

#-------------------------convert xy values to a shapefile
import pandas as pd

df = pd.read_excel(r'C:\Users\arasht\OneDrive\0-TAMU\points.xlsx')

#Create a new geopandas GeoDataFrame using the latitude and longitude columns
import geopandas as gpd
from shapely.geometry import Point

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]

gdf = gpd.GeoDataFrame(df, crs='EPSG:4326', geometry=geometry)

#Save the GeoDataFrame as a shapefile
gdf.to_file(r'C:\Users\arasht\OneDrive\0-TAMU\points.shp', driver='ESRI Shapefile')

#-------------------------select points inside a polygon
import geopandas as gpd

# Import the polygon shapefile
polygon = gpd.read_file(r'C:\Users\arasht\OneDrive - Texas A&M University\Documents\0_tamu_modeling\GIS_General_Files\TexasCounties_HarrisCounty\Harris_County.shp')

# Import the points shapefile
points = gpd.read_file(r'C:\Users\arasht\OneDrive - Texas A&M University\Documents\0_tamu_modeling\GIS_General_Files\points.shp')

# Select points inside the polygon
selected_points = points[points.within(polygon.geometry.iloc[0])]

# Print the selected points
print(selected_points)
selected_points.to_csv(r'C:\Users\arasht\OneDrive - Texas A&M University\Documents\0_tamu_modeling\GIS_General_Files\selected_points.csv')

#-------------------------Convert shapefile data (e.g., NSI) to csv
import geopandas as gpd
import pandas as pd

# Read the shapefile
shapefile_path = 'path/to/your/shapefile.shp'
gdf = gpd.read_file(shapefile_path)

# Convert the geometry column to WKT (Well-Known Text) format
gdf['geometry'] = gdf['geometry'].apply(lambda geom: geom.wkt)

# Convert the GeoDataFrame to a DataFrame
df = pd.DataFrame(gdf)

# Save the DataFrame to a CSV file
csv_file_path = 'path/to/your/output.csv'
df.to_csv(csv_file_path, index=False)
#-------------------------Convert NSI data to CSV
import geopandas as gpd

# Read the GeoPackage file
gdf = gpd.read_file('input.gpkg')

# Convert to shapefile
shapefile_path = 'output.shp'
gdf.to_file(shapefile_path)

# Read the shapefile
shapefile_gdf = gpd.read_file(shapefile_path)

# Convert to CSV
csv_path = 'output.csv'
shapefile_gdf.to_csv(csv_path, index=False)
#-------------------------


