#   flask Skeleton
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.

"""

from sqlalchemy import create_engine, Column,Integer,Numeric,DateTime
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql.expression import desc
import os

# Keep db in working directory
dir_name = (__file__.replace('/'+ os.path.basename(__file__),''))
SQLALCHEMY_DATABASE_URI = f"sqlite:////{dir_name}/mydb.db"

Base = declarative_base()

class DataBase:
    
    def __init__(self) -> None:
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()       
    
    
    def get_last(self,limit):
        query = self.session.query(Weather.id,  Weather.taken_at,Weather.temperature).order_by(desc(Weather.id)).limit(10)
        return [ letter for letter in query ]    

    def input_data(self,temp,time_now):
        """ Initialise db and store new data"""
        Base.metadata.create_all(self.engine)           
        temperature = Weather(temperature=temp,taken_at=time_now)
        self.session.add(temperature)
        self.session.commit()
        
        query = self.session.query(Weather.temperature,Weather.taken_at).all() 
        for item in query:
            print(f" {item[0]}  {item[1]} ")
         

class Weather(Base):
    __tablename__ = "temperature"
    
    id = Column(Integer(),primary_key=True,autoincrement=True)
    temperature = Column(Numeric(3,2),nullable=False)
    taken_at = Column(DateTime,default=datetime.now)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return "Weather(id={self.id},temperature={self.temperature},"\
            "taken_at={self.taken_at})".format(self=self)
 

def main():
    """Program Call Hub"""
    temp = 31 
    time_now = datetime.now()
    db = DataBase()    
    db.input_data(temp,time_now)

            


if __name__ == "__main__":
    main()