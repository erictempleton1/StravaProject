import convert_date
import datetime
import json
from strava_auth import Auth
          
# for readability in text file      
# data = json.dumps(results, indent=4, sort_keys=True)  

# uncomment to write json response to file if needed     
#with open('strava.txt', 'w')as f:  
   #f.write(data)  


class Calcs(object):

    def __init__(self):
        self.auth = Auth().connect()
        self.athlete_id = [ath_id['athlete']['id'] for ath_id in self.auth]           
        self.moving_time = [time['moving_time'] / 60 for time in self.auth] # secs to mins   
        self.distance = [items['distance'] * 0.000621371 for items in self.auth] # meters to miles   
        self.date = [date['start_date'][:10] for date in self.auth]    
        self.map_polyline = [maps['map']['summary_polyline'] for maps in self.auth]    
        self.calories = [cals['calories'] for cals in self.auth]   
        self.activity_id = [act_id['id'] for act_id in self.auth]
        self.avg_speed = [spd['average_speed'] for spd in self.auth]

    def week_goal(self, n):
        return n

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
        miles_remaining = n - self.week_total_miles()
        return int(miles_remaining)
        
    def week_total_time(self):   
        return sum(self.moving_time)

    def return_last_date(self):
        try:
            last_run = int(datetime.datetime.strptime(self.date[-1], '%Y-%m-%d').strftime('%d'))
        except IndexError:
            pass
            
    def days_remaining(self):
        """ added if's to deal with 0's produced by dividing by 0 on sundays """
        day_num = int(datetime.datetime.now().strftime('%d'))
        day_today = int(datetime.datetime.today().weekday() + 1)
        if day_today == 7:
            return 0
        elif day_today == 1:
            return 7
        else:
            return 7 - day_today
 
    def avg_to_goal(self):
        """ same as above, added if's to deal with 0's produced on sundays """
        if self.days_remaining() == 0:
            return 0
        else:
            return self.miles_remaining(self.week_goal(55)) / self.days_remaining()

    def avg_pace(self):
        if len(self.distance) > 0:
            return sum(self.moving_time) / sum(self.distance)
        else:
            return 0

    def num_runs(self):
        """ changes wording from 'runs' to 'run' if only one run """
        if len(self.distance) == 1:
            return '%.0f run' % len(self.distance)
        else:
            return '%.0f runs' % len(self.distance)

    def week_layout(self):
        """ displays weekdays with corresponding mileage """

        # returns date names to match against day_list
        date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in self.date]
        day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']
        
        
        layout_list = []
        count = -1
        for days in day_list:
            if days in date_names:
                count += 1
                layout_list.append(days + ': %.02f miles' % self.distance[count])
            else:
                layout_list.append(days + ':')
        return layout_list

    def progress_percent(self):
        """ gets percent complete for status bar. accounts for > 100% """
        if (self.week_total_miles() / self.week_goal(55)) * 100 <= 100:
            return (self.week_total_miles()/self.week_goal(55)) * 100
        else:
            return 100
        






