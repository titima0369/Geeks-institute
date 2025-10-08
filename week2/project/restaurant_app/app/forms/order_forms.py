from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired, NumberRange
from ..models import MenuItem

def item_choices():
    return [(str(i.id), i.title) for i in MenuItem.query.order_by(MenuItem.title).all()]

class OrderLineForm(FlaskForm):
    menu_item_id = SelectField("Item", choices=[], validate_choice=False)
    quantity = IntegerField("Qty", validators=[NumberRange(min=1)], default=1)

class OrderForm(FlaskForm):
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    lines = FieldList(FormField(OrderLineForm), min_entries=3, max_entries=10)
    submit = SubmitField("Create Order")
