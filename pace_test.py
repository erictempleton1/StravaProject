from strava_auth import Auth
import datetime

auth = Auth().connect()

distance = [items['distance'] * 0.000621371 for items in auth]
moving_time = [time['moving_time'] for time in auth]
date = [date['start_date'][:10] for date in auth]

def last_date():
    """ handles error when there is no runs for a week yet """

    try:
        last_run = int(datetime.datetime.strptime(date[-1], '%Y-%m-%d').strftime('%d'))

    except IndexError:
        last_run = 0

    return last_run


def days_remaining():
    """ added if's to deal with 0's produced by dividing by 0 on sundays """

    # returns day of the month from 1-31
    day_num = int(datetime.datetime.now().strftime('%d'))

    # return day of the week from 1-7
    day_today = int(datetime.datetime.today().isoweekday())

    # last_date() returns day of the month for last month
    # accounts for if you have ran on a given day
    if day_num == last_date():
        return 7 - day_today

    # accounts for extra day if no run for the day yet
    else:
        return 8 - day_today

def week_goal():
    return 55

def week_total_miles():   
    return sum(distance) 

def miles_remaining():
        """ change n (goal) as needed """
        miles_remaining = week_goal() - week_total_miles()
        return int(miles_remaining)


# need to manually enter vars to test this func
def avg_to_goal():
    """ same as above, added if's to deal with 0's produced on sundays """
    if days_remaining() == 0:
        return 0
    else:
        return miles_remaining() / days_remaining()

print week_total_miles(), miles_remaining(), avg_to_goal()

