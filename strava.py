import requests     
import json  
import convert_date
import datetime

date_param = convert_date.epoch_date(convert_date.date_monday())
   
payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354', 'after': date_param}            
r = requests.get('https://www.strava.com/api/v3/athlete/activities', params=payload)             
results = r.json()     
          
# for readability in text file      
data = json.dumps(results, indent=4, sort_keys=True)  

# uncomment to write json response to file if needed     
#with open('strava.txt', 'w')as f:  
   #f.write(data)  
    

class Calculations(object):

    def __init__(self):
        self.athlete_id = [ath_id['athlete']['id'] for ath_id in results]           
        self.moving_time = [time['moving_time'] / 60 for time in results] # secs to mins   
        self.distance = [items['distance'] * 0.000621371 for items in results] # meters to miles   
        self.date = [date['start_date'] for date in results]    
        self.map_polyline = [maps['map']['summary_polyline'] for maps in results]    
        self.calories = [cals['calories'] for cals in results]   
        self.activity_id = [act_id['id'] for act_id in results]
        self.avg_speed = [spd['average_speed'] for spd in results] 

    def time_list(self):
        return self.moving_time

    def week_total_miles(self):   
        return sum(self.distance)   
        
    def avg_miles(self):
        if len(self.distance) > 0:   
            return sum(self.distance) / len(self.distance)
        else:
            return 0 
        
    def miles_remaining(self, n):  
        """ change n (goal) as needed """   
        return n - self.week_total_miles()   
        
    def week_total_time(self):   
        return sum(self.moving_time)
 
    def days_remaining(self):
        """ added if's to deal with 0's produced by dividing by 0 on sundays """
        day_today = datetime.datetime.today().weekday() + 1
        if day_today == 7:
            return 0
        else:
            return 7 - day_today
 
    def avg_to_goal(self):
        """ same as above, added if's to deal with 0's produced on sundays """
        if self.days_remaining() == 0:
            return 0
        else:
            return self.miles_remaining(50) / self.days_remaining()

    def avg_pace(self):
        if len(self.distance) > 0:
            return sum(self.moving_time) / sum(self.distance)
        else:
            return 0






