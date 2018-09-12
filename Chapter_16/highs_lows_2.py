import csv

filename = ('D:/Users/growl/Gregor Rowley/Programming/Python/python_work/' +
    'Chapter_16/sitka_weather_07-2014.csv')

# Get high temperatures from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)