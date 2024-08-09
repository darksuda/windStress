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
            cD = 0.0011
        elif u < 22:
            cD = (0.61 + (0.063 * u))/1000
        u2 = u*u
        return cD* d * u2 * usign
    except:
        return np.nan

