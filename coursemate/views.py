import flask
from flask import current_app as app
from flask import render_template, session, request, redirect, url_for, flash

from .models import User
from .models import Course
from .models import db
from .forms import UploadForm
from .tools import s3_upload


@app.route('/bstest')
def bstest():
    return render_template('bootstrap.html')

@app.route('/', methods=['POST', 'GET'])
def home_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in
    name = session.get('username')
    return render_template('index.html', username=name)


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
            session['username'] = new_user.username
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
                    session['username'] = user.username
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
