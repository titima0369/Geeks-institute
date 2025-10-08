from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description')
    organizer_id = SelectField('Organizer', coerce=int, validators=[DataRequired()])
