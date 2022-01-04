#   flask Skeleton
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.

"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello , World<h1>'


def main():
    """Program Call Hub""" 
    app.run()


if __name__ == "__main__":
    main()