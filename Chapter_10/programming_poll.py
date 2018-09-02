prompt = "\nWhy do you like programming? "
prompt += "\n(Press q to quit). "

while True:
    reason = input(prompt)

    if reason == 'q':
        break
    else:
        with open('programming_poll.txt', 'a') as file_object:
            file_object.write(reason + "\n")