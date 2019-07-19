import argparse
import reading_files
import utills

if '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='file selected with year and months')
    parser.add_argument('-e', help='files selected  with year only')
    parser.add_argument('-c', help='visual reporting of monthly weather')
    args = parser.parse_args()
    if args.e:
        stored_readings = utills.ReadingStorage(year=args.e)
        report = utills.Reporter(stored_readings)
        report.yearly_report()
    if args.a:
        year, month = reading_files.converting_date(args.a)
        stored_readings = utills.ReadingStorage(year=year, month=month)
        report = utills.Reporter(stored_readings)
        report.monthly_report()
    if args.c:
        year, month = reading_files.converting_date(args.c)
        stored_readings = utills.ReadingStorage(year=year, month=month)
        report = utills.Reporter(stored_readings)
        report.monthly_separate_barcharts()
        report.monthly_collected_barcharts()
