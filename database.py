from dotenv import load_dotenv
load_dotenv()
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name='Margot', employee_number=1234, password='password')
    db.session.add(employee)

    beverages = MenuItemType(name='Beverages')
    entrees = MenuItemType(name='Entrees')
    sides = MenuItemType(name = 'Sides')

    dinner = Menu(name='Dinner')

    fries = MenuItem(name='French Fries', price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name='Dr. Pepper', price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name='Jambalaya', price=21.98, type=entrees, menu=dinner)

    db.session.add(dinner)

    table1 = Table(number=1, capacity=4, open=True)
    table2 = Table(number=2, capacity=8, open=True)

    db.session.add(table1)
    db.session.add(table2)
    db.session.commit()
