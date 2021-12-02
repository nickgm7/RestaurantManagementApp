from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

app = Flask(__name__)

#app.config['SERVER_NAME'] = 'localhost:8000'

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/Restaurant'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = create_engine(app)
connection = engine.raw_connection()
cursor = connection.cursor()

# session = db.session()
# cursor = session.execute(app).cursor

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    return render_template('order.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)


@app.route('/manager')
def manager():
    cur = cursor
    resultValue = cur.execute("SELECT * FROM chef")
    if resultValue > 0:
        chefDetails = cur.fetchall()
    
    cur = cursor
    resultValue = cur.execute("SELECT * FROM waiter")
    if resultValue > 0:
        waiterDetails = cur.fetchall()

    return render_template('manager.html', chefDetails=chefDetails, waiterDetails=waiterDetails)

@app.route('/customerinfo')
def customerinfo():
    return render_template('customerinfo.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
