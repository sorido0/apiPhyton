from flask import Flask
app = Flask(__name__)

@app.route('/sorido0')
def hello_world():
    return 'Hello, World!'
