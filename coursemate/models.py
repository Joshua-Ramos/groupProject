from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):  # http://stackoverflow.com/questions/29461959/flask-sqlalchemy-connect-to-mysql-database

    __tablename__ = 'User'

    id = db.Column('User_ID', db.Integer, primary_key=True)
    username = db.Column('Username', db.String, nullable=False)
    password = db.Column('Password', db.String, nullable=False)
    email = db.Column('Email', db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return '<title {}'.format(self.username)

class Course(db.Model):
    __tablename__ = 'Class'

    name = db.Column('Class_Name', db.String, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
