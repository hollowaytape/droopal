from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://droop.db'

class Tree(db.Model):
    __tablename__ = 'droop_tree'
    id = db.Column(db.Integer, primary_key = True)
    threshold = db.Column(db.Integer)
    ripeness = db.Column(db.Boolean)
    latitude = db.Column(db.Float(6))
    longitude = db.Column(db.Float(6))
    
class Reading(db.Model):
    __tablename__ = "droop_reading"
    id = db.Column(db.Integer, primary_key = True)
    tree = db.Column(db.ForeignKey("Tree.id"), nullable=False)
    date_time = db.Column(db.DateTime)
    value = db.Column(db.Integer)

if __name__ == '__main__':
  app.run(debug=True)

"""api.add_resource(TreeAPI, '/', endpoint = 'tree')

@app.route('/trees/')
def trees_index():
    # return render_template('tree_index.html')
    return jsonify
    
    
@app.route('/trees/<id>')
def tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run(debug=True)"""