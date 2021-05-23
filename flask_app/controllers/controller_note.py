import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app.models.model import Users,Notes
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)     

@app.route('/notes')
def note():
    if 'user_id' in session:
        return render_template("notes.html")
    return render_template("index.html")

@app.route('/notes/create',methods=['POST'])
def create_note():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'name':request.form['name'],
        'note':request.form['note'],
    }
    new= Notes.add(data)
    return redirect('/notes')