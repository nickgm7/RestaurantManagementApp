from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cam:admin@localhost/chuckles'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Manager(db.Model):
    __tablename__ = 'manager'
    manager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    salary = db.Column(db.REAL)

    def __init__(self, manager_id, name, salary):
        self.manager_id = manager_id
        self.name = name
        self.salary = salary

class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone_num = db.Column(db.String(200))

    def __init__(self, customer_id,name, address, phone_num):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_num = phone_num

class Waiter(db.Model):
    __tablename__ = 'waiter'
    waiter_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    salary = db.Column(db.REAL)

    def __init__(self, waiter_id, name, salary):
        self.waiter_id = waiter_id
        self.name = name
        self.salary = salary

class Chef(db.Model):
    __tablename__ = 'chef'
    chef_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    salary = db.Column(db.REAL)

    def __init__(self, chef_id, name, salary):
        self.chef_id = chef_id
        self.name = name
        self.salary = salary

class Dish(db.Model):
    __tablename__ = 'dish'
    dish_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(400))
    price = db.Column(db.REAL)

    def __init__(self, dish_id, name, description, price):
        self.dish_id = dish_id
        self.name = name
        self.description = description
        self.price = price

class Supplier(db.Model):
    __tablename__ = 'supplier'
    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    city = db.Column(db.String(200))
    phone_num = db.Column(db.String(200))

    def __init__(self, supplier_id, name, city, phone_num):
        self.supplier_id = supplier_id
        self.name = name
        self.city = city
        self.phone_num = phone_num

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    inventory = db.Column(db.Integer)
    
    def __init__(self, ingredient_id, name, inventory):
        self.ingredient_id = ingredient_id
        self.name = name
        self.inventory = inventory

class Order(db.Model):
    __tablename__ = 'order'
    customer_id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer)
    
    def __init__(self, customer_id, dish_id):
        self.customer_id = customer_id
        self.dish_id = dish_id

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    return render_template('order.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/authorizeLogin', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['userID']
        pw = request.form['password']
        if user == "admin" and pw == "admin":
            return redirect('/manager')
        # Error Message
        else:
            return render_template('login.html', message='Incorrect username or password')


@app.route('/submitChef', methods=['GET', 'POST'])
def addChef():
    if request.method == 'POST':
        chef_id = request.form['chef_id']
        name = request.form['name']
        salary = request.form['salary']
        if db.session.query(Chef).filter(Chef.chef_id == chef_id).count() == 0:
            new_entry = Chef(chef_id, name, salary)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())
    

@app.route('/deleteChef', methods=['GET', 'POST'])
def delChef():
    if request.method == 'POST':
        chef_id = request.form['chef_id']
        chef_to_remove = db.session.query(Chef).filter(Chef.chef_id == chef_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/submitWaiter', methods=['GET', 'POST'])
def addWaiter():
    if request.method == 'POST':
        waiter_id = request.form['waiter_id']
        name = request.form['name']
        salary = request.form['salary']
        if db.session.query(Waiter).filter(Waiter.waiter_id == waiter_id).count() == 0:
            new_entry = Waiter(waiter_id, name, salary)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteWaiter', methods=['GET', 'POST'])
def delWaiter():
    if request.method == 'POST':
        waiter_id = request.form['waiter_id']
        db.session.query(Waiter).filter(Waiter.waiter_id == waiter_id).delete()
        db.session.commit()

    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())


@app.route('/submitManager', methods=['GET', 'POST'])
def addManager():
    if request.method == 'POST':
        manager_id = request.form['manager_id']
        name = request.form['name']
        salary = request.form['salary']
        if db.session.query(Manager).filter(Manager.manager_id == manager_id).count() == 0:
            new_entry = Manager(manager_id, name, salary)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteManager', methods=['GET', 'POST'])
def delManager():
    if request.method == 'POST':
        manager_id = request.form['manager_id']
        db.session.query(Manager).filter(Manager.manager_id == manager_id).delete()
        db.session.commit()

    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())


@app.route('/submitCustomer', methods=['GET', 'POST'])
def addCustomer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        name = request.form['name']
        address = request.form['address']
        phone_num = request.form['phone_num']
        if db.session.query(Customer).filter(Customer.customer_id == customer_id).count() == 0:
            new_entry = Customer(customer_id, name, address, phone_num)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteCustomer', methods=['GET', 'POST'])
def delCustomer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        db.session.query(Customer).filter(Customer.customer_id == customer_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())


@app.route('/submitDish', methods=['GET', 'POST'])
def addDish():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        if db.session.query(Dish).filter(Dish.dish_id == dish_id).count() == 0:
            new_entry = Dish(dish_id, name, description, price)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteDish', methods=['GET', 'POST'])
def delDish():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        db.session.query(Dish).filter(Dish.dish_id == dish_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())


@app.route('/submitIngredient', methods=['GET', 'POST'])
def addIngredient():
    if request.method == 'POST':
        ingredient_id = request.form['i_id']
        name = request.form['name']
        inventory = request.form['qty']
        if db.session.query(Ingredient).filter(Ingredient.ingredient_id == ingredient_id).count() == 0:
            new_entry = Ingredient(ingredient_id, name, inventory)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteIngredient', methods=['GET', 'POST'])
def delIngredient():
    if request.method == 'POST':
        ingredient_id = request.form['ingredient_id']
        db.session.query(Ingredient).filter(Ingredient.ingredient_id == ingredient_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/submitSupplier', methods=['GET', 'POST'])
def addSupplier():
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']
        name = request.form['name']
        city = request.form['city']
        phone_num = request.form['phone_num']
        if db.session.query(Supplier).filter(Supplier.supplier_id == supplier_id).count() == 0:
            new_entry = Supplier(supplier_id, name,city, phone_num)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteSupplier', methods=['GET', 'POST'])
def delSupplier():
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']
        db.session.query(Supplier).filter(Supplier.supplier_id == supplier_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/submitOrder', methods=['GET', 'POST'])
def addOrder():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        dish_id = request.form['dish_id']
        if db.session.query(Order).filter(Order.customer_id == customer_id, Order.dish_id == dish_id).count() == 0:
            new_entry = Order(customer_id, dish_id)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/deleteOrder', methods=['GET', 'POST'])
def delOrder():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        dish_id = request.form['dish_id']
        db.session.query(Order).filter(Order.dish_id == dish_id, Order.customer_id == customer_id).delete()
        db.session.commit()
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())
    
@app.route('/manager', methods=['GET', 'POST'])
def manager():
    return render_template('manager.html', manager_table = Manager.query.all(), 
    customer_table = Customer.query.all(), waiter_table = Waiter.query.all(),
    dish_table = Dish.query.all(), supplier_table = Supplier.query.all(),
    chef_table = Chef.query.all(), ingredient_table = Ingredient.query.all(),
    order_table = Order.query.all())

@app.route('/customerInfo', methods=['GET', 'POST'])
def customerinfo():
    if request.method == 'GET':
        dish_id = request.args.get('dish_id')
    return render_template('customerinfo.html', test_value = dish_id)

@app.route('/getCustomerInfo', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        name = request.form['name']
        address = request.form['address']
        phone_num = request.form['phone_num']
        dish_id = request.form['dish_id']
        if db.session.query(Customer).filter(Customer.customer_id == customer_id).count() == 0:
            new_entry = Customer(customer_id, name, address, phone_num)
            db.session.add(new_entry)
            db.session.commit()
        if db.session.query(Order).filter(Order.customer_id == customer_id, Order.dish_id == dish_id).count() == 0:
            new_entry = Order(customer_id, dish_id)
            db.session.add(new_entry)
            db.session.commit()
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
