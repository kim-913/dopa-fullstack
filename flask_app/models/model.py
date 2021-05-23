
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
    def get_one(cls,name):
        mysql = connectToMySQL("dopa")
        users = mysql.query_db("SELECT * FROM users where name = %(name)s;")
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

