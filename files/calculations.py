from utills import ReadingStorage, Reporter, WeatherReading

g = ReadingStorage()
r = Reporter(g)
f = Reporter.yearly_report(r)
h = WeatherReading()

highest_temp_wr = max(f.row_readings, key=lambda x: h.highest_temp)
print(highest_temp_wr)
# lowest_temp_wr = min(self.weather_storage.row_readings, key=lambda x: x.lowest_temp)
# highest_humidity_wr = max(self.weather_storage.row_readings, key=lambda x: x.max_humidity)