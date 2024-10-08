from . import db
from datetime import datetime
from flask_login import UserMixin 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content_md = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text) 
    thumbnail = db.Column(db.String(255))  
    author = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_data = db.Column(db.LargeBinary, nullable=False)
    image_name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)