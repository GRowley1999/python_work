filepath = 'D:/Users/growl/Gregor Rowley/Programming/Python/python_work/Chapter_10/text_files/pi_million_digits.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string: 
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birtday does not appear in the first million digits of pi.")