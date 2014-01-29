from strava_auth import Auth
import datetime

auth = Auth().connect()

distance = [items['distance'] * 0.000621371 for items in auth]
moving_time = [time['moving_time'] for time in auth]
date = [date['start_date'][:10] for date in auth] 

time_secs = sum(moving_time)

time_display = str(datetime.timedelta(seconds=time_secs))

print time_display
