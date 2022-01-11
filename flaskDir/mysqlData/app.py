#   name of program
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.
"""

from flask import Flask
from flask import render_template
from datetime import time
from db import DataBase

app = Flask(__name__)

connection_uri = ("mysql+pymysql://root:Chilly1971*@localhost/grails1")

@app.route("/")
@app.route("/<qty>")
def Chart(qty=90):
    data = DataBase(connection_uri)
    holdings = data.get_holdings()
    print(f"{holdings}")
    percentage_data,money_data = data.holdings_last_days(qty)
    return render_template("chart.html",percentage_data=percentage_data,money_data=money_data,holdings=holdings)


def main():
    """Program Call Hub""" 
    app.run(port=5000,debug=True)


if __name__ == "__main__":
    main()