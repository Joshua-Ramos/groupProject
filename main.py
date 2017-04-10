from flask import Flask, render_template, flash, request, session
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
    if not session.get('logged_in'):
        return render_template('login_screen/index.html')
    else:
        return render_template('Course_Mate.html')

@app.route('/login', methods = ['POST', 'GET'])
def login_handle():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('Course_Mate.html')
    else:
        return '<h1> Incorrect logon </h1>'



@app.route('/upload', methods = ['POST', 'GET'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        output = s3_upload(form.example)
        flash('{src} uploaded to S3 as {dst}'.format(src=form.example.data.filename, dst=output))
    return render_template('example.html', form = form)


if __name__ == '__main__':
    app.run()
