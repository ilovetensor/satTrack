from sgp4.api import Satrec 
from sgp4.api import jday 
import pandas as pd 
import numpy as np
from skyfield.api import EarthSatellite, Loader
from skyfield.api import load, wgs84
import matplotlib.pyplot as plt 
import math


def cal_semi_major_axis(n):
    mu = float('3.986004418e+14')
    num = (mu)**(1/3)
    deno = ((2*n*np.pi)/(86400))**(2/3)
    return round((num/deno)/1000, 3)
    
def line1_data(line1, save_dict):
    save_dict['launch_year'] = line1[9: 11]
    save_dict['first_derivative_mean_motion'] = line1[33: 43]
    save_dict['second_derivative_mean_motion'] = line1[44: 52]
    save_dict['bstar'] = line1[53: 61]
 
def line2_data(line2, save_dict):
    save_dict['inclination'] = line2[8: 16]
    save_dict['RAAN'] = line2[17: 25]
    print(save_dict['RAAN'])
    save_dict['longitude_of_ascending_node'] = round((float(save_dict['RAAN']) * np.pi)/180, 2)
    save_dict['eccentricity'] = '0.'+line2[26: 33]
    save_dict['argument of perigee'] = line2[34: 41]
    save_dict['argument_of_periapsis'] = round((float(save_dict['argument of perigee']) * np.pi)/180, 2)
    save_dict['mean_anomaly']= line2[43: 50]
    save_dict['mean_motion']= line2[52: 63]
    save_dict['semi_major_axis']= cal_semi_major_axis(float(save_dict['mean_motion']))
    save_dict['period'] = round(1440/(float(save_dict['mean_motion'])), 1)

def convert(TLE_FILE = "tle.txt"):
    save_dict = {}
    TLEs = open(TLE_FILE, 'r')
    L_Name = []
    L_1 = []
    L_2 = []
    i = 1
    for line in TLEs:
        j = i
        if i == 1:
            line= line.replace('\n','')
            L_Name.append(line)
            name = line.strip()
            save_dict[name] = {}
            j = 2
        elif i == 2:
            L_1.append(line[:69])
            line1_data(line, save_dict[name])
            j = 3
        elif i == 3:
            L_2.append(line[:69])
            line2_data(line, save_dict[name])
            j = 1
        i = j
    dataframe = pd.DataFrame(columns = ['Satellite_name', 'Line_1', 'Line_2', 'Position_vector', 'Speed_vector']) 
    dataframe.Satellite_name = L_Name
    dataframe.Line_1 = L_1
    dataframe.Line_2 = L_2
    jd, fr = jday(2021, 2, 4, 18, 5, 0)
    L_PosVector = []
    L_SpeedVector = []
    for i in range(len(dataframe)):
    
        s = dataframe.Line_1[i]
        t = dataframe.Line_2[i]
        satellite = Satrec.twoline2rv(s, t)
        e, r, v = satellite.sgp4(jd, fr)
        L_PosVector.append(r)
        L_SpeedVector.append(v)

    dataframe.Position_vector = L_PosVector
    dataframe.Speed_vector = L_SpeedVector

    return dataframe, save_dict

# loading satellite parameters using skyfield


def get_live_data(TLE):
    load = Loader('~/Documents/fishing/SkyData')
    data = load('de421.bsp')
    ts = load.timescale() 

    planets = load('de421.bsp')
    earth = planets['earth']

    ts = load.timescale()
    minutes = np.arange(0, 240, 2)
    

    L1, L2 = TLE.splitlines()
    CARTO_Geo = EarthSatellite(L1, L2)
    print(CARTO_Geo.epoch.utc_jpl())
    time = ts.now()
    geocentric = CARTO_Geo.at(time)
    lat, lon = wgs84.latlon_of(geocentric)
    h = wgs84.height_of(geocentric)
    time_str = f"{time.utc.hour}: {time.utc.minute}: {int(time.utc.second)}"
    position = {'lat': round(lat.degrees, 2), 'lon': round(lon.degrees, 2), 'height': round(h.km, 2), 'time': time_str}
    
    return position
