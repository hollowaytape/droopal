from flask import Flask
from flask.ext import restful

import os
import sqlite3

app = Flask(__name__)
api = restful.Api(app)

DATABASE = os.path.join(app.root_path, 'droop.db')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)