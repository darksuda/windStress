import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

buoy = '0n170w'

time_numbers = ['01-01', '02-01', '03-01', '04-01', '05-01', '06-01', '07-01', '08-01', '09-01', '10-01', '11-01','12-01']
months = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']


data_hist = pd.read_csv(f'data/hist/data_hist_noaabuoys_winds_1990_{buoy}.csv')
data_1997 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_1997_{buoy}.csv')
data_2015 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_2015_{buoy}.csv')
data_2023 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_2023_{buoy}.csv')

data_1997['anom_u'] = data_1997['winds_u'] - data_hist['winds_u']
data_2015['anom_u'] = data_2015['winds_u'] - data_hist['winds_u']
data_2023['anom_u'] = data_2023['winds_u'] - data_hist['winds_u']

fig, ax = plt.subplots(1,4, figsize = (19,3.5))
a = np.zeros(365)
a[:] = np.nan 
ax[0].plot(a, data_hist['time2'])
ax[0].barh(data_hist[data_hist['winds_u']>=0]['time2'], data_hist[data_hist['winds_u']>=0]['winds_u'], color='red')
ax[0].barh(data_hist[data_hist['winds_u']<0]['time2'], data_hist[data_hist['winds_u']<0]['winds_u'], color='blue')

ax[1].plot(a, data_hist['time2'])
ax[1].barh(data_1997[data_1997['winds_u']>=0]['time2'], data_1997[data_1997['winds_u']>=0]['winds_u'], color='red')
ax[1].barh(data_1997[data_1997['winds_u']<0]['time2'], data_1997[data_1997['winds_u']<0]['winds_u'], color='blue')
ax[1].set_title('1997')

ax[2].plot(a, data_hist['time2'])
ax[2].barh(data_2015[data_2015['winds_u']>=0]['time2'], data_2015[data_2015['winds_u']>=0]['winds_u'], color='red')
ax[2].barh(data_2015[data_2015['winds_u']<0]['time2'], data_2015[data_2015['winds_u']<0]['winds_u'], color='blue')
ax[2].set_title('2015')

ax[3].plot(a, data_hist['time2'])
ax[3].barh(data_2023[data_2023['winds_u']>=0]['time2'], data_2023[data_2023['winds_u']>=0]['winds_u'], color='red')
ax[3].barh(data_2023[data_2023['winds_u']<0]['time2'], data_2023[data_2023['winds_u']<0]['winds_u'], color='blue')
ax[3].set_title('2023')

for axi in ax:
    axi.set_xbound(-12, 12)
    axi.set_ybound('01-01', '12-31')
    axi.set_xticks(np.arange(-12, 13, 4), fontsize=2.5)
    axi.set_yticks(time_numbers, months)
    axi.axhline(y='06-01', color='red', linestyle='dashed')

plt.suptitle(f'Wind Stress Boya {buoy}')

plt.savefig(f'plots/ws/3years/ws_1997_2015_2023_{buoy}.png')
plt.close()