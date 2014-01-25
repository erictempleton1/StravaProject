import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth] # [:10] drops extra time info
distance = [items['distance'] * 0.000621371 for items in auth]


# converts given date to it day name in the week ie: monday, tuesday, friday ect
date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in date]

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

layout_list = []
count = -1
for days in day_list:
    if days in date_names:
        count += 1
        layout_list.append(days + ': %.02f miles' % distance[count])
    else:
        layout_list.append(days)

print layout_list
        
    
