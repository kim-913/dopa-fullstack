import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.helpers import send_file
from flask.wrappers import Request
from flask_app.models.model import Users,Notes,Accounts
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import operator

bcrypt = Bcrypt(app)     

@app.route('/accounts')
def account():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':session['user_id']
    }
    all_acc=Accounts.get_all(data)

    return render_template("accounts.html",all=all_acc)

@app.route('/accounts/create',methods=['POST'])
def create_acc():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'name':request.form['name'],
        'link':request.form['link'],
        'user_name':request.form['user_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'comment':request.form['comment'],
        'user_id':session['user_id']
    }
    new= Accounts.add(data)
    print(new)
    return redirect('/accounts')


@app.route('/accounts/update',methods=['post'])
def update_acc():
    if 'user_id' not in session:
        return render_template("index.html")
    
    data={
        'id':request.form['id'],
        'name':request.form['name'],
        'link':request.form['link'],
        'user_name':request.form['user_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'comment':request.form['comment'],
    }
    data_del={
        'id':request.form['id']
    }
    if request.form['submit']=='Update':
        all_note = Accounts.update(data)
    if request.form['submit']=='Delete':
        delete = Accounts.delete(data_del)
    return redirect('/accounts')

@app.route('/account/search',methods=['get'])
def search_acc():
    if 'user_id' not in session:
        return render_template("index.html")
    content=request.args.get('search_content')
    type=request.args.get('search_type')
    data={
        'id':session['user_id'],
        'content':'%%'+content+'%%',
    }
    searchdata= Accounts.search(data,type)
    searchdata = sorted(searchdata, key=operator.attrgetter('updated_at'),reverse=True)

    return render_template("searchacc.html",search = searchdata,content=content,type=type)
