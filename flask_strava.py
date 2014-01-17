import sys, os
INTERP = os.path.join(os.environ['HOME'], 'django.runthescript.com', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
 
sys.path.append('django')
from django import app as application


import datetime
from strava import Calcs
from flask import Flask, render_template
app_strava = Flask(__name__)


@app_strava.route('/')
def index_strava():
    calcs = Calcs()

    date = datetime.datetime.now()  
      
    week_date = 'Weekly Totals as of %s:' % date.strftime('%m/%d/%Y')
    week_miles = '%.1f miles' % calcs.week_total_miles()
    miles_remain = '%.1f miles remaining to goal' % calcs.miles_remaining(50)
    week_total_time = '%.1f mins total' % calcs.week_total_time()   
    moving_time = '%.0f runs' % len(calcs.moving_time)
    avg_miles = '%.1f avg miles per day' % calcs.avg_miles() 
    days_remain = '%.0f days remaining this week after today' % calcs.days_remaining()
    avg_to_goal = '%.1f miles per day to reach weekly goal' % calcs.avg_to_goal()
    avg_pace = '%.2f mins/mile avg pace' % calcs.avg_pace()

    return render_template('strava.html', week_date=week_date, week_miles=week_miles, 
                            miles_remain=miles_remain, avg_pace=avg_pace, week_total_time=week_total_time,
                            moving_time=moving_time, avg_miles=avg_miles, days_remain=days_remain,
                            avg_to_goal=avg_to_goal,)

if __name__ == '__main__':
    app_strava.run(debug=True)
    