import glob
from csv import DictReader
from datetime import datetime
from colorama import Fore
from calculations import max_temperature, max_humidity, min_temperature
from calculations import min_avg_temp, max_avg_temp, mean_avg_humidity


class WeatherReading:
    
    def __init__(self, row):
        self.date = datetime.strptime(row.get('PKT') or row.get('PKST'), '%Y-%m-%d').date()
        self.highest_temp = int(row['Max TemperatureC']) if row['Max TemperatureC'] else None
        self.lowest_temp = int(row['Min TemperatureC']) if row['Min TemperatureC'] else None
        self.max_humidity = int(row['Max Humidity']) if row['Max Humidity'] else None
        self.mean_humidity = int(row[' Mean Humidity']) if row[' Mean Humidity'] else None
        self.mean_temperature = int(row['Mean TemperatureC']) if row['Mean TemperatureC'] else None
        
     
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
        
        print(f"Highest: {max_temperature(self.weather_storage).highest_temp}C on "
              f"{max_temperature(self.weather_storage).date.strftime('%B')} "
              f"{max_temperature(self.weather_storage).date.day}\n"
              f"Lowest: {min_temperature(self.weather_storage).lowest_temp}C on "
              f"{min_temperature(self.weather_storage).date.strftime('%B')} "
              f"{min_temperature(self.weather_storage).date.day}\n"
              f"Humidity: {max_humidity(self.weather_storage).max_humidity}% on "
              f"{max_humidity(self.weather_storage).date.strftime('%B')} "
              f"{max_humidity(self.weather_storage).date.day}")
    
    def monthly_report(self):
    
        print(f"Highest Average: {max_avg_temp(self.weather_storage)}C\n"
              f"Lowest Average: {min_avg_temp(self.weather_storage)}C\n"
              f"Average Mean Humidity: {mean_avg_humidity(self.weather_storage)}%")
        
    def monthly_separate_barcharts(self):
        
        date = self.weather_storage.row_reading[0].date
        print(f"{date.strftime('%B')}  {date.year}")
        for weather_reading in self.weather_storage.row_reading:

            print(f'{weather_reading.date.day} {Fore.RED}', end='')
            for num in range(weather_reading.highest_temp or 0):
                print('+',  end='')
            
            print(f'{Fore.RESET}{weather_reading.highest_temp}C')
            print(f'{weather_reading.date.day} {Fore.BLUE}', end='')
            for num in range(weather_reading.lowest_temp or 0):
                print('+',  end='')
            print(f'{Fore.RESET} {weather_reading.lowest_temp}C')
        
    def monthly_collected_barcharts(self):
        date = self.weather_storage.row_reading[0].date
        print(f'{date.strftime("%B")}  {date.year}')
        for weather_reading in self.weather_storage.row_reading:
            print(f"{weather_reading.date.day} {Fore.BLUE}", end='')
            for h in range(weather_reading.lowest_temp or 0):
                print('+', end='')
            for l in range(weather_reading.highest_temp or 0):
                print(Fore.RED + '+', end='')
            print(f' {Fore.RESET}{weather_reading.lowest_temp}C - {weather_reading.highest_temp}C')
