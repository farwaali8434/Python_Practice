from statistics import mean


def max_avg_temp(weather_storage):
    hat = [v for v in weather_storage.row_reading if v.mean_temperature is not None]
    highest_avg_temp = max(hat, key=lambda x: x.mean_temperature)
    return highest_avg_temp.highest_temp


def min_avg_temp(weather_storage):
    lat = [v for v in weather_storage.row_reading if v.mean_temperature is not None]
    lowest_avg_temp = min(lat, key=lambda x: x.mean_temperature)
    return lowest_avg_temp.lowest_temp
    
    
def mean_avg_humidity(weather_storage):
    avg_humidity = [value for value in weather_storage.row_reading if value.mean_humidity is not None]
    avg_mean_humidity = mean([humidity.mean_humidity for humidity in avg_humidity])
    return round(avg_mean_humidity, 2)


def max_temperature(weather_storage):
    highest = [value for value in weather_storage.row_reading if value.highest_temp is not None]
    highest_temp_wr = max(highest, key=lambda x: x.highest_temp)
    return highest_temp_wr


def min_temperature(weather_storage):
    lowest = [value for value in weather_storage.row_reading if value.lowest_temp is not None]
    lowest_temp_wr = min(lowest, key=lambda x: x.lowest_temp)
    return lowest_temp_wr


def max_humidity(weather_storage):
    highest_humidity = [value for value in weather_storage.row_reading if value.max_humidity is not None]
    highest_humidity_wr = max(highest_humidity, key=lambda x: x.max_humidity)
    return highest_humidity_wr








