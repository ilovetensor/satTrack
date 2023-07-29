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

class Satellite(models.Model):
    norad_id = models.IntegerField('NORAD ID', primary_key=True)
    name = models.CharField('Satellite Name', max_length=20)
    description = models.TextField('About Satellite', default='')
    tle = models.TextField("Satellite Tle" ,default='', editable=False)
    launch_date = models.DateField('Launch Date', default=datetime.now())
    launch_site = models.CharField('Launch Site', max_length=50, default='not provided')
    last_tle_update = models.DateField('Launch Date', default=datetime.now(),editable=False)
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.tle, self.last_tle_update = get_tle_from_n2yo(self.norad_id)
        super().save(*args, **kwargs)
    

    




# M8PZCZ-5ELM7M-DE5LRK-531A