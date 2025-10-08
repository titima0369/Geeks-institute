from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CategoryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Save")
