import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gsw


file = open('data_pota_2.json')
data = json.load(file)
print('EL ARCHIVO TIENE: ' + str(len(data)) + ' PERFILES')

psal_start  = 34.2#
psal_end = 36.4
temp_start = 10
temp_end = 30


pres_start = 0
pres_end = 300

ids = []
platforms = []
cycles = []
lats = []
lons = []
dates = []


for p in data:
    ids.append(p['_id'])
    platforms.append(str(p['_id'][0:-4]))
    lons.append(p['geolocation']['coordinates'][0])
    lats.append(p['geolocation']['coordinates'][1])
    dates.append(p['timestamp'][0:10])
    cycles.append(p['cycle_number'])

data_df = pd.DataFrame({
    'id': ids,
    'platform': platforms,
    'cycle': cycles,
    'lat': lats,
    'lon': lons,
    'date': dates
})

data_df.to_csv('datos_oc_pq/datos_equator/resumen_data_sep_dic_2019.csv', index=False)
