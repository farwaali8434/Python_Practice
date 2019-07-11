import datetime
import glob
import pandas as pd


class WeatherReading:
    
    def __init__(self, row):
        self.date = row[0]
        self.highest_temp = row[1]
        self.lowest_temp = row[2]
        self.max_humidity = row[3]
        self.mean_humidity = row[4]
        
     
class ReadingStorage:
    row_reading = []
    def __init__(self, year, month='*'):
        files = glob.glob(f'files/Murree_weather_{year}_{month}.txt')
        for file in files:
            data_frame = pd.read_csv(f'{file}', sep=",", header=0)
            for row in data_frame[
                ['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity']].itertuples(
                    index=False):
                self.row_reading.append(WeatherReading(row))
    


class ReadingCalculator:
    
    def calculating_max(self, list):
        return max(list)
    