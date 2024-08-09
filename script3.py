import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  # Corrección en la importación

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
                file_path = f'data/monthly/{lat}{lon}_{year}.csv'
                d = pd.read_csv(file_path)
                m = d[d['month'] == month]
                if m.empty or (m['count'].iloc[0] == 0):
                    ocean_grid[lon].append(np.nan)
                else:
                    #DEFINIR SI ES SUMA MENSUAL O PROMEDIO MENSUAL
                    ocean_grid[lon].append(m['sum'].iloc[0])
            except FileNotFoundError:
                ocean_grid[lon].append(np.nan)
                print(f"File not found: {file_path}")
            except Exception as e:
                ocean_grid[lon].append(np.nan)
                print(f"Error processing file {file_path}: {e}")

    # Convertir ocean_grid a DataFrame
    ocean_grid_df = pd.DataFrame(ocean_grid, index=lats)
    
    fig, ax = plt.subplots()

    cols = [-204, -195, -180, -170]
    rows = [-5, -2, 0, 2, 5]
    ax.set_yticks(rows,  ['5°S', '2°S', '0°N', '2°N', '5°N'])
    ax.set_xticks(cols, ['-156°E', '-165°E', '180°W', '170°W'])

    ocean_grid_df.columns = cols
    ocean_grid_df.index= rows
    print(ocean_grid_df)
    
    
    for id, row in ocean_grid_df.iterrows():
        for r in list(row.index):
            ax.scatter(r, id, color='yellow', edgecolor='black')
            ax.arrow(r, id, row[r]*5, 0, width=0.2, color= arrow_color(row[r]))


    ax.set_title(f'{months_names[month-1]} - {year}')
    ax.grid()
    ax.set_ybound(-7, 7)
    ax.set_xbound(-210, -165)

    #print(ocean_grid_df)

    #plt.show()
    #break

    plt.savefig(f'plots/arrows/arrows_{lat}{lon}_{year}_{months_names[month-1]}.png')

    