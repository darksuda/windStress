import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  # Corrección en la importación

year = '1997'

months = [1,2,3,4,5,6,7,8,9]
months_names = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO','JULIO', 'AGOSTO', 'SEPTIEMBRE']
lats = ['5n', '2n', '0n', '2s', '5s']
for month in months:
    ocean_grid = {
        '156e': [],
        '165e': [],
        '180w': [],
        '170w': []
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
                    # DEFINIR SI ES SUMA MENSUAL O PROMEDIO MENSUAL
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


    plot = ax.contourf(ocean_grid_df, cmap='coolwarm', levels=np.arange(-2.5, 2.55, 0.05))
    plot2 = ax.contour(plot, levels=np.arange(-2.5, 2.6, 0.1), colors='black', linewidths = 0.7)
    ax.clabel(plot2)
    ax.set_yticks([0,1,2,3,4], ['5°S', '2°S', '0°N', '2°N', '5°N'])
    ax.set_xticks([0,1,2,3], ['156°E', '165°E', '180°W', '170°W'])
    ax.set_ylabel('Latitud')
    ax.set_xlabel('Longitud')
    ax.set_title(months_names[month-1] + f' {year}')
    plt.colorbar(plot)
    plt.show()
    #plt.savefig(f'plots/monthly/ws_{lat}{lon}_{year}_{months_names[month-1]}.png')