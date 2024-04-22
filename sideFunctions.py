

def setBuoyName(buoy:str):
    buoy = buoy.replace('n', '°N ')
    buoy = buoy.replace('s', '°S ')
    buoy = buoy.replace('e', '°E')
    buoy = buoy.replace('w', '°W')
    return buoy

