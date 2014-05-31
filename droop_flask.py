from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template

import os

app = Flask(__name__)
db = SQLAlchemy(app)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
os.path.join(PROJECT_DIR, 'droop.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///droop.db'

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
    
@app.route('/trees/', methods=['GET'])
def trees():
  if request.method == 'GET':
    results = Tree.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
      d = {'id': result.id,
           'threshold': result.threshold,
           'ripeness': result.ripeness,
           'latitude': result.latitude,
           'longitude': result.longitude}
      json_results.append(d)

    return jsonify(items=json_results)
    
@app.route('/trees/<int:id>/', methods=['GET'])
def tree(id):
    if request.method == 'GET':
        result = Tree.query.filter_by(id=id).first()
        d = {'id': result.id,
           'threshold': result.threshold,
           'ripeness': result.ripeness,
           'latitude': result.latitude,
           'longitude': result.longitude}
        json_results = d
            
        return jsonify(items=json_results)
    
@app.errorhandler(404)
def page_not_found_better_show_the_index(e):
    return render_template("index.html")
    
if __name__ == '__main__':
  app.run(debug=True)