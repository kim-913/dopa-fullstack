import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from werkzeug import datastructures
from flask_app.models.model import Users,Notes,Links,Videos,Medias
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import operator

bcrypt = Bcrypt(app)     

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/dashboard')
def success():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':session["user_id"]
    }
    User_info=Users.get_one(data)
    user_id_data={
        'id':User_info[0]['id']
    }
    All_note=Notes.get_all(user_id_data)
    All_link=Links.get_all(user_id_data)
    All_image=Medias.get_all(user_id_data)
    All_video=Videos.get_all(user_id_data)
    sorted_all_notes = sorted(All_note, key=operator.attrgetter('updated_at'),reverse=True)
    sorted_all_links = sorted(All_link, key=operator.attrgetter('updated_at'),reverse=True)
    sorted_all_image = sorted(All_image, key=operator.attrgetter('updated_at'),reverse=True)

    sorted_all_videos = sorted(All_video, key=operator.attrgetter('updated_at'),reverse=True)

    print(All_note)
    return render_template('dashboard.html',all_note=sorted_all_notes,all_link=sorted_all_links,all_image=sorted_all_image,all_video=sorted_all_videos)

@app.route('/create',methods=['post'])
def create():
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data={
        'name':request.form['name'],
        'email':request.form['email'],
        'pw':pw_hash
    }
    new= Users.add(data)
    session['user_id'] = new
    return redirect('/dashboard')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/contactinfo')
def about():

    return render_template('about.html')
@app.route('/files')
def file():

    return render_template('files.html')
@app.route('/friends')
def friends():

    return render_template('friends.html')


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

