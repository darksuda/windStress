import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('vientos pisco.csv', sep=';')
data['time'] = [i[5:] for i in data['time']]
años = data['AÑO'].unique()

data_mean = data.groupby('time').mean(numeric_only=True).reset_index()
data_mean = data_mean.drop(data_mean[data_mean['time'] == '02-29'].index).reset_index()
data_mean = data_mean.drop('index', axis=1)

data_mean_v = np.array(data_mean['v'])
data_mean_u = np.array(data_mean['u'])

years = años

a = np.zeros(365)
a[:] = np.nan

for year in years:
    fig, ax = plt.subplots(2, figsize= (16, 9))

    ax[0].plot(data_mean['time'], a)

    ax[0].set_ylabel('vientos zonales')
    ax[0].axhline(y=0, color='red', linestyle='dotted')
    ax[0].set_xticks(['01-01', '02-01', '03-01', '04-01', '05-01', '06-01', '07-01', '08-01', '09-01', '10-01', '11-01', '12-01', '12-31'], ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC', 'ENE'])

    ax[1].plot(data_mean['time'], a)

    ax[1].set_ylabel('vientos meridionales')
    ax[1].axhline(y=0, color='red', linestyle='dotted')
    ax[1].set_xticks(['01-01', '02-01', '03-01', '04-01', '05-01', '06-01', '07-01', '08-01', '09-01', '10-01', '11-01', '12-01', '12-31'], ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC', 'ENE'])

    data_year = data[data['AÑO'] == year]
    data_year = data_year.drop(data_year[data_year['time'] == '02-29'].index).reset_index()
    u_anom = np.array(data_year['u']) - data_mean_u
    v_anom = np.array(data_year['v']) - data_mean_v
    data_year['u_anom'] = u_anom
    data_year['v_anom'] = v_anom

    ax[0].bar(data_year[data_year['u_anom'] >= 0]['time'], data_year[data_year['u_anom'] >= 0]['u_anom'], color='blue')
    ax[0].bar(data_year[data_year['u_anom'] < 0]['time'], data_year[data_year['u_anom'] < 0]['u_anom'], color='red')
    ax[1].bar(data_year[data_year['v_anom'] >= 0]['time'], data_year[data_year['v_anom'] >= 0]['v_anom'], color='blue')
    ax[1].bar(data_year[data_year['v_anom'] < 0]['time'], data_year[data_year['v_anom'] < 0]['v_anom'], color='red')
    plt.suptitle(f'vientos zonales y meridionales en Pisco\nAño: {year}')


    ax[0].set_ybound(-8, 8)
    ax[1].set_ybound(-8, 8)

    plt.tight_layout()

    plt.savefig(f'vientos_u_v_pisco_{year}.png')
    plt.close()
    #plt.show()
    