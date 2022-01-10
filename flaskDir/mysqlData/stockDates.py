#   name of program
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.
"""

from networkdays import networkdays
from datetime import datetime,timedelta,date


class StockDates():
    def __init__(self) -> None:
        self.date_now = datetime.now()
        self.holidays = [date(2021,1,1),date(2021,1,26),date(2021,4,2),date(2021,4,5),date(2021,4,25),date(2021,6,14),date(2021,12,27),date(2021,12,28),
                         date(2022,1,3),date(2022,1,26),date(2022,4,15),date(2022,4,18),date(2022,4,25),date(2022,6,13),date(2022,12,26),date(2022,12,27)]

    def getStockDates(self,days=90):
        """ List X amount of days minus trading day holidays"""
        no_of_days = timedelta(days)        
        before_x_days = self.date_now - no_of_days 
        days = networkdays.Networkdays(datetime.date(before_x_days),datetime.date(self.date_now),self.holidays)
        return days.networkdays()
       
                


def main():
    """Program Call Hub""" 
    dates = StockDates()
    dates.getStockDates()


if __name__ == "__main__":
    main()