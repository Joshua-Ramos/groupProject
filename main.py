from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_wtf import Form
from flask_wtf.file import FileField
from tools import s3_upload

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# AWS S3
app.config['S3_KEY'] = 'AKIAJZ6GXZRQMZIAADIA'
app.config['S3_SECRET'] = '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'
app.config['S3_BUCKET'] = 'coursemat'
app.config['S3_UPLOAD_DIRECTORY'] = 'Testing'
app.config['SECRET_KEY'] = 'TestingSecretKey'

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://CourseMate:password@localhost/CourseMate'


db = SQLAlchemy(app)
# from app import views, models

class Users(db.Model):  # http://stackoverflow.com/questions/29461959/flask-sqlalchemy-connect-to-mysql-database

    __tablename__ = 'User'

    id = db.Column('User_ID', db.Integer, primary_key=True)
    username = db.Column('Username', db.String, nullable=False)
    password = db.Column('Password', db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<title {}'.format(self.username)

import flask
@app.route('/testdb')  # http://stackoverflow.com/questions/29461959/flask-sqlalchemy-connect-to-mysql-database
def testdb():
    admin = Users('admin', 'password')
    user1 = Users('user1', 'password1')

    # db.session.add(admin)
    # db.session.add(user1)

    results = Users.query.all()

    json_results = []
    for result in results:
        d = {'username': result.username,
             'password': result.password}
        json_results.append(d)

    return flask.jsonify(items=json_results)


class UploadForm(Form):
    example = FileField()


@app.route('/', methods=['POST', 'GET'])
def home_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in

    return render_template('index.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email address']
        return 'fuck'
    return redirect(url_for('login_page'))



# try using flask-login, flask-user, flask-SQLAlchemy



@app.route('/login', methods = ['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('home_page'))
        else:
            return 'Invalid credentials. Please try again.'
    return render_template('login_screen/index.html')

@app.route('/courses')
def courses_page():
    if not session.get('logged_in'):return login_page()    # block access if not logged in

    return render_template('courses.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in

    form = UploadForm()
    if form.validate_on_submit():
        output = s3_upload(form.example)
        flash('{src} uploaded to S3 as {dst}'.format(src=form.example.data.filename, dst=output))
    return render_template('upload.html', form=form)


@app.route('/about')
def about_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in

    return render_template('about.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return login_page()


if __name__ == '__main__':
    app.run(debug=True)
