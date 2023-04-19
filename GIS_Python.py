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

-------------------------#