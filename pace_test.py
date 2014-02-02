import requests
import datetime
import convert_date
import json


date_param = convert_date.epoch_date(convert_date.date_monday())

payload = {'access_token': 'e8a0059d272d880a129fba2ca321204394f99806',
                   'after': date_param}

r = requests.get('https://www.strava.com/api/v3/athlete/activities', 
                          params=payload)

results = r.json()

print results





