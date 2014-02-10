import datetime
from strava import Calcs
from flask import Flask, render_template, request, redirect, flash
from contact_form import ContactForm
from flask_mail import Message, Mail


app_strava = Flask(__name__)
app_strava.secret_key = 'dev key'

mail = Mail()
app_strava.config['MAIL_SERVER'] = 'smtp.gmail.com'
app_strava.config['MAIL_PORT'] = 465
app_strava.config['MAIL_USE_SSL'] = True
app_strava.config['MAIL_USERNAME'] = 'milesdash4@gmail.com'
app_strava.config['MAIL_PASSWORD'] = 'milesdash'
mail.init_app(app_strava)


@app_strava.route('/')
def index_strava():
    calcs = Calcs()

    date = datetime.datetime.now()  
      
    week_date = 'Weekly Totals as of %s:' % date.strftime('%m/%d/%Y')
    week_miles = '%.1f miles' % calcs.week_total_miles()
    miles_remain = '%.1f miles remain' % calcs.miles_remaining()
    week_total_time = '%s total time' % calcs.time_list() 
    num_runs = calcs.num_runs()
    avg_miles = '%.1f avg miles/run' % calcs.avg_miles() 
    days_remain = '%.0f days remaining' % calcs.days_remaining()
    avg_to_goal = '%.1f miles/day to reach goal' % calcs.avg_to_goal()
    avg_pace = '%s mins/mile avg pace' % calcs.avg_pace()
    week_goal = 'Week goal: %.0f miles' % calcs.week_goal()
    week_layout = calcs.week_layout()

    week_totals = [week_miles, num_runs, week_total_time, avg_miles, avg_pace]

    week_goals = [week_goal, days_remain, miles_remain, avg_to_goal] 

    return render_template('strava.html', week_date=week_date, week_totals=week_totals,
                            week_goals=week_goals, week_layout=week_layout)

@app_strava.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('contact.html', form=form)    
        return 'Form posted'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app_strava.route('/test')
def form():
    return render_template('forms.html')

@app_strava.route('/response', methods=['POST'])
def hello():
    name=request.form['yourname']
    return render_template('form_action.html', name=name)

if __name__ == '__main__':
    app_strava.run(debug=True)
    