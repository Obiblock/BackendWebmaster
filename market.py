from flask import Flask 
app = Flask(__name__)

@app.route('/admin')
def hello_world():
    return '<h1>Hello, World h1!<h1>'