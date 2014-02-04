import datetime
from datetime import timedelta
from strava_auth import Auth

auth = Auth().connect()

#date = [date['start_date'][:10] for date in date_test]
#distance = [items['distance'] * 0.000621371 for items in auth]

date_test = ['2014-02-03T03:43:19Z', '2014-02-03T05:43:19Z', '2014-02-04T03:43:20Z']
distance = [8.5463, 5.6654, 6.764]

date = [date[:10] for date in date_test]

def week_layout():
    """ displays weekdays with corresponding mileage """

    # returns date names to match against day_list
    date_names = [datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A') for dates in date]
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']
        
        
    layout_list = []
    count = -1
    for days in day_list:
        if days in date_names:
            count += 1
            layout_list.append(days + ': %.01f miles' % distance[count])
        else:
            layout_list.append(days + ':')
    return layout_list


def count_list():

    day_list = [int(datetime.datetime.strptime(dates[:10], '%Y-%m-%d').strftime('%d')) for dates in date_test]
    for items in day_list:
        return day_list.count(items)

print count_list()





