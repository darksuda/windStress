import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

year = '1997'

time_numbers = ['01-01', '02-01', '03-01', '04-01', '05-01', '06-01', '07-01', '08-01', '09-01', '10-01', '11-01','12-01']
months = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']

data_hist_65 = pd.read_csv(f'data/hist/data_hist_noaabuoys_winds_1990_0n165e.csv')
data_hist_80 = pd.read_csv(f'data/hist/data_hist_noaabuoys_winds_1990_0n180w.csv')
data_hist_70 = pd.read_csv(f'data/hist/data_hist_noaabuoys_winds_1990_0n170w.csv')

data_year_65 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_0n165e.csv')
data_year_80 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_0n180w.csv')
data_year_70 = pd.read_csv(f'data/year/data_year_noaabuoys_winds_{year}_0n170w.csv')

data_year_65['anom_u'] = data_year_65['winds_u'] - data_hist_65['winds_u']
data_year_80['anom_u'] = data_year_80['winds_u'] - data_hist_80['winds_u']
data_year_70['anom_u'] = data_year_70['winds_u'] - data_hist_70['winds_u']

fig, ax = plt.subplots(1,3, figsize=(19,3.5))

a = np.zeros(365)
a[:] = np.nan 

ax[0].plot(a, data_hist_65['time2'])
ax[0].barh(data_year_65[data_year_65['winds_u']>=0]['time2'], data_year_65[data_year_65['winds_u']>=0]['winds_u'], color='red')
ax[0].barh(data_year_65[data_year_65['winds_u']<0]['time2'], data_year_65[data_year_65['winds_u']<0]['winds_u'], color='blue')
ax[0].set_title('BOYA = 0N165E', fontsize=10)

ax[1].plot(a, data_hist_80['time2'])
ax[1].barh(data_year_80[data_year_80['winds_u']>=0]['time2'], data_year_80[data_year_80['winds_u']>=0]['winds_u'], color='red')
ax[1].barh(data_year_80[data_year_80['winds_u']<0]['time2'], data_year_80[data_year_80['winds_u']<0]['winds_u'], color='blue')
ax[1].set_title('BOYA = 0N180W', fontsize=10)

ax[2].plot(a, data_hist_70['time2'])
ax[2].barh(data_year_70[data_year_70['winds_u']>=0]['time2'], data_year_70[data_year_70['winds_u']>=0]['winds_u'], color='red')
ax[2].barh(data_year_70[data_year_70['winds_u']<0]['time2'], data_year_70[data_year_70['winds_u']<0]['winds_u'], color='blue')
ax[2].set_title('BOYA = 0N170W', fontsize=10)

for axi in ax:
    axi.set_xbound(-12, 12)
    axi.set_ybound('01-01', '12-31')
    axi.set_xticks(np.arange(-12, 13, 4), fontsize=2.5)
    axi.set_yticks(time_numbers, months)
    axi.axhline(y='06-01', color='red', linestyle='dashed')

plt.suptitle(f'Wind Stress histórico', fontsize=8)
plt.savefig(f'plots/ws/3years/ws_0n_165e_180w_170w_{year}.png')

