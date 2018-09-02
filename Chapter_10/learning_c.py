filepath = 'D:/Users/growl/Gregor Rowley/Programming/Python/python_work/Chapter_10/text_files/learning_python.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()
 
for line in lines:
    print(line.replace('python', 'C'))