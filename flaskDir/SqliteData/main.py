#   flask Skeleton
#
# © 2021 Cameron Hill Programmer

"""
    Program: File.py Author: Cameron Hill.

"""
from db import input_data
import requests
from time import sleep
from datetime import datetime

def get_weather_data(city):    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=cf6fce591432e1a6d1742bd90432ea70'     
    r = requests.get(url).json()
    return r

def main():
    """Program Call Hub""" 
    delay = 600
    while True:
        r = get_weather_data('perth')
        weather = {
        'city' : 'Perth',
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],        
        }
        
        input_data(weather['temperature'],datetime.now())
        print(f"{datetime.now()}")
        sleep(delay)
        



if __name__ == "__main__":
    main()