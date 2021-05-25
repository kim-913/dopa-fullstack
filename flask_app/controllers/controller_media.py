import re
from types import DynamicClassAttribute, MethodDescriptorType
from flask.globals import current_app
from flask.helpers import send_file
from flask.wrappers import Request
from flask_app.models.model import Users,Notes,Accounts,Medias,Videos
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import operator
from urllib.parse import urlparse, parse_qs
import base64


bcrypt = Bcrypt(app)     


def get_yt_video_id(url):

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url
        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError

@app.route('/medias')
def media():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':session['user_id']
    }
    all_medias=Medias.get_all(data)
    all_video=Videos.get_all(data)
    sorted_all_medias = sorted(all_medias, key=operator.attrgetter('created_at'),reverse=True)
    sorted_all_video = sorted(all_video, key=operator.attrgetter('created_at'),reverse=True)
    
    return render_template("medias.html",all=sorted_all_medias,allv=sorted_all_video)



@app.route('/medias/image', methods=['post'])
def up_photo():
    img = request.files["file"]
    base64_data = base64.b64encode(img.read())
    data={
        "name":request.form['name'],
        'file':base64_data,
        'user_id':session['user_id']
    }
    new_image=Medias.add(data)
    return redirect('/medias')

@app.route('/image/delete',methods=['post'])
def delete_image():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':request.form['id']
    }
    all_note = Medias.delete(data)
    return redirect('/medias')


@app.route('/medias/video',methods=['post'])
def create_media():
    if 'user_id' not in session:
        return render_template("index.html")
    try:
        video_id=get_yt_video_id(request.form['note'])
        data={
                'name':request.form['name'],
                'note':video_id,
                'user_id':session['user_id'],
            }
        new_media= Videos.add(data)
        return redirect("/medias")
    except:
        return redirect("/medias")

@app.route('/video/delete',methods=['post'])
def delete_video():
    if 'user_id' not in session:
        return render_template("index.html")
    data={
        'id':request.form['id']
    }
    all_note = Videos.delete(data)
    return redirect('/medias')