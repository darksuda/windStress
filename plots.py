import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import calc_wind_stress as cws
import request_winds as rqw
import request_iso as rqi
import request_dyn as rqd

buoy = '0n165e'
hist = '1990'
years = ['2015']

rqw.request_wind_historical_data(hist, buoy)
data = pd.read_csv(f'data\hist\data_hist_noaabuoys_winds_{hist}_{buoy}.csv')

time = data['time2']
month = data['month']
u = data['winds_u']
u = [np.round(cws.calc_wind_stresss(wu, 1022), 3) for wu in u]

data_ws = pd.DataFrame()
data_ws['month'] = month
data_ws['wind_stress'] = u
data_ws_sum = data_ws.groupby('month').sum()['wind_stress']

data_ws = data_ws.groupby('month').describe()
data_ws['sum'] = data_ws_sum

for year in years:
    rqw.request_wind_data(year, buoy)
    data_year = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_{buoy}.csv')
    u_year = data_year['winds_u']
    u_year = [np.round(cws.calc_wind_stresss(wu, 1022), 3) for wu in u_year]
    
    data_ws_year = pd.DataFrame()
    data_ws_year['month'] = data_year['month']
    data_ws_year['wind_stress'] = u_year
    data_ws_year_sum = data_ws_year.groupby('month').sum()['wind_stress']

    data_ws_year = data_ws_year.groupby('month').describe()
    data_ws_year['sum'] = data_ws_year_sum

fig, ax = plt.subplots(3)
fig2, ax2 = plt.subplots()

ax[0].plot(time, u, label = 'Histórico')
ax[0].axhline(y=0, color="#c3093f", linestyle = 'dotted')
ax[0].set_ylabel('wind stress')

for year in years:
    rqw.request_wind_data(year, buoy)
    data_year = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_{buoy}.csv')
    u_year = data_year['winds_u']
    u_year = [np.round(cws.calc_wind_stresss(wu, 1022), 3) for wu in u_year]
    time_year = data_year['time2']
    ax[0].plot(time_year, u_year, linestyle = 'dashed', label = data_year['year'][0])

ax[0].set_xticks(['01-01', '03-01', '05-01', '07-01', '09-01', '11-01', '12-31'], ['ENE', 'MAR', 'MAY', 'JUL', 'SEP', 'NOV', 'ENE'])

ax[0].set_title(f'{buoy}')
ax[0].legend()





rqd.init_dyn_data_download(buoy)

rqd.request_dyn_historical_data(hist, buoy)
data = pd.read_csv(f'data\hist\data_hist_noaabuoys_dyn_{hist}_{buoy}.csv')
time = data['time2']
month = data['month']
dyn = data['dyn']

ax[1].plot(time, dyn, label = 'Histórico')
ax2.plot(time, dyn, label = 'Histórico altura dinámica')
ax[1].set_xticks(['01-01', '03-01', '05-01', '07-01', '09-01', '11-01', '12-31'], ['ENE', 'MAR', 'MAY', 'JUL', 'SEP', 'NOV', 'ENE'])

for year in years:
    rqd.request_dyn_data(year, buoy)
    data_year = pd.read_csv(f'data/year/data_year_noaabuoys_dyn_{year}_{buoy}.csv')
    dyn = data_year['dyn']
    time_year = data_year['time2']
    ax[1].plot(time_year, dyn, linestyle = 'dashed', label = data_year['year'][0])
    ax2.plot(time_year, dyn, linestyle = 'dashed', label = data_year['year'][0])

ax[1].legend()
ax[1].set_ylabel('Altura dinámica')




rqi.init_iso_data_download(buoy)

rqi.request_iso_historical_data(hist, buoy)
data = pd.read_csv(f'data\hist\data_hist_noaabuoys_iso_{hist}_{buoy}.csv')
time = data['time2']
month = data['month']
iso = data['iso']

ax[2].plot(time, iso, label = 'Histórico')
ax2.plot(time, iso * -1, label = 'Histórico isoterma')
ax[2].set_xticks(['01-01', '03-01', '05-01', '07-01', '09-01', '11-01', '12-31'], ['ENE', 'MAR', 'MAY', 'JUL', 'SEP', 'NOV', 'ENE'])

for year in years:
    rqi.request_iso_data(year, buoy)
    data_year = pd.read_csv(f'data/year/data_year_noaabuoys_iso_{year}_{buoy}.csv')
    iso = data_year['iso']
    time_year = data_year['time2']
    ax[2].plot(time_year, iso, linestyle = 'dashed', label = data_year['year'][0])
    ax2.plot(time_year, iso * - 1, linestyle = 'dashed', label = data_year['year'][0])

ax[2].legend()
ax[2].invert_yaxis()
ax[2].set_ylabel('Isoterma de 20°C')


ax2.legend()


plt.show()