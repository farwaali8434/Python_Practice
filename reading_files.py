import datetime
import utills
import argparse


def converting_date(filename):

    given = filename.split('/')
    month_name = datetime.datetime(year=int(given[0]),month=int(given[1]),day = 1)
    return month_name.year, month_name.strftime('%b')

    
def parsing_files_with_months():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='file selected with year and months')
    args = parser.parse_args()
    year, month = converting_date(args.a)
    utills.ReadingStorage(year=year, month=month)
    
    
def parsing_files_with_year():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='files selected  with year only')
    args = parser.parse_args()
    utills.ReadingStorage(year=args.e)
    
    
