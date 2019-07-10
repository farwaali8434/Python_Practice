import os, pandas as pd, glob, datetime,utills
import argparse
from collections import namedtuple

# files = os.scandir('files/')
# for file in files:
#     print(file)


def readfile(year, month='*'):
    row_reading = []
    files = glob.glob(f'files/Murree_weather_{year}_{month}.txt')
    for file in files:
        data_frame = pd.read_csv(f'{file}', sep=",", header=0)
        for row in data_frame[['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Max Humidity']].itertuples(index=True):
            reading = utills.WeatherReading(row)
            row_reading.append(reading)
        for one in row_reading:
            print(one)
        
        
def monthly_reading(filename):
    line_list = [line.rstrip('\n') for line in open(f'files/{filename}')]


def converting_date(filename):

    given = filename.split('/')
    month_num = given[1]
    year_num = given[0]
    month_name = datetime.datetime(year=int(year_num),month=int(month_num),day = 1)
    return month_name.year, month_name.strftime('%b')
    
    
def parsing_files_with_months():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='file selected with year and months')
    args = parser.parse_args()
    year, month = converting_date(args.a)
    readfile(year=year, month=month)
    
    
def parsing_files_with_year():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='files selected  with year only')
    args = parser.parse_args()
    readfile(year=args.e)
