from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Employee, Menu, MenuItem, Table, Order, OrderDetail
from app.forms import AssignForm, CloseTableForm, OrderForm
from app import db

bp = Blueprint('orders', __name__, url_prefix='')

@bp.route('/')
@login_required
def index():
    menu_items = MenuItem.query.all()
    employees = Employee.query.all()
    tables = Table.query.all()
    order_details = OrderDetail.query.all()

    return render_template('orders.html', tables=tables, employees=employees, menu_items=menu_items, order_details=order_details)


@bp.route('/assign', methods=['GET', 'POST'])
def assign():
    assign_form = AssignForm()

    if assign_form.validate_on_submit():
        handle_assign(assign_form)

    return render_template('assign.html', assign=assign_form, title='Assign Employee')

@bp.route('/close', methods=['GET', 'POST'])
def close():
    close_form = CloseTableForm()

    if close_form.validate_on_submit():
        handle_close(close_form)

    return render_template('close.html', close=close_form, title='Close Table')

@bp.route('/order', methods=['GET', 'POST'])
def order():
    order_form = OrderForm()

    if order_form.validate_on_submit():
        handle_order(order_form)

    return render_template('order_form.html', order=order_form, title='Order Form')


def handle_assign(form):
    employee = Employee.query.filter_by(employee_number=form.employee_number.data).first()
    table = Table.query.filter_by(number=form.table_number.data).first()

    table.employee_id = employee.id
    table.open = False
    db.session.commit()

def handle_close(form):
    table = Table.query.filter_by(number=form.table_number.data).first()
    order = Order.query.filter_by(table_id=table.id).first()

    table.open = True
    table.employee_id = None
    order.finished = True

    db.session.delete(order)

    db.session.commit()

def handle_order(form):
    order = Order.query.get(form.order_id.data)
    table = Table.query.filter_by(number=form.table_number.data).first()

    if not order:
        order = Order(id=form.order_id.data, employee_id=table.employee_id, table_id=table.id, finished=False)
        table.open = False
        db.session.add(order)
        db.session.commit()

    order_detail = OrderDetail(order_id=order.id, menu_item_id=form.food_id.data)
    db.session.add(order_detail)
    db.session.commit()
