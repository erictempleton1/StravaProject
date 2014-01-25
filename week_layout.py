import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth] # [:10] drops extra time info
distance = [items['distance'] * 0.000621371 for items in auth]


# converts given date to it day name in the week ie: monday, tuesday, friday ect
date_distance = zip(date, distance)

date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in date]

date_num = [datetime.datetime.strptime(dates, '%Y-%m-%d').weekday() for dates in date]

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


date1 = int(datetime.datetime.now().strftime('%d')) + 1
date2 = int(datetime.datetime.strptime(date[-1], '%Y-%m-%d').strftime('%d'))

print date1 != date2
    
