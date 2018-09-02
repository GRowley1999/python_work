filepath = 'D:/Users/growl/Gregor Rowley/Programming/Python/python_work/Chapter_10/text_files/pi_digits.txt'

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())