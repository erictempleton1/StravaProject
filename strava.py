import requests     
import json  
import datetime 
import time   
   
   
def date_monday(): 
    """ returns day of the week from 0-6, then subtracted from 
        current date to return monday's date for given week for any given week """
    now = datetime.datetime.now() 
    day_number = datetime.datetime.today().weekday() 
    mon_date = int(now.day) - day_number 
    return '%d/%s/%d' % (now.month, mon_date, now.year) 
   
def epoch_date(n): 
    """ converts any given date in m/d/y format to unix epoch. 
        date_monday is converted in this case """
    unix_epoch = time.mktime(datetime.datetime.strptime(n, '%m/%d/%Y').timetuple()) 
    return '%.0f' % unix_epoch 
   
   
date_param = epoch_date(date_monday()) 
   
payload = {'access_token': 'b295cfca0cfdf8f23d3a94707337f56b77ce7354', 'after': date_param}            
r = requests.get('https://www.strava.com/api/v3/athlete/activities', params=payload)             
results = r.json()     
          
# for readability in text file      
data = json.dumps(results, indent=4, sort_keys=True)  
      
#with open('strava.txt', 'w')as f:  
   #f.write(data)  

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
    #change amount as needed   
    return n - week_total_miles()   
        
def week_total_time():   
    return sum(moving_time)
 
def days_remaining():
    day_today = datetime.datetime.today().weekday() + 1
    return 7 - day_today
 
def avg_to_goal():
    return miles_remaining(50) / days_remaining()
     
def display_results():  
          
    date = datetime.datetime.now()  
      
    print 'Weekly Totals as of %s:' % date.isoformat()
    print '%.1f miles' % week_total_miles()
    print '%.1f mins total' % week_total_time()   
    print '%.0f runs' % len(moving_time)
    print '%.1f average miles per day' % avg_miles() 
    print '%.1f miles remaing' % miles_remaining(50)
    print '%.0f days remaining this week after today' % days_remaining()
    print '%.1f miles per day to reach weekly goal' % avg_to_goal()
 
 
#display_results()
# avg page using minutes per miles?
print moving_time[0] / distance[0]
print 60 / (((avg_speed[0] * 0.000621371) * 60) * 60)
# display_results()

# figure out remainder portion of above. remainder should be multiplied by 60 somehow?!