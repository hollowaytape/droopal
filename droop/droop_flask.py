from flask import Flask
from flask.ext.restful import Api, Resource

import os
import sqlite3

app = Flask(__name__)
api = Api(app)

DATABASE = os.path.join(app.root_path, 'droop.db')

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

class TreeAPI(Resource):
    def get(self, id):
        pass
    
    def put(self, id):
        pass
        
    def delete(self, id):
        pass

api.add_resource(TreeAPI, '/', endpoint = 'tree')
    
@app.route('/trees/')
def trees_index():
    return render_template('tree_index.html')
    
@app.route('/trees/<id>')
def tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run(debug=True)