import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('tabla.csv')
data.columns=['year', 'month', 'nino_1+2', 'anom_1+2', 'nino_3', 'anom_3', 'nino_4', 'anom_4', 'nino_3.4', 'anom_3.4']

yi = 2022
yf = 2023

d8283= data[(data['year']>=yi)&((data['year']<=yf))]

fig, ax = plt.subplots(figsize=(7,4))

#AREA  EL NIÑO 1+2
ax.plot(np.arange(1,25), d8283['nino_1+2'], label=f'{yi} - {yf} (1+2)', color='#1466e0', linewidth=0.8)
ax.plot(np.arange(1,25), d8283['nino_1+2']-d8283['anom_1+2'], label=f'hist (1+2)', color='black', linewidth=2.5)
ax.scatter(np.arange(1,25), d8283['nino_1+2'], marker='v', color='#1466e0', s=7)

#AREA  EL NIÑO 3.4
ax.plot(np.arange(1,25), d8283['nino_3.4'], label=f'{yi} - {yf} (3.4)', color='red', linewidth=0.8)
ax.plot(np.arange(1,25), d8283['nino_3.4']-d8283['anom_3.4'], label=f'hist (3.4)', color='#ff0000', linewidth=2.5)
ax.scatter(np.arange(1,25), d8283['nino_3.4'], color='red', s=7)

ax.set_xticks(np.arange(1,25), ['E', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D', 'E', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])
ax. axvline(x=12.5)
ax. axhline(y=0, color= '#bd0250', linestyle='dashed')

ax.set_ybound(20, 30)

ax.grid()
ax.legend(fontsize=7)

plt.savefig(f'plots/enso/temp{yi}-{yf}')
plt.show()
