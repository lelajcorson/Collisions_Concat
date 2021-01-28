# -*- coding: utf-8 -*-

import pandas as pd
import os

imports = 'C://Lela/Math Modeling/Collision_Data/'

file_names = []
for(dirpath, dirnames, filenames) in os.walk(imports):
    file_names.extend(filenames)
    files = pd.Series(file_names)
    break

collision_files = files[files.str.contains('Collision')]

data = pd.DataFrame()

for file in collision_files:
    this_data = pd.read_csv(imports + file)
    
    if data.empty:
        data = this_data
        
    else:
        data = pd.concat([data, this_data])
        
data.to_csv('C://Lela/Math Modeling/concat_output.csv', header = False, line_terminator = '\r')

#data['COLLISION_DATE'] = pd.to_datetime(data['COLLISION_DATE'], format = '%Y/%m/%d')
#data['COLLISION_YEAR'] = data['COLLISION_DATE'].dt.year

# key_list = range(len(data.index))
# data.set_index(key_list)

index_not_2019 = data['ACCIDENT_YEAR'] != 2009
data = data[index_not_2019]
     
print(data)

grouped_data = data.groupby(by = ['COUNTY', 'ACCIDENT_YEAR']).count()
grouped_data.to_csv('C://Lela/Math Modeling/concat_output_grouped.csv', header = False, line_terminator = '\r')
