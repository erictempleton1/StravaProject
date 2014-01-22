import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth] # [:10] drops extra time info
distance = [items['distance'] * 0.000621371 for items in auth]

# converts given date to it day name in the week ie: monday, tuesday, friday ect
for dates, miles in zip(date, distance):
    print datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A'), '%.02f' % miles