from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class User(db.Model):  # http://stackoverflow.com/questions/29461959/flask-sqlalchemy-connect-to-mysql-database

    __tablename__ = 'User'

    id = db.Column('User_ID', db.Integer, primary_key=True)
    username = db.Column('Username', db.String, nullable=False)
    password = db.Column('Password', db.String, nullable=False)
    email = db.Column('Email', db.String, nullable=False)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return '<title {}'.format(self.username)

class Course(db.Model):
    __tablename__ = 'Class'

    name = db.Column('Class_Name', db.String, primary_key=True)
    id = db.Column('Class_ID', db.Integer)

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return self.name


class Post(db.Model):
    __tablename__ = 'Post'

    title = db.Column('Post_Name', db.String, primary_key=True, nullable=True)
    course = db.Column('Class_ID', db.String, primary_key=True, nullable=False)
    user = db.Column('User_ID', db.String, primary_key=True, nullable=False)
    content = db.Column('Post_Text', db.String, nullable=False)
    post_time = db.Column('Time', db.Date, nullable=False)





    def __init__(self, title, course, user, content, post_time):
        self.title = title
        self.course = course
        self.user = user
        self.content = content
        self.post_time = post_time

    def __repr__(self):
        return self.name


class File(db.Model):
    __tablename__ = 'File'

    name = db.Column('File_Name', db.String, primary_key = True, nullable = False)
    uploaded = db.Column('Uploaded', db.Date, primary_key = False, nullable = False)
    course_id = db.Column('course_id', db.Integer, primary_key = True, nullable = False)
    user_id = db.Column('User_ID', db.Integer, primary_key = False, nullable = False)

    def __init__(self, name, course_id, user_id):
        self.name = name
        self.course_id = course_id
        self.user_id = user_id
        self.uploaded = datetime.utcnow()


