import datetime 
import time


def date_monday():
    """ returns day of the week from 0-6, then subtracted from
        current date to return monday's date for given week for any given week """
    now = datetime.datetime.now()
    day_number = datetime.datetime.today().weekday()
    mon_date = int(now.day) - day_number
    return '%d/%s/%d' % (now.month, mon_date, now.year)

def epoch_date(n):
    """ converts any given date in m/d/y format to unix epoch.
        date_monday for strava.py is converted in this case """
    unix_epoch = time.mktime(datetime.datetime.strptime(n, '%m/%d/%Y').timetuple())
    return '%.0f' % unix_epoch