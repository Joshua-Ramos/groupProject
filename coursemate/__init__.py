from flask import Flask


app = Flask(__name__)
app.config.from_object('coursemate.config.DevConfig')

with app.app_context():
    import coursemate.views


