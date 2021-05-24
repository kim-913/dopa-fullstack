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

@app.route('/medias')
def media():
    if 'user_id' not in session:
        return render_template("index.html")

    return render_template("medias.html")
