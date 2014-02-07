import datetime
from datetime import timedelta
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth]
distance = [items['distance'] * 0.000621371 for items in auth]
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']
date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in date]

def week_layout():
    """ displays weekdays with corresponding mileage """
    layout_list = []
    layout_count = -1
    for days in day_list:
        if days in date_names:
            layout_count += 1
            layout_list.append(days + ': %.01f miles' % distance[layout_count])
        else:
            layout_list.append(days + ':')
    return layout_list

day_distance = zip(date_names, distance)

# print day_distance[3][0] # returns 'Thursday'

# days[1] returns days names from day_list

layout_list = []
for days in day_distance:
    layout_list.append('%s: %.02f miles' % (days[0], days[1]))

print layout_list



