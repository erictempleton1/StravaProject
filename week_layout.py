import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth] # [:10] drops extra time info
distance = [items['distance'] * 0.000621371 for items in auth]

date_distance = zip(date, distance)

# converts given date to it day name in the week ie: monday, tuesday, friday ect
for dates, miles in date_distance:
    print datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A'), '%.02f' % miles

for dates in date:
    print datetime.datetime.strptime(dates, '%Y-%m-%d').weekday()

day_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday',
            3:'Thursday', 4:'Friday', 5:'Saturday',
            6:'Sunday'}


"""
 # try to use something like this to compare dict and list

for key in mylist:
    if key in mydict1:
        print 'Key %s in dict 1' % key
    elif key in mydict2:
        print 'Key %s in dict 2' % key
    else:
        print 'Key %s not in dictionaries' % key
"""