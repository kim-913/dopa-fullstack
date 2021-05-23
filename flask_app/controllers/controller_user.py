import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app.models.model import Users
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)     

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template("dashboard.html")
    return render_template("index.html")

@app.route('/dashboard')
def success():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('dashboard.html')

@app.route('/create',methods=['post'])
def create():
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data={
        'name':request.form['name'],
        'email':request.form['email'],
        'pw':pw_hash
    }
    new= Users.add(data)
    print(new)
    session['user_id'] = new
    return redirect('/dashboard')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login',methods=['post'])
def login():
    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = Users.get_one_by_email(data['email'])
    if not user_in_db:
        flash("Invalid Email/Password",'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db[0]['pw'], request.form['pw']):
        flash("Invalid Email/Password",'login')
        return redirect('/')
    session['user_id'] = user_in_db[0]['id']

    return redirect("/dashboard")