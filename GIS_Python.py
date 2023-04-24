-------------------------#ArcGIS “Summary Statistics” in Geoprocessing  
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

-------------------------#Extraxt value to points
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

-------------------------#
