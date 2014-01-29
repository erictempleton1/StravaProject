import datetime
from strava import Calcs
from flask import Flask, render_template, request, redirect
app_strava = Flask(__name__)


@app_strava.route('/')
def index_strava():
    calcs = Calcs()

    date = datetime.datetime.now()  
      
    week_date = 'Weekly Totals as of %s:' % date.strftime('%m/%d/%Y')
    week_miles = '%.1f miles this week' % calcs.week_total_miles()
    miles_remain = '%.1f miles remain' % calcs.miles_remaining(calcs.week_goal(55))
    week_total_time = '%s time this week' % calcs.time_list() 
    num_runs = calcs.num_runs()
    avg_miles = '%.1f avg miles per day' % calcs.avg_miles() 
    days_remain = '%.0f days remaining this week' % calcs.days_remaining()
    avg_to_goal = '%.1f miles per day to reach goal' % calcs.avg_to_goal()
    avg_pace = '%s mins/mile avg pace' % calcs.avg_pace()
    week_goal = 'Week goal: %.0f miles' % calcs.week_goal(55)
    week_layout = calcs.week_layout()
    week_percent = '%.0f' % calcs.progress_percent()
    
    results_list = [week_goal, week_miles, miles_remain, week_total_time,
                    num_runs, avg_miles, days_remain, avg_to_goal, avg_pace]

    return render_template('strava.html', week_date=week_date, results_list=results_list,
                            week_layout=week_layout)

@app_strava.route('/test')
def form():
    return render_template('forms.html')

@app_strava.route('/response', methods=['POST'])
def hello():
    name=request.form['yourname']
    return render_template('form_action.html', name=name)

if __name__ == '__main__':
    app_strava.run(debug=True)
    