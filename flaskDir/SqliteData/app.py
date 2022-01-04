#   flask Skeleton
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.
    python flaskDir/SqliteData/app.py
"""

from flask import Flask,render_template
from db import DataBase

app = Flask(__name__)

@app.route('/')
@app.route('/<number>')
def load_show_last_10(number=10):
    db = DataBase()
    history = db.get_last(number)   
    print(f"{number}")
    return render_template('load-history.html',history=history)


def main():
    """Program Call Hub""" 
    app.run(port=5001)


if __name__ == "__main__":
    main()