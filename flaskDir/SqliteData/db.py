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



engine = create_engine('sqlite:///mydb.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Weather(Base):
    __tablename__ = "temperature"
    
    id = Column(Integer(),primary_key=True,autoincrement=True)
    temperature = Column(Numeric(3,2),nullable=False)
    taken_at = Column(DateTime,default=datetime.now)
    
    def __str__(self) -> str:
        return super().__str__()
    

def input_data(temp,time_now):
    Base.metadata.create_all(engine)    
    temperature = Weather(temperature=temp,taken_at=time_now)
    session.add(temperature)
    session.commit()
    
    query = session.query(Weather.temperature,Weather.taken_at).all() 
    for item in query:
        print(f" {item[0]}  {item[1]} ")
     
    

def main():
    """Program Call Hub"""
    temp = 31 
    time_now = datetime.now()
    input_data(temp,time_now)

            


if __name__ == "__main__":
    main()