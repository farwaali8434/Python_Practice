import datetime


class WeatherReading:
    
    def __init__(self, row):
        self.date = row[0]
        self.highest_temp = row[1]
        self.lowest_temp = row[3]
        # self.max_humidity = row[7]
        
        # self.highest_average_temp = int
        # self.lowest_average_temp = int
        # self.average_mean_humidity = int
        

class ReadingStorage:
    
    pass