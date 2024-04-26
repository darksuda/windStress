import request_winds as rqw 
import calc_wind_stress as cws
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sideFunctions as sdf


buoys = [
        '0n147e', '2n147e', '5n147e', '8n147e', '2s147e', '5s147e', '8s147e',
        '0n165e', '2n165e', '5n165e', '8n165e', '2s165e', '5s165e', '8s165e',
        '0n156e', '2n156e', '5n156e', '8n156e', '2s156e', '5s156e', '8s156e',
        '0n180w', '2n180w', '5n180w', '8n180w', '2s180w', '5s180w', '8s180w',
        '0n170w', '2n170w', '5n170w', '8n170w', '2s170w', '5s170w', '8s170w'
        ]
buoys = [
        '0n147e', '2n147e', '5n147e', '8n147e', '2s147e', '5s147e', '8s147e',
        '0n165e', '2n165e', '5n165e', '8n165e', '2s165e', '5s165e', '8s165e',
        '0n156e', '2n156e', '5n156e', '8n156e', '2s156e', '5s156e', '8s156e',
        '0n180w', '2n180w', '5n180w', '8n180w', '2s180w', '5s180w', '8s180w',
        '0n170w', '2n170w', '5n170w', '8n170w', '2s170w', '5s170w', '8s170w'
        ]
for buoy in buoys:
        
    year_hist = '1990'

    for year in ['1991', '1992', '1997', '1998',  '1999', '2000', '2015', '2016', '2017', '2023']:
        try:
            
            print(f'{buoy} - {year}')
                
            rqw.init_wind_data_download(buoy)

            hist_dir = rqw.request_wind_historical_data(year_hist, buoy)
            year_dir = rqw.request_wind_data(year, buoy)

            data_hist = pd.read_csv(hist_dir)
            data_year = pd.read_csv(year_dir)

            data_year = data_year.drop(data_year[data_year['time2'] == '02/29'].index).reset_index()

            a = np.zeros(365)
            a[:] = np.nan


            data_hist['wsu'] = [cws.calc_wind_stress(u, 1.2) for u in data_hist['winds_u']] 

            data_year['wsu'] = [cws.calc_wind_stress(u, 1.2) for u in data_year['winds_u']]
            data_year['anom_u'] = data_year['winds_u'] - data_hist['winds_u']
            data_year['anom_wsu'] = data_year['wsu'] - data_hist['wsu']


            fig, ax = plt.subplots(1,3, figsize = (18, 10))

            for axi in ax:
                axi.barh(data_hist['time2'], a)


            ax[0].barh(data_hist[data_hist['wsu']<0]['time2'], data_hist[data_hist['wsu']<0]['wsu'], color='blue')
            ax[0].barh(data_hist[data_hist['wsu']>=0]['time2'], data_hist[data_hist['wsu']>=0]['wsu'], color='red')
            ax[1].barh(data_year[data_year['wsu']<0]['time2'], data_year[data_year['wsu']<0]['wsu'], color = 'blue')
            ax[1].barh(data_year[data_year['wsu']>=0]['time2'], data_year[data_year['wsu']>=0]['wsu'], color='red')
            ax[2].barh(data_year[data_year['anom_wsu']<0]['time2'], data_year[data_year['anom_wsu']<0]['anom_wsu'], color = 'blue')
            ax[2].barh(data_year[data_year['anom_wsu']>=0]['time2'], data_year[data_year['anom_wsu']>=0]['anom_wsu'], color='red')

            for axi in ax:
                axi.set_xbound(-0.16, 0.16)
                axi.set_ybound('01/01', '12/31')
                axi.set_yticks(['01-01', '02-01', '03-01', '04-01', '05-01', '06-01', '07-01', '08-01', '09-01', '10-01', '11-01', '12-01', '12-31'], ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC', 'ENE'])
                axi.set_xlabel('Wind Stress (N/m2)')
                axi.set_xticks(np.arange(-0.16, 0.16 + 0.01, 0.02), [-0.16, '', -0.12, '', -0.08, '', -0.04, '', 0, '', 0.04, '', 0.08, '', 0.12, '', 0.16], fontsize= 8)
                axi.grid()

            ax[0].set_ylabel('Fecha')

            ax[0].set_title('Historico')
            ax[1].set_title(year)
            ax[2].set_title('Anomalías')



            plt.suptitle(f'Wind Stress {year} - Buoy: {sdf.setBuoyName(buoy=buoy)}')
            plt.savefig(f'plots/ws/plot_ws_{buoy}_{year}.png')
            plt.close()
        except:
            print(f'Error boya {buoy} año {year}')
