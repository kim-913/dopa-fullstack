import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.helpers import send_file
from flask.wrappers import Request
from flask_app.models.model import Users,Notes
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



    return render_template("accounts.html")

# @app.route('/notes/create',methods=['POST'])
# def create_note():
#     if 'user_id' not in session:
#         return render_template("index.html")
#     data={
#         'name':request.form['name'],
#         'note':request.form['note'],
#         'user_id':session['user_id']
#     }
#     new= Notes.add(data)
#     return redirect('/notes')

# @app.route('/notes/<id>')
# def edit_note(id):
#     if 'user_id' not in session:
#         return render_template("index.html")
#     data2={
#         'id':id
#     }
#     data={
#         'id':session['user_id']
#     }
#     all_note = Notes.get_all(data)
#     sorted_all_notes = sorted(all_note, key=operator.attrgetter('updated_at'),reverse=True)

#     update=Notes.get_one(data2)
#     return render_template('updatenote.html',all=sorted_all_notes,update=update)

# @app.route('/notes/<id>/update',methods=['post'])
# def update_note(id):
#     if 'user_id' not in session:
#         return render_template("index.html")
#     data={
#         'id':id,
#         'name':request.form['name'],
#         'note':request.form['note'],
#     }
#     all_note = Notes.update(data)
#     return redirect('/notes')

# @app.route('/notes/<id>/delete')
# def delete_note(id):
#     if 'user_id' not in session:
#         return render_template("index.html")
#     data={
#         'id':id,
#     }
#     all_note = Notes.delete(data)
#     return redirect('/notes')
