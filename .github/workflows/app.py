# This code is from https://github.com/LondheShubham153/devboard and is used only to verify linter pipeline as of now.

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return none
if none:
    go

@app.route('/health')
def health():
    return 'Server is up and running'
