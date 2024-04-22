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
        '5n165e'
        ]
for buoy in buoys:
        
    year_hist = '1990'

    #for year in ['1991', '1992', '1997', '2015', '2016', '2017', '2023']:
    for year in ['1991']:
        try:
                
            rqw.init_wind_data_download(buoy)

            hist_dir = rqw.request_wind_historical_data(year_hist, buoy)
            year_dir = rqw.request_wind_data(year, buoy)

            data_hist = pd.read_csv(hist_dir)
            data_year = pd.read_csv(year_dir)

            data_year = data_year.drop(data_year[data_year['time2'] == '02/29'].index).reset_index()

            a = np.zeros(365)
            a[:] = np.nan


            data_hist['wsu'] = [cws.calc_wind_stress(u, 1022) for u in data_hist['winds_u']] 

            data_year['wsu'] = [cws.calc_wind_stress(u, 1022) for u in data_year['winds_u']]
            data_year['anom_u'] = data_year['winds_u'] - data_hist['winds_u']
            data_year['anom_wsu'] = data_year['wsu'] - data_hist['wsu']

            print(data_year)

        except:
            print('error xd')