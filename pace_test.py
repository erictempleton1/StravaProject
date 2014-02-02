import datetime
from datetime import timedelta

now = datetime.datetime.now()
day_number = datetime.datetime.today().weekday()
current_year = now.year

    # failsafe for mondays with dates in prev months (31,30,29 ect)
mon_date = now - datetime.timedelta(days=day_number)
mon_num = mon_date.strftime('%d')
mon_year = int(mon_date.strftime('%Y'))
mon_monday = int(mon_date.strftime('%m'))


print mon_monday, mon_num, mon_year
print now.month, mon_num, now.year






