from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ChefForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=120)])
    bio = TextAreaField("Bio")
    submit = SubmitField("Save")
