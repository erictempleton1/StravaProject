import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth]
distance = [items['distance'] * 0.000621371 for items in auth]

# converts given date to it day name in the week ie: monday, tuesday, friday ect
for items in date:
    print datetime.datetime.strptime(items, '%Y-%m-%d').strftime('%A')