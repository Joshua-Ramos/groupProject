from flask import Flask


app = Flask(__name__)
app.config.from_object('config.DevConfig')

with app.app_context():
    import coursemate.views


app.run(debug=True)


