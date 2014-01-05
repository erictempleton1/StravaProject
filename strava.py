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

# data in lists from strava api
athlete_id = [ath_id['athlete']['id'] for ath_id in results]           
moving_time = [time['moving_time'] / 60 for time in results]    
distance = [items['distance'] * 0.000621371 for items in results]    
date = [date['start_date'] for date in results]    
map_polyline = [maps['map']['summary_polyline'] for maps in results]    
calories = [cals['calories'] for cals in results]   
activity_id = [act_id['id'] for act_id in results]
avg_speed = [spd['average_speed'] for spd in results] 
   

def week_total_miles():   
    return sum(distance)   
        
def avg_miles():   
    return sum(distance) / len(distance)   
        
def miles_remaining(n):  
    """ change n (goal) as needed """   
    return n - week_total_miles()   
        
def week_total_time():   
    return sum(moving_time)
 
def days_remaining():
    """ added if's to deal with 0's produced by dividing by 0 on sundays """
    day_today = datetime.datetime.today().weekday() + 1
    if day_today == 7:
        return 0
    else:
        return 7 - day_today
 
def avg_to_goal():
    """ same as above, added if's to deal with 0's produced on sundays """
    if days_remaining() == 0:
        return 0
    else:
        return miles_remaining(50) / days_remaining()

def avg_pace():
    return sum(moving_time) / sum(distance)
     
def display_results():  
          
    date = datetime.datetime.now()  
      
    print 'Weekly Totals as of %s:' % date.isoformat()
    print '%.1f miles' % week_total_miles()
    print '%.1f miles remaining to goal' % miles_remaining(50)
    print '%.1f mins total' % week_total_time()   
    print '%.0f runs' % len(moving_time)
    print '%.1f avg miles per day' % avg_miles() 
    print '%.0f days remaining this week after today' % days_remaining()
    print '%.1f miles per day to reach weekly goal' % avg_to_goal()
    print '%.2f mins/mile avg pace' % avg_pace()
 
 
display_results()
