
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

@app.route('/search',methods=['GET','POST'])
def search():
    content=request.args.get('search_content')
    type=request.args.get('search_type')
    data={
        'id':session['user_id'],
        'content':'%%'+content+'%%'
    }
    if type == 'Notes':
        searchdata=Notes.search(data)
        searchdata = sorted(searchdata, key=operator.attrgetter('updated_at'),reverse=True)
        print(searchdata)
    elif type == 'Links':
        searchdata=Links.search(data)
        searchdata = sorted(searchdata, key=operator.attrgetter('updated_at'),reverse=True)
    elif type == 'Images':
        searchdata=Medias.search(data)
        searchdata = sorted(searchdata, key=operator.attrgetter('updated_at'),reverse=True)
    elif type == 'Videos':
        searchdata=Videos.search(data)
        searchdata = sorted(searchdata, key=operator.attrgetter('updated_at'),reverse=True)
    return render_template("search.html",search_content=content,search_type=type,search=searchdata)



@app.route('/search/video/delete',methods=['POST'])
def delete():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':request.form['id']
    }
    all_note = Videos.delete(data)
    return redirect('/search')