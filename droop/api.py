from flask import Flask
from flask.ext import restful

import sqlite3

DATABASE = 'C:/Antpile/Code/droopal/droop.db'

app = Flask(__name__)
api = restful.Api(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)