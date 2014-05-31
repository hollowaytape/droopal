from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template

import os
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
os.path.join(PROJECT_DIR, 'droop.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///droop.db'

class Tree(db.Model):
    __tablename__ = 'droop_tree'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    threshold = db.Column(db.Integer)
    ripeness = db.Column(db.Boolean)
    latitude = db.Column(db.Float(6))
    longitude = db.Column(db.Float(6))
    
class Reading(db.Model):
    __tablename__ = "droop_reading"
    id = db.Column(db.Integer, primary_key = True)
    tree_id = db.Column(db.ForeignKey("Tree.id"), nullable=False)
    date_time = db.Column(db.String)
    value = db.Column(db.Integer)
    
@app.route('/trees/', methods=['GET'])
def trees():
    if request.method == 'GET':
        results = Tree.query.limit(50).offset(0).all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                'name': result.name,
                'type': result.type,
                'threshold': result.threshold,
                'ripeness': result.ripeness,
                'latitude': result.latitude,
                'longitude': result.longitude}
            json_results.append(d)

        return jsonify(items=json_results)
    """if request.method == 'PUT':
        results """
    
    
@app.route('/trees/<int:id>/', methods=['GET'])
def tree(id):
    if request.method == 'GET':
        result = Tree.query.filter_by(id=id).first()
        when_ripe = Reading.query.filter_by(tree_id=id, value=result.threshold).first()
        
        json_results = []
        t = {'id': result.id,
           'name': result.name,
           'type': result.type,
           'threshold': result.threshold,
           'ripeness': result.ripeness,
           'latitude': result.latitude,
           'longitude': result.longitude}
           
        r = {'tree_id': when_ripe.id,
             'date_time': str(when_ripe.date_time),
             'value': when_ripe.value}
        
        json_results.append(t)
        json_results.append(r)
            
        return jsonify(items=json_results)
        
@app.route('/trees/<int:id>/log', methods=['GET'])
def log(id):
    if request.method == 'GET':
        result = Tree.query.filter_by(id=id).first()
        readings = Reading.query.filter_by(tree_id=id).limit(100)
        
        json_results = []
        t = {'id': result.id,
           'name': result.name,
           'type': result.type,
           'threshold': result.threshold,
           'ripeness': result.ripeness,
           'latitude': result.latitude,
           'longitude': result.longitude}
        json_results.append(t)
        
        for reading in readings:
            r = {'tree_id': reading.id,
             'date_time': str(reading.date_time),
             'value': reading.value}
            json_results.append(r)
            
        return jsonify(items=json_results)
   
@app.errorhandler(404)
def page_not_found_better_show_the_index(e):
    return render_template("index.html")
    return "404"
    
if __name__ == '__main__':
  app.run(debug=True)