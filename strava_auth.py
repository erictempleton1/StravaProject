import requests
import json
import convert_date
import datetime

class Auth(object):
    
    def __init__(self):
        self.date_param = convert_date.epoch_date(convert_date.date_monday())
   
    def connect(self):
        payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354',
                   'after': self.date_param}
        r = requests.get('https://www.strava.com/api/v3/athlete/activities', 
                          params=payload)           
        self.results = r.json()
        return self.results
      