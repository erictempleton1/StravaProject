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
        self.moving_time = [time['moving_time'] for time in self.auth] # secs to mins   
        self.distance = [items['distance'] * 0.000621371 for items in self.auth] # meters to miles   
        self.date = [date['start_date'][:10] for date in self.auth]    
        self.map_polyline = [maps['map']['summary_polyline'] for maps in self.auth]    
        self.calories = [cals['calories'] for cals in self.auth]   
        self.activity_id = [act_id['id'] for act_id in self.auth]
        self.avg_speed = [spd['average_speed'] for spd in self.auth]

    def week_goal(self):
        return 55

    def time_list(self):
        time_secs = sum(self.moving_time)
        time_display = str(datetime.timedelta(seconds=time_secs))
        return time_display

    def week_total_miles(self):   
        return sum(self.distance)   
        
    def avg_miles(self):
        if len(self.distance) > 0:   
            return sum(self.distance) / len(self.distance)
        else:
            return 0 
        
    def miles_remaining(self):
        """ change n (goal) as needed """
        miles_remaining = self.week_goal() - self.week_total_miles()
        return int(miles_remaining)
        
    def week_total_time(self):   
        return sum(self.moving_time)

    def last_date(self):
        """ handles error when there is no runs for a week yet """

        try:
            last_run = int(datetime.datetime.strptime(self.date[-1], '%Y-%m-%d').strftime('%d'))

        except IndexError:
            last_run = 0

        return last_run
            
    def days_remaining(self):
        """ added if's to deal with 0's produced by dividing by 0 on sundays """

        # returns day of the month from 1-31
        day_num = int(datetime.datetime.now().strftime('%d'))

        # return day of the week from 1-7
        day_today = int(datetime.datetime.today().isoweekday())

        # last_date() returns day of the month for last month
        # accounts for if you have ran on a given day
        if day_num == self.last_date():
            return 7 - day_today

        # accounts for extra day if no run for the day yet
        else:
            return 8 - day_today
 
    def avg_to_goal(self):
        """ same as above, added if's to deal with 0's produced on sundays """
        if self.days_remaining() == 0:
            return 0
        else:
            return float(self.miles_remaining()) / float(self.days_remaining())

    def avg_pace(self):
        """ uses timedelta to convert secs to minutes. 
            converted to string to slice of extra details for display """
        try:
            avg_pace = sum(self.moving_time) / sum(self.distance)

        except ZeroDivisionError:
            avg_pace = 0

        convert_sec = str(datetime.timedelta(seconds=avg_pace))
        if self.distance == 0 or self.moving_time == 0:
            return 0
        if len(self.distance) > 0:
            return convert_sec[2:7]
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
                layout_list.append(days + ': %.01f miles' % self.distance[count])
            else:
                layout_list.append(days + ':')
        return layout_list


        






