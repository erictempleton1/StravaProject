from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, IntegerField, validators

class ContactForm(Form):
    name = TextField('Name', [validators.Required('Please enter your name')])
    email = TextField('Email', [validators.Required('Please enter your email'), validators.Email('Please enter your email')])
    subject = TextField('Subject', [validators.Required('Please enter a subject')])
    message = TextAreaField('Message', [validators.Required('Please enter a message')])
    submit = SubmitField('Send')

class GoalForm(Form):
    goal = IntegerField('Week Goal (1 - 150 miles)', [validators.NumberRange(min=1, max=150), validators.Required('Please enter a number from 1 to 150')])
    submit = SubmitField('Submit')