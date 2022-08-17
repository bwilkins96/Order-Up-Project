from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, PasswordField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AssignForm(FlaskForm):
    employee_number = StringField('Employee Number', validators=[DataRequired()])
    table_number = StringField('Table Number', validators=[DataRequired()])
    submit = SubmitField('Assign')

class CloseTableForm(FlaskForm):
    table_number = StringField('Table Number', validators=[DataRequired()])
    submit = SubmitField('Close Table', validators=[DataRequired()])

class OrderForm(FlaskForm):
    food_id = StringField('Food ID', validators=[DataRequired()])
    order_id = StringField('Order ID', validators=[DataRequired()])
    table_number = StringField('Table Number', validators=[DataRequired()])
    submit = SubmitField('Add to Order')
