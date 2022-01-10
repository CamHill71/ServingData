#   name of program
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.

"""

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from stockDates import StockDates
import itertools
import csv
import datetime

from sqlalchemy.sql.expression import text

connection_uri = ("mysql+pymysql://root:Chilly1971*@localhost/djangodb")
Base = declarative_base()
table_name = ''


class DataBase:
    def __init__(self,engine) -> None:
        self.engine = create_engine(engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.dates = StockDates()
        self.holdings = {}
        self.chartData_raw = {}
        self.percentage_results = {}
        
    def __str__(self) -> str:
        pass
       

    def get_last(self,quantity):
        query = self.session.query(Books).all()        
        return [ letter for letter in query ] 
    
    def get_holdings(self):
        with open('myFlask/ServingData/flaskDir/mysqlData/Holdings_9010242_09-01-2022.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row[0].strip()) == 3:                    
                    if float(row[2]) != 0.0:
                        self.holdings[row[0]] = (row[1],row[2])   
                        
                        
    def holdings_last_days(self,qty):
        """ Get combined stock 90 day data, output a percentage"""
        engine = create_engine("mysql+pymysql://root:Chilly1971*@localhost/grails1")     
        with engine.connect() as conn:
            for stock in self.holdings.keys():
                result = conn.execute(text(f"SELECT `EntryDate`,`Close` FROM grails1.asx_{stock} where `EntryDate` >= date_add(date(now()),interval -{qty} day)"))   
                self.chartData_raw[stock] = result.all()
            
            active_days = self.dates.getStockDates(float(qty))
            eod_price = 1
            stock_date = 0
            for day in active_days[1:len(active_days)-1]:
                eod_list = []                
                for stock in self.chartData_raw.keys():                    
                    stock_list = self.chartData_raw[stock]
                    count = 0
                    if (day in itertools.chain(*stock_list)):
                        for date in stock_list:
                            if day == date[stock_date]:
                                previousDay = stock_list[count-1][eod_price]
                                currentDay = date[eod_price]
                                percent = ((previousDay - currentDay) / currentDay) * 100
                                eod_list.append(percent)
                            count += 1
                                           
                self.percentage_results[str(day)] = round(sum(eod_list)) 
            print(f"{len(self.percentage_results)}")
            return  [ str(item) for item in self.percentage_results.items()]              

                                        
                     

class Books(Base):
    __tablename__ = "books_book"
    
    id = Column(Integer(),primary_key=True, autoincrement=True)   
    title = Column(String()) 
    
    def __str__(self) -> str:
        return super().__str__()

def main():
    """Program Call Hub""" 
    mydata = DataBase(connection_uri)
    mydata.get_holdings()
    #query = mydata.get_last(10)
    query2 = mydata.holdings_last_days()
    #print(f"{query[0].id}")






if __name__ == "__main__":
    main()