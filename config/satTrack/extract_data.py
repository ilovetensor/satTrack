from sgp4.api import Satrec 
from sgp4.api import jday 
import pandas as pd 
import numpy as np
from skyfield.api import EarthSatellite, Loader
from skyfield.api import load, wgs84
import matplotlib.pyplot as plt 
import math
import requests

api_key = 'M8PZCZ-5ELM7M-DE5LRK-531A'
API_URL = 'https://api.n2yo.com/rest/v1/satellite/'
params = {'apiKey': api_key}
def get_tle_from_n2yo(id):
        r = requests.get(
            f'{API_URL}tle/{id}',
            params=params
        ).json()
        return r['tle']


def cal_semi_major_axis(n):
    mu = float('3.986004418e+14')
    num = (mu)**(1/3)
    deno = ((2*n*np.pi)/(86400))**(2/3)
    return round((num/deno)/1000, 3)
    
def line1_data(line1, save_dict):
    save_dict['norad_id'] = line1[2: 7]
    save_dict['launch_year'] = line1[9: 11]
    save_dict['first_derivative_mean_motion'] = line1[33: 43]
    save_dict['second_derivative_mean_motion'] = line1[44: 52]
    save_dict['bstar'] = line1[53: 61]
 
def line2_data(line2, save_dict):
    save_dict['inclination'] = line2[8: 16]
    save_dict['RAAN'] = line2[17: 25]
    save_dict['longitude_of_ascending_node'] = round((float(save_dict['RAAN']) * np.pi)/180, 2)
    save_dict['eccentricity'] = '0.'+line2[26: 33]
    save_dict['argument of perigee'] = line2[34: 41]
    save_dict['argument_of_periapsis'] = round((float(save_dict['argument of perigee']) * np.pi)/180, 2)
    save_dict['mean_anomaly']= line2[43: 50]
    save_dict['mean_motion']= line2[52: 63]
    save_dict['semi_major_axis']= cal_semi_major_axis(float(save_dict['mean_motion']))
    save_dict['period'] = round(1440/(float(save_dict['mean_motion'])), 1)

def convert(TLE):
    save_dict = {}
    L1, L2 = TLE.splitlines()
    line1_data(L1, save_dict)
    line2_data(L2, save_dict)
    save_dict['L1'] = L1
    save_dict['L2'] = L2
    
    return save_dict


def load_satellite(TLE):
    load = Loader('~/Documents/fishing/SkyData')
    ts = load.timescale() 
    L1, L2 = TLE.splitlines()
    SATELLITE = EarthSatellite(L1, L2)
    return SATELLITE, ts

def get_azimuth_altitude_distance_ra_dec(SATELLITE, time, cur_loc):
    bluffton = wgs84.latlon(float(cur_loc['lat']), float(cur_loc['lon']))
    difference = SATELLITE - bluffton
    topocentric = difference.at(time)
    alt, az, distance = topocentric.altaz()
    ra, dec, distance = topocentric.radec()
    return (alt, az, distance, ra, dec)

def get_live_data(TLE, cur_loc):
    SATELLITE, ts = load_satellite(TLE)
    time = ts.now()
    alt, az, distance, ra, dec = get_azimuth_altitude_distance_ra_dec(SATELLITE, time, cur_loc)

    geocentric = SATELLITE.at(time)
    v = geocentric.velocity.km_per_s
    speed = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    lat, lon = wgs84.latlon_of(geocentric)
    h = wgs84.height_of(geocentric)
    time_str = f"{time.utc.hour}: {time.utc.minute}: {int(time.utc.second)}"
    position = {'lat': round(lat.degrees, 2),
                'lon': round(lon.degrees, 2), 
                'height': round(h.km, 2), 
                'speed' :round(speed, 2),
                'time': time_str,
                'elevation': str(alt),
                'azimuth': str(az),
                'distance': distance.km,
                'ra': str(ra),
                'dec': str(dec), }
    return position

def data_over_time(TLE, minutes_to_project=94):
    SATELLITE, ts = load_satellite(TLE)

    now = ts.now()
    minutes = np.arange(now.utc.minute, now.utc.minute + (minutes_to_project), 2)
    time_scale = ts.utc(now.utc.year, now.utc.month, now.utc.day, now.utc.hour, minutes, now.utc.second)

    geocentric = SATELLITE.at(time_scale)
    lat, lon = wgs84.latlon_of(geocentric)
    h = wgs84.height_of(geocentric)

    buffer = {}
    i = 0
    for j,k,l,m in zip(lat.degrees, lon.degrees, h.km, time_scale):
        buffer[i] = {'latitude':j, 'longitude': k, 'height': l, 'iso_string': m.utc_iso()}
        i+=1
        
    return buffer