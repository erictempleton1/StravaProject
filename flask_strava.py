import datetime
from strava import Calcs
from flask import Flask, render_template, request, redirect, flash, url_for
from forms import GoalForm
from flask_mail import Message, Mail

app_strava = Flask(__name__)
app_strava.secret_key = 'dev key'


@app_strava.route('/', methods=['GET', 'POST'])
def index_strava():
    calcs = Calcs()
    form = GoalForm()

    date = datetime.datetime.now()  
  
    week_date = 'Weekly Totals as of %s:' % date.strftime('%m/%d/%Y')
    week_miles = '%.1f miles' % calcs.week_total_miles()
    week_total_time = '%s total time' % calcs.time_list() 
    num_runs = calcs.num_runs()
    avg_miles = '%.1f miles/run' % calcs.avg_miles() 
    avg_pace = '%s mins/mile avg pace' % calcs.avg_pace()

    # Mon - Sun per day miles including doubles
    week_layout = calcs.week_layout()

    week_totals = [week_miles, num_runs, week_total_time, avg_miles, avg_pace]

    return render_template('strava.html', week_date=week_date, week_totals=week_totals,
                            week_layout=week_layout, title='Home', form=form)


@app_strava.route('/goals', methods = ['GET', 'POST'])
def goals():
    calcs = Calcs()
    form = GoalForm()

    if request.method == 'POST' and form.validate() == True:
        goal = form.goal.data
        avg_to_goal = '%.1f miles/day to reach goal' % calcs.avg_to_goal(goal)
        miles_remain = '%.1f miles remain' % calcs.miles_remaining(goal)
        days_remain = '%.0f days remaining' % calcs.days_remaining()
        week_goal = '%.0f miles' % calcs.week_goal(goal)
        week_goals = [week_goal, miles_remain, days_remain, avg_to_goal]
        return redirect(url_for('index_strava'))
    else:
        flash('Please enter a number from 1-100')
        return redirect(url_for('index_strava'))

if __name__ == '__main__':
    app_strava.run(debug=True)
    