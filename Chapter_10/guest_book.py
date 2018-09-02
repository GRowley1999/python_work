prompt = "\nPlease enter your name:"
prompt += "\n(Press q to quit)."

while True:
    name = input(prompt)

    if name == 'q':
        break
    else:
        print("Hello " + name.title())
        with open("guest_book.txt", 'a') as file_object:
            file_object.write(name.title())
