import csv

filename = ('D:/Users/growl/Gregor Rowley/Programming/Python/python_work/' +
    'Chapter_16/sitka_weather_07-2014.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)