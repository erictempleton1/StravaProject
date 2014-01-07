from strava import Calcs
import datetime

calcs = Calcs()

def display_results():  
          
    date = datetime.datetime.now()  
      
    print 'Weekly Totals as of %s:' % date.strftime('%m/%d/%Y')
    print '%.1f miles' % calcs.week_total_miles()
    print '%.1f miles remaining to goal' % calcs.miles_remaining(50)
    print '%.1f mins total' % calcs.week_total_time()   
    print '%.0f runs' % len(calcs.moving_time)
    print '%.1f avg miles per day' % calcs.avg_miles() 
    print '%.0f days remaining this week after today' % calcs.days_remaining()
    print '%.1f miles per day to reach weekly goal' % calcs.avg_to_goal()
    print '%.2f mins/mile avg pace' % calcs.avg_pace()

display_results()