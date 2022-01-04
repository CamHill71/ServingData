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
def load_show_last_10():
    db = DataBase()
    history = db.get_last(10)   
    return render_template('load-history.html',history=history,length = len(history))


def main():
    """Program Call Hub""" 
    app.run(port=5001)


if __name__ == "__main__":
    main()