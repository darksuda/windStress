import netCDF4 as cdf 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import os
import datetime as dt

import calc_wind_stress as cws


def init_wind_data_download(buoy):
    try:
        url = f"https://www.pmel.noaa.gov/tao/taoweb/disdel_data/cdf/sites/daily/w{buoy}_dy.cdf"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"data/total/w{buoy}_dy.cdf", "wb") as f:
                f.write(response.content)
                f.close()
    except:
        print('No se ha encontrado data disponible')



def  request_wind_data(year, buoy):
    file_cdf = f'data/total/w{buoy}_dy.cdf'
    file_dir = f'data/year/data_year_noaabuoys_winds_{year}_{buoy}.csv'

    if year == str(dt.date.today().year):
        try:
            os.remove(file_dir)
            print('Actualizando datos de vientos')
        except:
            print('Creando datos de vientos')

    if not os.path.isfile(file_dir):
        print(f'No se ha encontrado data disponible en su computadora para el año {year} en la boya {buoy}')
        try:
            init_wind_data_download(buoy)      
            data = cdf.Dataset(file_cdf)
            date_init = dt.datetime(
                int(data['time'].units[11:15]),
                int(data['time'].units[16:18]),
                int(data['time'].units[19:21])
            )
            time = np.array(data['time'])
            time = [str(date_init + dt.timedelta(days=int(i))) for i in time]
            winds_u = np.array(data['WU_422']).T[0][0][0]
            winds_u[winds_u == 1e+35] = np.nan
            winds_v = np.array(data['WV_423']).T[0][0][0]
            winds_v[winds_v == 1e+35] = np.NaN
            data_df = pd.DataFrame({
                'time' : [i[:10] for i in time],
                'time2' : [i[5:10] for i in time],
                'year' : [int(i[:4]) for i in time],
                'month' : [int(i[5:7]) for i in time],
                'day' : [int(i[8:10]) for i in time],
                'winds_u' : winds_u,
                'winds_v' : winds_v
            })
            data_year = data_df[data_df['year'] == int(year)].reset_index(drop=True)
            data_year = data_year.drop(data_year[data_year['time2'] == '02-29'].index).reset_index(drop=True)
            data_year.to_csv(file_dir, index=False)
            print(f'data {year} created')
            data.close()
            os.remove(file_cdf)

        except:
            print(f'La NOAA no tiene datos disponibles para el año {year} en la boya {buoy}')
            data_year = pd.DataFrame({
                'time' : [],
                'time2' : [],
                'year' : [],
                'month' : [],
                'day' : [],
                'winds_u' : [],
                'winds_v' :[] 
            })
            data_year.to_csv(file_dir, index=False)
    return file_dir

def request_wind_historical_data(year, buoy):
    file_cdf = f'data/total/w{buoy}_dy.cdf'
    file_dir = f'data/hist/data_hist_noaabuoys_winds_{year}_{buoy}.csv'

    if not os.path.isfile(file_dir):
        print(f'No se ha encontrado data histórica disponible en su computadora para el año {year} en la boya {buoy}')
        try:
            init_wind_data_download(buoy)      
            data = cdf.Dataset(file_cdf)
            date_init = dt.datetime(
                int(data['time'].units[11:15]),
                int(data['time'].units[16:18]),
                int(data['time'].units[19:21])
            )
            time = np.array(data['time'])
            time = [str(date_init + dt.timedelta(days=int(i))) for i in time]
            winds_u = np.array(data['WU_422']).T[0][0][0]
            winds_u[winds_u == 1e+35] = np.nan
            winds_v = np.array(data['WV_423']).T[0][0][0]
            winds_v[winds_v == 1e+35] = np.NaN
            data_df = pd.DataFrame({
                'time' : [i[:10] for i in time],
                'time2' : [i[5:10] for i in time],
                'year' : [int(i[:4]) for i in time],
                'month' : [int(i[5:7]) for i in time],
                'day' : [int(i[8:10]) for i in time],
                'winds_u' : winds_u,
                'winds_v' : winds_v
            })
            data_hist = data_df[(data_df['year'] >= int(year)) & (data_df['year'] < int(year)+30)].reset_index(drop=True)
            data_hist = data_hist.groupby('time2').mean(numeric_only=True).reset_index()
            data_hist = data_hist.drop(data_hist[data_hist['time2'] == '02-29'].index).reset_index(drop=True)
            data_hist.to_csv(file_dir, index=False)
            print(f'data {year} created')
            data.close()
            os.remove(file_cdf)
        except:
            print(f'La NOAA no tiene datos disponibles para el año {year} en la boya {buoy}')
            
    return file_dir

