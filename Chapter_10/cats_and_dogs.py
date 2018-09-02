filenames = ["D:/Users/growl/Gregor Rowley/Programming/Python/python_work/" +
        "Chapter_10/text_files/cats.txt",
        "D:/Users/growl/Gregor Rowley/Programming/Python/python_work/" +
        "Chapter_10/dogs.txt"]

for filename in filenames:
    try:
        print("\nReading in file: " + filename)
        with open(filename) as f_obj:
            content = f_obj.read()
            print(content)
    except FileNotFoundError:
        pass
    