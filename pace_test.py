import datetime
from datetime import timedelta
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth]
distance = [items['distance'] * 0.000621371 for items in auth]
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in date]


def week_layout():
    """ displays weekdays with corresponding mileage """
  
    layout_list = []
    layout_count = -1
    name_count = 1
    for days in day_list:

        if days in date_names and date_names.count(days) > 1:
            name_count += date_names.count(days) # end range for sum below. should work for 2+ activities in one day
            sum_extra = sum(distance[date_names.index(days):name_count]) # only sums matching days
            layout_list.append(days + ': %.01f miles' % sum_extra)

        elif days in date_names:
            layout_count += 1
            layout_list.append(days + ': %.01f miles' % distance[layout_count])

        else:
            layout_list.append(days + ':')

    return layout_list

print week_layout()








