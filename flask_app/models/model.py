
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt        
from flask_app import app

bcrypt = Bcrypt(app)     
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]') 

class Users:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.email=data['email']
        self.pw=data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls,id):
        mysql = connectToMySQL("dopa")
        users = mysql.query_db("SELECT * FROM users where id = %(id)s;")
        print(users)
        return users
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO users(name,email,pw) VALUES(%(name)s,%(email)s,%(pw)s);"
        new_user = mysql.query_db(query,data)
        return new_user

    @classmethod
    def get_one_by_email(cls, email):
        mysql = connectToMySQL("dopa")
        query = 'SELECT * FROM users WHERE email = %(users_email)s;'
        data = {
            "users_email": email
        }
        one_user = mysql.query_db(query, data)
        print(one_user)
        return one_user

class Notes:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.note=data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.userinfo=Users.get_one(data['user_id'])

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("dopa")
        notes = mysql.query_db("SELECT * FROM notebox where name = %(name)s and user_id= %(id)s;")
        print(notes)
        return notes

    @classmethod
    def get_all(cls,id):
        mysql = connectToMySQL("dopa")
        all_notes = mysql.query_db("SELECT * FROM notebox where user_id = %(id)s;")
        print(all_notes)
        return all_notes

    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO notebox(name,note) VALUES(%(name)s,%(note)s);"
        new_note = mysql.query_db(query,data)
        return new_note
