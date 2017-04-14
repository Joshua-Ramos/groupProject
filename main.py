from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_wtf import Form
from flask_wtf.file import FileField
from tools import s3_upload

app = Flask(__name__)
app.config['S3_KEY'] = 'AKIAJZ6GXZRQMZIAADIA'
app.config['S3_SECRET'] = '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'
app.config['S3_BUCKET'] = 'coursemat'
app.config['S3_UPLOAD_DIRECTORY'] = 'Testing'
app.config['SECRET_KEY'] = 'TestingSecretKey'

class UploadForm(Form):
    example = FileField()


@app.route('/', methods=['POST', 'GET'])
def home_page():
    if not session.get('logged_in'): return login_page()    # block access if not logged in

    return render_template('index.html')


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
