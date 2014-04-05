from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, IntegerField, validators

class GoalForm(Form):
    goal = IntegerField('Week Goal', [validators.NumberRange(min=1, max=150), validators.Required('Please enter a number from 1 to 150')])
