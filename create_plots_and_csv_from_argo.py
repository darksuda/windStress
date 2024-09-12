import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gsw


file = open('data_pota_2.json')
data = json.load(file)
print('EL ARCHIVO TIENE: ' + str(len(data)) + ' PERFILES')

psal_start  = 34.2#
psal_end = 36.4
temp_start = 10
temp_end = 30
        

pres_start = 0
pres_end = 300

for p in data:
    id = p['_id']
    platform = str(id[0:-4])
    lon = p['geolocation']['coordinates'][0]
    lat = p['geolocation']['coordinates'][1]
    date = p['timestamp'][0:10]
    cycle = str(p['cycle_number'])
    params = p['data_info'][0]
    param_values = p['data']
    index_CTD = []

    index_CTD.append(params.index('salinity_sfile')) if 'salinity_sfile' in params else index_CTD.append(params.index('salinity'))
    index_CTD.append(params.index('temperature_sfile')) if 'temperature_sfile' in params else index_CTD.append(params.index('temperature'))
    index_CTD.append(params.index('pressure'))
    if 'doxy' in params:
        index_CTD.append(params.index('doxy'))


    datadf= pd.DataFrame()
    for i in index_CTD:
        datadf[params[i]] = param_values[i]

    psal = datadf.columns[0]
    temp = datadf.columns[1]
    pres = datadf.columns[2]
    if 'doxy' in params:
        doxy = datadf.columns[3]

    mint=np.min(datadf[temp])
    maxt=np.max(datadf[temp])

    mins=np.min(datadf[psal])
    maxs=np.max(datadf[psal])

    tempL=np.linspace(temp_start ,temp_end ,50)
    salL=np.linspace(psal_start ,psal_end ,50)

    Tg, Sg = np.meshgrid(tempL,salL)
    sigma_theta = gsw.sigma0(Sg, Tg)

    datadf['lat'] = round(lat,2)
    datadf['lon'] = round(lon,2)
    datadf['date'] = date
    datadf.to_csv(f'datos_oc_pq/datos_equator/pota2019/{id}.csv', index=False)
    
#SOLO GENERA EL CSV
""" 
    fig, ax = plt.subplots(1,3, figsize = (15,8))
    ax[0].plot(datadf[temp], datadf[pres])
    ax[0].axhline(y=25, color="#c3093f")
    ax[0].invert_yaxis()
    ax[0].set_xticks(np.linspace(10,30,11))
    ax[0].set_yticks(np.arange(pres_start,pres_end + 1,50))
    ax[0].set_ybound(pres_start, pres_end)
    ax[0].set_xbound(temp_start, temp_end)
    ax[0].set_title('Temperatura vs Presión')
    ax[0].set_xlabel('Temperatura (°C)')
    ax[0].set_ylabel('Presión (dbar)')
    ax[0].grid()

    ax[1].plot(datadf[psal], datadf[pres])
    ax[1].axhline(y=25, color="#c3093f")
    ax[1].axvline(x=35.1, color="#c3093f")
    ax[1].axvline(x=34.8, color="#c3093f")
    ax[1].axvline(x=33.8, color="#c3093f")
    ax[1].invert_yaxis()
    ax[1].set_xticks(np.linspace(33.3, 36.3, 16))
    ax[1].set_yticks(np.arange(pres_start,pres_end + 1,50))
    ax[1].set_ybound(pres_start, pres_end)
    ax[1].set_xbound(psal_start, psal_end)
    ax[1].set_title('Salinidad vs Presión')
    ax[1].set_xlabel('Salinidad (psu)')
    ax[1].set_ylabel('Presión (dbar)')
    ax[1].grid()

    ax[2].plot(datadf[psal], datadf[temp])
    plot_ts = ax[2].contour(Sg, Tg, sigma_theta, colors='grey', zorder=1)
    cl=plt.clabel(plot_ts,fontsize=10,inline=True)
    ax[2].set_xticks(np.linspace(33.3, 36.3, 16))
    ax[2].set_yticks(np.linspace(10,30,11))
    ax[2].set_ybound(temp_start, temp_end)
    ax[2].set_xbound(psal_start, psal_end)
    ax[2].set_title('Diagrama TS')
    ax[2].set_xlabel('Salinidad (psu)')
    ax[2].set_ylabel('Temperatura (°C)')
    ax[2].grid()

    plt.suptitle('Platform: '+ str(platform) +'   Cycle: ' + str(cycle) + ' Date: ' + date + '   Coords: ' + str(np.round(lon, 2)) + ' , ' + str(np.round(lat, 2)) )
    #plt.figtext(0.08, 0.02, "Fuente: Argo (https://argo.ucsd.edu)", fontsize=6.5)
    

    #plt.savefig('IMGS/profile'+id+'_2024_FEB_26')
    #plt.show()
    #plt.close()

    if 'doxy' in params:
        fig2, ax2 = plt.subplots(figsize = (12,7))
        ax2.set_xticks(np.linspace(0, 300, 17), list(map(lambda x: x * 0.032 , np.linspace(0, 300, 17))))
        ax2.scatter(datadf[doxy], datadf[pres], s=9)
        ax2.invert_yaxis()
        ax2.set_title('Platform: '+ str(platform) +'   Cycle: ' + str(cycle) + '\n Date: ' + date + '   Coords: ' + str(np.round(lon, 2)) + ' , ' + str(np.round(lat, 2)) + '\nOxígeno disuelto')
        ax2.set_xlabel('Oxígeno disuelto (mgO2/Kg)')
        ax2.set_ylabel('Presión (dbar)')
        ax2.set_yticks(np.arange(pres_start ,pres_end, 50))
        ax2.set_ybound(pres_start, pres_end)
        ax2.grid()

        #plt.savefig('IMGS/profile_doxy_'+id+'_2024_FEB_26')
        #plt.show()
        #plt.close()

"""