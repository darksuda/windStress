import numpy  as np
import matplotlib.pyplot as plt
import netCDF4 as cdf
import math
import gsw


def calc_wind_stress(u, d):
    try:
        u = float(u)
        usign = np.sign(u)
        u = abs(u)
        if u < 6:
            cD = (0.61 + (0.063 * u))/1000
        elif u < 22:
            cD = 0.0011
        u2 = u*u
        return cD* d * u2 * usign
    except:
        return np.nan


"""
x = np.arange(0, 22.1, 0.1)
y0 = [calc_wind_stress(u, 1020) for u in x]
y1 = [calc_wind_stress(u, 1021) for u in x]
y2 = [calc_wind_stress(u, 1022) for u in x]
y3 = [calc_wind_stress(u, 1023) for u in x]
y4 = [calc_wind_stress(u, 1024) for u in x]
y5 = [calc_wind_stress(u, 1025) for u in x]



fig, ax = plt.subplots()

ax.plot(x, y1, label='1021 kg/m3', color='blue')
ax.plot(x, y2, label='1022 kg/m3', color='red')
ax.plot(x, y3, label='1023 kg/m3', color='yellow')
ax.plot(x, y4, label='1024 kg/m3', color='black')
ax.plot(x, y5, label='1025 kg/m3', color='green')
ax.plot(x, y0, label='1020 kg/m3', color='purple')

ax.set_xlabel('Velocidad de viento (m/s)')
ax.set_ylabel('Wind Stress (N/m2)')

ax.set_title('Wind Stress a diferentes densidades')

ax.legend()

plt.show()
"""
