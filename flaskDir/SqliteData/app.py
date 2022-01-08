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
    return render_template('load-history.html',history=history)

@app.route('/a')
def load_show_last(): 
    return render_template('dynamic-chart.html') # jsonify(sample_data)


@app.route('/api/static-chart')
def static_chart():
    return "<h1> hello World<h1>"  #render_template('static-chart.html')




def main():
    """Program Call Hub""" 
    app.run(port=5002)


if __name__ == "__main__":
    main()