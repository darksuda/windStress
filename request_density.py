import gsw 
import netCDF4 as cdf
import numpy as np
import matplotlib.pyplot as plt

data_temp = cdf.Dataset('cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_1710878813881.nc')
temp = np.array(data_temp['thetao'])[0][0]
lat = np.array(data_temp['latitude'])
lon = np.array(data_temp['longitude'])

data_psal = cdf.Dataset('cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m_1710881879681.nc')
psal = np.array(data_psal['so'])[0][0]

d = gsw.rho_t_exact(35, 25, 0)
d2 = gsw.sigma0(35, 25)

st = gsw.sigma0(psal, temp)
d2 = gsw.rho_t_exact(psal, temp, 0)

print(np.nanmean(st, axis=0))
print(np.nanmean(d2, axis=0))

fig, ax = plt.subplots()
ax.plot(lon, np.nanmean(st, axis=0))
plt.show()


"""
fig, ax = plt.subplots(2)

plot_st = ax[0].contourf(lon, lat, st, levels = np.arange(20, 23.001, 0.2), cmap='rainbow')
plot_d2 = ax[1].contourf(lon, lat, d2, levels = np.arange(1020, 1023.001, 0.2), cmap='rainbow')
plotc_st = ax[0].contour(plot_st, colors = 'black', linewidths = 0.7)
plotc_d2 = ax[1].contour(plot_d2, colors = 'black', linewidths = 0.7)

ax[0].clabel(plotc_st)
ax[1].clabel(plotc_d2)

ax[0].set_title('SIGMA-T')
ax[1].set_title('DENSIDAD')

plt.colorbar(plot_st)

plt.show()
plt.colorbar(plot_d2)"""


