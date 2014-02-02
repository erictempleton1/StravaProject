import requests
import datetime
import convert_date
import json


date_param = convert_date.epoch_date(convert_date.date_monday())

payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354',
                   'after': date_param}

r = requests.get('https://www.strava.com/api/v3/athlete/activities', 
                          params=payload)

results = r.json()

print results





