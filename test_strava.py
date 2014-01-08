import requests
import json
import convert_date

date_param = convert_date.epoch_date(convert_date.date_monday())

payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354', 'resolution': 'low'}
r = requests.get('https://www.strava.com/api/v3/activities/104260032/streams/latlng', params=payload)           
results = r.json()

data = json.dumps(results, indent=4, sort_keys=True) 

lats = [points['data'] for points in results]


with open('strava.txt', 'w') as f:
    f.write(data)