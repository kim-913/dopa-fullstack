
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
        self.note=data['note']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.type=data['type']
        self.userinfo=Users.get_one(data['user_id'])

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM notebox where id =  %(id)s;"
        one_note = mysql.query_db(query,name)

        print(one_note)
        return one_note

    @classmethod
    def get_all(cls,id):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM notebox where user_id = %(id)s;"
        all_notes = mysql.query_db(query,id)
        all = []
        for b in all_notes:
            all.append(cls(b))
        return all


    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO notebox(name,note,type,user_id) VALUES(%(name)s,%(note)s,'note',%(user_id)s);"
        new_note = mysql.query_db(query,data)
        return new_note

    @classmethod
    def update(cls,data):
        mysql = connectToMySQL("dopa")
        query="UPDATE notebox SET name = %(name)s, note=%(note)s WHERE id = %(id)s;"
        update_note =mysql.query_db(query,data)
        return update_note

    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("dopa")
        query="DELETE FROM notebox WHERE id = %(id)s;"
        remove = mysql.query_db(query,id)
        return remove