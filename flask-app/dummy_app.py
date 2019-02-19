#!/usr/bin/env python
from google.appengine.ext import vendor
vendor.add('lib')

from flask import Flask
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/datetime')
def get_datetime():
    data = { 'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S') }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
