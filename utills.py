import glob
from csv import DictReader


class WeatherReading:
    
    def __init__(self, row):
        self.date = row['PKT']
        self.highest_temp = row['Max TemperatureC']
        self.lowest_temp = row['Min TemperatureC']
        self.max_humidity = row['Max Humidity']
        self.mean_humidity = row[' Mean Humidity']
        
     
class ReadingStorage:
    row_reading = []
    
    def __init__(self, year=2004, month='Aug'):
        files = glob.glob(f'files/Murree_weather_{year}_{month}.txt')
        for file in files:
            data_frame = DictReader(open(file))
            for row in data_frame:
                self.row_reading.append(WeatherReading(row))
                
    def calculations(row_reading):
        maxx = max(row_reading[WeatherReading().highest_temp])
        print(maxx)
    
        
class Reporter:
    def __init__(self):
        pass

    def reporter_with_month(self):
        print(f"Highest: {45}C on {'June'} {23}\n"
              f"Lowest: {1}C on {'December'} {22}\n"
              f"Humidity: {95}% on {'August'} {14}")
    
    def reporter_with_years(self):
        print(f"""Highest Average: {39}C
                  Lowest Average: {18}C
                  Average Mean Humidity: {71}%""")
