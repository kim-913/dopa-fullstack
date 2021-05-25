
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
        self.all_notes = Notes.get_all(data['id'])
        self.all_accs = Accounts.get_all(data['id'])

    @classmethod
    def get_one(cls,id):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM users where id = %(id)s;"
        user_info = mysql.query_db(query,id)
        return user_info

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
        query = "SELECT * FROM notebox where user_id = %(id)s and type= 'note';"
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


class Accounts:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.link = data['link']
        self.user_name=data['user_name']
        self.email=data['email']
        self.password=data['pw']
        self.comment=data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.userinfo=Users.get_one(data['user_id'])

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM accountbox where id =  %(id)s;"
        one_acc = mysql.query_db(query,name)

        return one_acc

    @classmethod
    def get_all(cls,id):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM accountbox where user_id = %(id)s ;"
        all_acc = mysql.query_db(query,id)
        all = []
        for b in all_acc:
            all.append(cls(b))
        return all


    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO accountbox(name,link,user_name,email,pw,comment,user_id) VALUES(%(name)s,%(link)s,%(user_name)s,%(email)s,%(password)s,%(comment)s,%(user_id)s);"
        new_acc = mysql.query_db(query,data)
        return new_acc

    @classmethod
    def update(cls,data):
        mysql = connectToMySQL("dopa")
        query="UPDATE accountbox SET name = %(name)s, link=%(link)s,user_name=%(user_name)s,email=%(email)s,comment=%(comment)s, pw=%(password)s WHERE id = %(id)s;"
        update_acc =mysql.query_db(query,data)
        print(update_acc)
        return update_acc

    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("dopa")
        query="DELETE FROM accountbox WHERE id = %(id)s;"
        remove = mysql.query_db(query,id)
        print(remove)
        return remove


class Links:
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
        query = "SELECT * FROM notebox where user_id = %(id)s and type= 'link';"
        all_notes = mysql.query_db(query,id)
        all = []
        for b in all_notes:
            all.append(cls(b))
        return all


    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO notebox(name,note,type,user_id) VALUES(%(name)s,%(note)s,'link',%(user_id)s);"
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


class Videos:
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
        query = "SELECT * FROM notebox where user_id = %(id)s and type= 'video';"
        all_notes = mysql.query_db(query,id)
        all = []
        for b in all_notes:
            all.append(cls(b))
        return all


    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO notebox(name,note,type,user_id) VALUES(%(name)s,%(note)s,'video',%(user_id)s);"
        new_note = mysql.query_db(query,data)
        return new_note

    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("dopa")
        query="DELETE FROM notebox WHERE id = %(id)s;"
        remove = mysql.query_db(query,id)
        return remove


class Medias:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.file=data['file']
        self.created_at = data['CREATED_AT']
        self.updated_at = data['UPDATED_AT']
        self.type=data['type']
        self.userinfo=Users.get_one(data['user_id'])

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM filebox where id =  %(id)s;"
        one_note = mysql.query_db(query,name)
        print(one_note)
        return one_note

    @classmethod
    def get_all(cls,id):
        mysql = connectToMySQL("dopa")
        query = "SELECT * FROM filebox where user_id = %(id)s and type='media' ;"
        all_notes = mysql.query_db(query,id)
        all = []
        for b in all_notes:
            all.append(cls(b))
        return all

    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dopa")
        query="INSERT INTO filebox(name,file,type,user_id) VALUES(%(name)s,%(file)s,'media',%(user_id)s);"
        new_note = mysql.query_db(query,data)
        return new_note

    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("dopa")
        query="DELETE FROM filebox WHERE id = %(id)s;"
        remove = mysql.query_db(query,id)
        return remove