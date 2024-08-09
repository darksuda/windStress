import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 


year = '2024'

months = [1,2,3,4,5,6,7,8,9,10, 11,12]
months_names = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO','JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
lats = ['5n', '2n', '0n', '2s', '5s']

def arrow_color(n):
    if n < 0:
        return '#06449c'
    else:
        return '#9c061a'

for month in months:
    ocean_grid = {
        '156e': [],
        '165e': [],
        '180w': [],
        '170w': [],
    }
    for lon in ocean_grid:
        for lat in lats:
            try:
                file_path = f'data/hist/data_hist_noaabuoys_winds_1990_{lat}{lon}.csv'
                d = pd.read_csv(file_path)
                d = d.groupby('month').mean(numeric_only=True)
                ocean_grid[lon].append(d)


            except FileNotFoundError:
                ocean_grid[lon].append(np.nan)
                print(f"File not found: {file_path}")
            except Exception as e:
                ocean_grid[lon].append(np.nan)
                print(f"Error processing file {file_path}: {e}")
            
            break