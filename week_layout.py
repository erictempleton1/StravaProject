import datetime
from strava_auth import Auth

auth = Auth().connect()

date = [date['start_date'][:10] for date in auth] # [:10] drops extra time info
distance = [items['distance'] * 0.000621371 for items in auth]

date_distance = zip(date, distance)

# converts given date to it day name in the week ie: monday, tuesday, friday ect
for dates, miles in date_distance:
    print datetime.datetime.strptime(dates, '%Y-%m-%d').strftime('%A'), '%.02f' % miles

day_number = datetime.datetime.today().weekday()
print day_number

# figure out how to use this with range to slice in dates for the rest of the week