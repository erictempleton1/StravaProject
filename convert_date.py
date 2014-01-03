import datetime
from datetime import timedelta
import time

def date_monday():
    """ returns day of the week from 0-6, then subtracted from
        current date to return monday's date for given week for any given week.
        switched to timedelta for when a new month starts midweek and causes problems
        with prior months 31,30,29 ect. also added failsafe for first week
        of a new year, which caused issues with 2013 to 2014 in same week."""

    now = datetime.datetime.now()
    day_number = datetime.datetime.today().weekday()
    current_year = now.year

    # failsafe for mondays with dates in prev months (31,30,29 ect)
    mon_date = now - datetime.timedelta(days=day_number)
    mon_num = mon_date.strftime('%d')
    mon_year = int(mon_date.strftime('%Y'))
    mon_monday = int(mon_date.strftime('%m'))

    if current_year > mon_year:
        return '%d/%s/%s' % (mon_monday, mon_num, mon_year)
    else:
        return '%d/%s/%s' % (now.month, mon_num, now.year)

def epoch_date(n):
    """ converts any given date in m/d/y format to unix epoch.
        date_monday for strava.py is converted in this case """
    unix_epoch = time.mktime(datetime.datetime.strptime(n, '%m/%d/%Y').timetuple())
    return '%.0f' % unix_epoch