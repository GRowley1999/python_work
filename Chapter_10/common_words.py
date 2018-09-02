filenames = ["D:/Users/growl/Gregor Rowley/Programming/Python/python_work/" +
        "Chapter_10/text_files/alice.txt",
        "D:/Users/growl/Gregor Rowley/Programming/Python/python_work/" +
        "Chapter_10/text_files/little_women.txt",
        "D:/Users/growl/Gregor Rowley/Programming/Python/python_work/" +
        "Chapter_10/text_files/moby_dick.txt"]

for filename in filenames:
    print("Reading in file: " + filename)
    with open(filename) as f_obj:
        content = f_obj.read()
        print("The word 'the' appears: " + str(content.lower().count("the")) +
            " times in " +  filename)