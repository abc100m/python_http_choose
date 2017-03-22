#wsgi.py
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"

@app.route('/uwsgi/')
def index1():
    return "<span style='color:blue'>I am app 2</span>"

port = 8080
if len(sys.argv) > 1:
    port = int(sys.argv[1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
