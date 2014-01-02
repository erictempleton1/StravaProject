import requests 
import json 
  
#http://www.strava.com/clubs/1357 
  
#f = open('afc.txt', 'w')    
  
payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354', 'per_page': 100} 
  
r = requests.get('https://www.strava.com/api/v3/clubs/1357/activities', params=payload) 
  
results = r.json()    
      
# for readability in text file     
data = json.dumps(results, indent=4, sort_keys=True)  


map_polyline = [maps['map']['summary_polyline'] for maps in results]

print len(map_polyline)

#f.write(data)     
#f.close