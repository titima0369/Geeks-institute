from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, BooleanField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from ..models import Category, Chef

def category_choices():
    return [(str(c.id), c.name) for c in Category.query.order_by(Category.name).all()]

def chef_choices():
    return [(str(c.id), c.name) for c in Chef.query.order_by(Chef.name).all()]

class ItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=150)])
    description = TextAreaField("Description")
    price = DecimalField("Price (MAD)", validators=[DataRequired(), NumberRange(min=0)], places=2, rounding=None)
    is_available = BooleanField("Available", default=True)
    category_id = SelectField("Category", choices=[], validate_choice=False)
    chef_ids = SelectMultipleField("Chefs", choices=[], validate_choice=False)
    submit = SubmitField("Save")
