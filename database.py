from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
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

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    return render_template('signUp.html')

@app.route('/manager')
def manager():
    return render_template('manager.html')


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/supplier')
def supplier():
    return render_template('supplier.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
