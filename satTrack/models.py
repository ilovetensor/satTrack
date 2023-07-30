from django.db import models
from datetime import datetime
import requests

api_key = 'M8PZCZ-5ELM7M-DE5LRK-531A'
API_URL = 'https://api.n2yo.com/rest/v1/satellite/'
params = {'apiKey': api_key}

def get_tle_from_n2yo(id):
    r = requests.get(
        f'{API_URL}tle/{id}',
        params=params
    ).json()
    last_tle_update = datetime.now().date()
    return (r['tle'], last_tle_update)

STATUS_CHOICES = (( 'active','ACTIVE'),
                  ('not_tracked','NOT TRACKED'))

class Sensor(models.Model):
    name = models.CharField('Sensor Name', max_length=20)
    resolution_type = models.CharField('Resolution Type', max_length=30, default='')
    resolution_value = models.FloatField('Resolution [m]', default=0)
    swath = models.FloatField('Swath [km]', default=0)
    tilting_type = models.CharField('Tilting Type', max_length=20, default='')
    positive_tilting = models.FloatField('Positive Tilting', default=0)
    negative_tilting = models.FloatField('Negative Tilting', default=0)


    
    def __str__(self):
        return f"{self.resolution_type} sensor,\n res.:{self.resolution_value}m, swath: {self.swath}km"

TILT_CHOICES = (('ROLL', 'ROLL'),
                ('YAW','YAW'),
                ('PITCH', 'PITCH'))

class Satellite(models.Model):
    norad_id = models.IntegerField('NORAD ID', primary_key=True)
    name = models.CharField('Satellite Name', max_length=20)
    manufacturer = models.CharField('Manufacturer', max_length=15, default='')
    satellite_type = models.CharField('Satellite type', max_length=30, default='')

    description = models.TextField('About Satellite', default='')
    tle = models.TextField("Satellite Tle" ,default='', editable=False)
    launch_date = models.DateField('Launch Date', default=datetime.now())
    launch_site = models.CharField('Launch Site', max_length=50, default='not provided')
    last_tle_update = models.DateField('Launch Date', default=datetime.now(),editable=False)
    swath = models.FloatField('Swath [km]', default=0)
    status = models.CharField('Status',max_length=20, choices = STATUS_CHOICES, default='IN ORBIT')
    # resolution_type = models.CharField('Resolution Type',max_length=30, default="")
    # resolution_value = models.FloatField('Resolution Value [m]', default=0)
    orbit = models.CharField('Orbit Type', max_length=20, default='')
    orbital_period = models.FloatField('Orbital Period [m]', default=0)
    inclination = models.FloatField('Inclination [°]', default=0)
    perigee = models.FloatField('Perigee', default=0)
    apogee = models.FloatField('Apogee', default=0)
    sensors = models.ManyToManyField(Sensor)

   


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.tle, self.last_tle_update = get_tle_from_n2yo(self.norad_id)
        super().save(*args, **kwargs)
    


    




"""
S.No    Satellite Name	Manufacturer	Launch date	Satellite Type	Orbit Type	Orbital Period	Inclination	Perigee Altitude	Apogee Altitude	Satellite Norad Id	Status	Payload	Swath	Resolution Type	Resolution	Tilting Type	Positive Tiliting	Negative Tilting	Application
1	EOS 4	ISRO	14-Feb-22	EARTH OBSERVATION	Sun Synchronous	95.2 Minutes	97.6	526.7 Km	543.4 Km	                                        51656	Active	SAR	     223	CRS	                  50	Roll	              36	           -36	                                                                    Agriculture, Forestry & Plantations, Soil Moisture & Hydrology and Flood Mapping
2	EOS 4	ISRO	14-Feb-22	EARTH OBSERVATION	Sun Synchronous	95.2 Minutes	97.6	526.7 Km	543.4 Km	51656	Active	SAR	160	MRS	33	Roll	36	-36	Agriculture, Forestry & Plantations, Soil Moisture & Hydrology and Flood Mapping
3	EOS 4	ISRO	14-Feb-22	EARTH OBSERVATION	Sun Synchronous	95.2 Minutes	97.6	526.7 Km	543.4 Km	51656	Active	SAR	25	FRS 1	3	Roll	36	-36	Agriculture, Forestry & Plantations, Soil Moisture & Hydrology and Flood Mapping
4	EOS 4	ISRO	14-Feb-22	EARTH OBSERVATION	Sun Synchronous	95.2 Minutes	97.6	526.7 Km	543.4 Km	51656	Active	SAR	20	FRS 2	3	Roll	36	-36	Agriculture, Forestry & Plantations, Soil Moisture & Hydrology and Flood Mapping
5	EOS 4	ISRO	14-Feb-22	EARTH OBSERVATION	Sun Synchronous	95.2 Minutes	97.6	526.7 Km	543.4 Km	51656	Active	SAR	15	HRS	1	Roll	36	-36	Agriculture, Forestry & Plantations, Soil Moisture & Hydrology and Flood Mapping
"""