import time

import flask
from .helpers.login_helpers import acceptable_username
from .helpers.login_helpers import acceptable_password
from flask import current_app as app
from flask import render_template, session, request, redirect, url_for, flash

from .models import User
from .models import Course
from .models import Post
from .models import File
from .models import db
from .forms import UploadForm
from .tools import s3_upload, s3_download



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
    ######TO DO REPLACE ASSERT WITH HTML UPDATES TO USER####
    assert(acceptable_username(username) == True)
    assert(acceptable_password(password) == True)
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


@app.route('/courses', methods=['POST', 'GET'])
def courses_page():
    if not session.get('logged_in'):return login_page()    # block access if not logged in
    if request.method == 'POST':
        course_name = request.form['input']
        flask.flash(course_name)
        new_course = Course(course_name)
        db.session.add(new_course)
        db.session.commit()
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)


@app.route('/courses/<course_name>', methods = ['POST', 'GET'])
def course_page(course_name):
    course = Course.query.filter_by(name=course_name).all()[0]  # hacky but good enough  for now (milestone 5)
    course_id = course.id
    if request.method == 'POST':
        post_title  = request.form['title']
        post_content = request.form['content']
        username = session['username']
        userid = User.query.filter_by(username=username)[0].id
        post_time = time.strftime('%Y-%m-%d %H:%M:%S')
        new_post = Post(post_title, course_id, userid, post_content, post_time)
        db.session.add(new_post)
        db.session.commit()
    if not session.get('logged_in'): return login_page()    # block access if not logged in
    posts = Post.query.filter_by(course=course_id).all()
    files = File.query.filter_by(course_id=course_id).all()
    return render_template('course.html', title=course_name, posts=posts, files = files)


@app.route('/courses/<course_name>/files/<file_name>', methods = ['GET'])
def download_file(course_name, file_name):
    s3_download(file_name)
    return course_page(course_name)


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
