import netCDF4 as cdf 
import numpy as np 
import pandas as pd 


data = cdf.Dataset('DATOS_COP.nc')

temp = np.array(data['thetao'])[0][0]
latitude = np.array(data['latitude'])
longitude = np.array(data['longitude'])


temp = pd.DataFrame(temp)

print(latitude)