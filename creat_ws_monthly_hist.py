import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import calc_wind_stress as cws

"""
#CREA LOS HISTORICOS DE SUMA MENSUAL DE CADA BOYA EN WS
buoys = pd.read_csv('data/buoys.csv')['buoy']

#buoy = '0n180w'
for buoy in buoys:
    data = pd.read_csv(f'data/hist/data_hist_noaabuoys_winds_1990_{buoy}.csv')
    data['wsu'] = [cws.calc_wind_stress(i, 1.204) for i in data['winds_u']]
    data['wsv'] = [cws.calc_wind_stress(i, 1.204) for i in data['winds_v']]
    data = data.groupby('month').sum(numeric_only=True).reset_index()
    data = data[['month','wsu', 'wsv']]
    data['month'] = [int(i) for i in data['month']]
    data.to_csv(f'data/ws/data_ws_monthly_sum_hist_{buoy}.csv', index=False)
"""
def arrow_color(n):
    if n < 0:
        return '#06449c'
    else:
        return '#9c061a'

months_names = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO','JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
lats = ['5n', '2n', '0n', '2s', '5s']

month = 0
for month in range(12):
    buoys = pd.read_csv('data/buoys.csv')
    data_wsu = []
    data_wsv = []
    for buoy in buoys['buoy']:
        data_wsu.append(pd.read_csv(f'data/ws/data_ws_monthly_sum_hist_{buoy}.csv').iloc[month]['wsu'])
        data_wsv.append(pd.read_csv(f'data/ws/data_ws_monthly_sum_hist_{buoy}.csv').iloc[month]['wsv'])

    data_ws = np.array([data_wsu, data_wsv]).T

    fig, ax = plt.subplots()

    for index, row in buoys.iterrows():
        lon = row['lon']
        lat = row['lat']
        ax.arrow(lon, lat, data_ws[index][0]*3, data_ws[index][1]*3, width=0.15, color= arrow_color(data_ws[index][0]))
    
    ax.arrow(-175, -6.2, 1*3, 0,width=0.25, color='black', alpha=0.5)
    ax.text(-175, -5.9,'1 N/m2')
    ax.set_title(f'{months_names[month]}')
    ax.set_yticks([-5,-2,0,2,5],  ['5°S', '2°S', '0°N', '2°N', '5°N'])
    ax.set_xticks([-204,-195, -180, -170],  ['156°E', '165°E', '180°W', '170°W'])
    ax.set_ybound(-7, 7)
    ax.set_xbound(-210, -165)
    ax.grid()

    #plt.show()

    plt.savefig(f'plots/hist_month_ws/{month+1}_{months_names[month]}')
    plt.close()