import glob
from csv import DictReader
from statistics import mean
from datetime import datetime
from colorama import Fore


class WeatherReading:
    
    def __init__(self, row):
        self.date = datetime.strptime(row.get('PKT') or row.get('PKST'), '%Y-%m-%d').date()
        self.highest_temp = int(row['Max TemperatureC']) if row['Max TemperatureC'] else None
        self.lowest_temp = int(row['Min TemperatureC']) if row['Min TemperatureC'] else None
        self.max_humidity = int(row['Max Humidity']) if row['Max Humidity'] else None
        self.mean_humidity = int(row[' Mean Humidity']) if row[' Mean Humidity'] else None
        self.mean_temperature =int(row['Mean TemperatureC']) if row['Mean TemperatureC'] else None
        
     
class ReadingStorage:
    
    def __init__(self, year=2004, month='*'):
        self.row_reading = []
        for file in glob.glob(f'files/Murree_weather_{year}_{month}.txt'):
            for row in DictReader(open(file)):
                self.row_reading.append(WeatherReading(row))

                
class Reporter:
    
    def __init__(self, reading_storage):
        self.weather_storage = reading_storage
    
    def yearly_report(self):
        highest = [value for value in self.weather_storage.row_reading if value.highest_temp is not None]
        
        highest_temp_wr = max(highest, key=lambda x: x.highest_temp)
        
        lowest = [value for value in self.weather_storage.row_reading if value.lowest_temp is not None]
        
        lowest_temp_wr = min(lowest,  key=lambda x: x.lowest_temp)
        
        highest_humidity = [value for value in self.weather_storage.row_reading if value.max_humidity is not None]
        
        highest_humidity_wr = max(highest_humidity, key=lambda x: x.max_humidity)
        
        print(f"Highest: {highest_temp_wr.highest_temp}C on {highest_temp_wr.date.strftime('%B')} {highest_temp_wr.date.day}\n"
        
              f"Lowest: {lowest_temp_wr.lowest_temp}C on {lowest_temp_wr.date.strftime('%B')} {lowest_temp_wr.date.day}\n"
        
              f"Humidity: {highest_temp_wr.max_humidity}% on {highest_humidity_wr.date.strftime('%B')} {highest_humidity_wr.date.day}")
    
    def monthly_report(self):
        
        hat = [v for v in self.weather_storage.row_reading if v.mean_temperature is not None]
        
        highest_avg_temp = max(hat, key=lambda x: x.mean_temperature)
        
        lat = [v for v in self.weather_storage.row_reading if v.mean_temperature is not None]
        
        lowest_avg_temp = min(lat, key=lambda x: x.mean_temperature)
        
        avg_humidity = [value for value in self.weather_storage.row_reading if value.mean_humidity is not None]
        
        avg_mean_humidity = mean([humidity.mean_humidity for humidity in avg_humidity])
    
        print(f"Highest Average: {highest_avg_temp.mean_temperature}C\n"
              f"Lowest Average: {lowest_avg_temp.mean_temperature}C\n"
              f"Average Mean Humidity: {avg_mean_humidity}%")
        
        
    def monthly_separate_barcharts(self):
        date = self.weather_storage.row_reading[0].date
        print(f"{date.strftime('%B')}  {date.year}")
        for weather_reading in  self.weather_storage.row_reading:

            print(f'{weather_reading.date.day} {Fore.RED}', end='')
            for num in range(weather_reading.highest_temp or 0):
                print( '+',  end='')
            
            print(f'{Fore.RESET}{weather_reading.highest_temp}C')
            print(f'{weather_reading.date.day} {Fore.BLUE}', end='')
            for num in range(weather_reading.lowest_temp or 0):
                print('+',  end='')
            print(f'{Fore.RESET} {weather_reading.lowest_temp}C')
        
    def monthly_collected_barcharts(self):
        date = self.weather_storage.row_reading[0].date
        print(f'{date.strftime("%B")}  {date.year}')
        for weather_reading in self.weather_storage.row_reading:
            print(f"{weather_reading.date.day} {Fore.BLUE}", end = '')
            for h in range(weather_reading.lowest_temp or 0):
                print('+', end='')
            for l in range(weather_reading.highest_temp or 0):
                print(Fore.RED + '+', end='')
            print(f' {Fore.RESET}{weather_reading.lowest_temp}C - {weather_reading.highest_temp}C')
            
            
        
        # range read
        # self.weather_storage.row_reading[14].highest_temp
        # self.weather_storage.row_reading[6].highest_temp
        #print(item, end=" ")
        # '.' (dot operator)| template: <object>.<field> to access a field of an object
        # '.' (dot operator)| template: <class>.<field> to accessa staic field of an class
        # '[str]' (subscript notation)| template: <dict>[<key>] to access a value against a specific key in dictionary/key-value pairs
        # '[int]' (subscript notation)| template: <python list/tuple/array/set>[int] to access a value in a specific index in tuple/python list/array/set