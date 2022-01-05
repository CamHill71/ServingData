#   flask Skeleton
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.
    python flaskDir/SqliteData/app.py
"""

from flask import Flask,render_template,jsonify,json
from db import DataBase
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})

@app.route('/')
@app.route('/<number>')
def load_show_last_10(number=10):
    db = DataBase()
    history = db.get_last(number)   
    print(f"{number}")
    return render_template('load-history.html',history=history)

@app.route('/api/J')
@app.route('/api/J/<number>')
def load_show_last(number=10):
    db = DataBase()
    history = db.get_last(number)   
    print(f"{number}")
    sample_data = {
        0: {
            'created_at': '2020-01-01 00:00:01',
            'load': '62.5'
        },
        1: {
            'created_at': '2020-01-01 00:00:06',
            'load': '56.2'
        },
        2: {
            'created_at': '2020-01-01 00:00:11',
            'load': '34.9'
        },
        3: {
            'created_at': '2020-01-01 00:00:16',
            'load': '24.6'
        },
        4: {
            'created_at': '2020-01-01 00:00:21',
            'load': '3.1'
        },
        5: {
            'created_at': '2020-01-01 00:00:26',
            'load': '4.9'
        }
    }    
    items_required = dict(list(sample_data.items())[0:1])
    jsonData = json.dumps(items_required)    
    return render_template('json.html',jsonData = jsonData) # jsonify(sample_data)


@app.route('/api/static-chart')
def static_chart():
    return "<h1> hello World<h1>"  #render_template('static-chart.html')




def main():
    """Program Call Hub""" 
    app.run(port=5001)


if __name__ == "__main__":
    main()