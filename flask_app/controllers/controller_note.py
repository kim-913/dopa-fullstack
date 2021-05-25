import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.helpers import send_file
from flask.wrappers import Request
from flask_app.models.model import Users,Notes,Links
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import operator
import pytube

bcrypt = Bcrypt(app)     

@app.route('/notes')
def note():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':session['user_id']
    }

    all_note = Notes.get_all(data)
    sorted_all_notes = sorted(all_note, key=operator.attrgetter('updated_at'),reverse=True)

    print(sorted_all_notes)
    return render_template("notes.html",all=sorted_all_notes)

@app.route('/notes/create',methods=['POST'])
def create_note():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'name':request.form['name'],
        'note':request.form['note'],
        'user_id':session['user_id']
    }
    new= Notes.add(data)
    return redirect('/notes')

@app.route('/notes/<id>')
def edit_note(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data2={
        'id':id
    }
    data={
        'id':session['user_id']
    }
    all_note = Notes.get_all(data)
    
    sorted_all_notes = sorted(all_note, key=operator.attrgetter('updated_at'),reverse=True)

    update=Notes.get_one(data2)
    if update[0]['user_id']==session['user_id']:
        return render_template('updatenote.html',all=sorted_all_notes,update=update)
    else:
        return redirect('/notes')

@app.route('/notes/<id>/update',methods=['post'])
def update_note(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':id,
        'name':request.form['name'],
        'note':request.form['note'],
    }
    all_note = Notes.update(data)
    return redirect('/notes')

@app.route('/notes/<id>/delete')
def delete_note(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':id,
    }
    all_note = Notes.delete(data)
    return redirect('/notes')

#beyond is for links since they are in same database

@app.route('/links')
def link():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':session['user_id']
    }

    all_link = Links.get_all(data)
    sorted_all_links = sorted(all_link, key=operator.attrgetter('updated_at'),reverse=True)

    print(sorted_all_links)
    return render_template("links.html",all=sorted_all_links)

@app.route('/links/create',methods=['POST'])
def create_link():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'name':request.form['name'],
        'note':request.form['note'],
        'user_id':session['user_id']
    }
    new= Links.add(data)
    return redirect('/links')


@app.route('/links/<id>')
def edit_link(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data2={
        'id':id
    }
    data={
        'id':session['user_id']
    }
    all_link = Links.get_all(data)
    sorted_all_links = sorted(all_link, key=operator.attrgetter('updated_at'),reverse=True)
    update=Links.get_one(data2)
    if update[0]['user_id']==session['user_id']:
        return render_template('updatelink.html',all=sorted_all_links,update=update)
    else:
        return redirect('/notes')

@app.route('/links/<id>/update',methods=['post'])
def update_link(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':id,
        'name':request.form['name'],
        'note':request.form['note'],
    }
    all_note = Links.update(data)
    return redirect('/links')

@app.route('/links/<id>/delete')
def delete_link(id):
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':id,
    }
    all_note = Links.delete(data)
    return redirect('/links')