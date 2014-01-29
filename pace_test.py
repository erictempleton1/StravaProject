from strava_auth import Auth
import datetime

auth = Auth().connect()

distance = [items['distance'] * 0.000621371 for items in auth]
moving_time = [time['moving_time'] for time in auth]
date = [date['start_date'][:10] for date in auth] 

avg_pace = sum(moving_time) / sum(distance)
convert_sec = str(datetime.timedelta(seconds=avg_pace))

print convert_sec[2:7]
