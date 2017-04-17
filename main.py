from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_wtf import Form
from flask_wtf.file import FileField
from tools import s3_upload


import flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)


# AWS S3
app.config['S3_KEY'] = 'AKIAJZ6GXZRQMZIAADIA'
app.config['S3_SECRET'] = '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'
app.config['S3_BUCKET'] = 'coursemat'
app.config['S3_UPLOAD_DIRECTORY'] = 'Testing'
app.config['SECRET_KEY'] = 'TestingSecretKey'

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://CourseMate:password@localhost/CourseMate'


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


class UploadForm(Form):
    example = FileField()

@app.route('/bstest')
def bstest():
    return render_template('bootstrap.html')

@app.route('/', methods=['POST', 'GET'])
def home_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in
    test = 'sdfsd'
    return render_template('index.html', username=test)


@app.route('/signup', methods=['POST', 'GET'])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email address']
        new_user = User(username, password, email)
        available = True
        for user in User.query.all():
            if new_user.username == user.username:
                available = False
        if available:
            db.session.add(new_user)
            db.session.commit()
            session['logged_in'] = True
            return redirect(url_for('home_page'))
        else:
            flask.flash('username is already in use')

    return redirect(url_for('login_page'))



# try using flask-login, flask-user
@app.route('/login', methods = ['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        valid_user = False
        users = User.query.all()
        if request.form['username'] in users:
            session['logged_in'] = True
        for user in users:  # check if use exists. there's gotta be a better way though
            if user.username == request.form['username']:
                valid_user = True
                if user.password == request.form['password']:
                    session['logged_in'] = True
                    break
                else:
                    flask.flash('invalid password')
                    break
        if not valid_user:
            flask.flash('invalid username')
        return redirect(url_for('home_page'))

    return render_template('login_screen/index.html')



@app.route('/courses')
def courses_page():
    if not session.get('logged_in'):return login_page()    # block access if not logged in

    courses = Course.query.all()

    return render_template('courses.html', courses=courses)


@app.route('/courses/<courseID>')
def course_page(courseID):
    if not session.get('logged_in'): return login_page()    # block access if not logged in
    return render_template('course.html', title=courseID)


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
