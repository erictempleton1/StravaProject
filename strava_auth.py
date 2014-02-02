import requests
import json
import convert_date
import datetime

class Auth(object):
    
    def __init__(self):
        self.date_param = convert_date.epoch_date(convert_date.date_monday())
   
    def connect(self):
        payload = {'access_token': 'e8a0059d272d880a129fba2ca321204394f99806',
                   'after': self.date_param}
        r = requests.get('https://www.strava.com/api/v3/athlete/activities', 
                          params=payload)           
        self.results = r.json()
        return self.results
      