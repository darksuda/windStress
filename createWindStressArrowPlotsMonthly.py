import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import calc_wind_stress as cws
import netCDF4 as cdf 
import request_winds as rqw

def arrow_color(n):
    if n < 0:
        return '#06449c'
    else:
        return '#9c061a'


buoys = pd.read_csv('data/buoys.csv')

year = 2024

lats = ['5n', '2n', '0n', '2s', '5s']
months_names = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO','JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']


for month in  np.arange(12):
    wsu = []
    wsv = []
    for buoy in buoys['buoy']:
        try:
            rqw.request_wind_data(year, buoy)
            data = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_{buoy}.csv')
            data['wsu'] = [cws.calc_wind_stress(i, 1.204) for i in data['winds_u']]
            data['wsv'] = [cws.calc_wind_stress(i, 1.204) for i in data['winds_v']]
            data = data.groupby('month').sum(numeric_only=True).reset_index()
            data = data[data['month'] == month+1]
            wsu.append(data['wsu'].iloc[0])
            wsv.append(data['wsv'].iloc[0])
        except Exception as err:
            print(err)
            wsu.append(False)
            wsv.append(False)
            print('error con la boya')


    wsu = np.array(wsu)
    wsv = np.array(wsv)

    fig, ax = plt.subplots()
    for index, row in buoys.iterrows():
        lon = row['lon']
        lat = row['lat']
        if wsu[index]:
            ax.arrow(lon, lat, wsu[index]*3, wsv[index]*3, width=0.25, color= arrow_color(wsu[index]))
            ax.scatter(lon, lat, color='yellow', s=35, edgecolor='black')
        else:
            ax.scatter(lon, lat, color='gray', s=200, edgecolor='black', marker='X')

    ax.arrow(-175, -6.2, 1*3, 0,width=0.25, color='black', alpha=0.5)
    ax.text(-175, -5.9,'1 N/m2')
    ax.set_title(f'{months_names[month]} - {year}')
    ax.set_yticks([-5,-2,0,2,5],  ['5°S', '2°S', '0°N', '2°N', '5°N'])
    ax.set_xticks([-204,-195, -180, -170],  ['156°E', '165°E', '180°W', '170°W'])
    ax.set_ybound(-7, 7)
    ax.set_xbound(-210, -165)
    ax.grid()

    #plt.show()
    plt.savefig(f'plots/arrows/windStressByYear/{year}_{month+1}_{months_names[month]}')
    plt.close()