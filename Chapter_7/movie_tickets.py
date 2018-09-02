prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            ticket_cost = 0
        elif age > 3 and age < 12:
            ticket_cost = 10
        elif age > 12:
            ticket_cost = 15

        if ticket_cost == 0:
            print("Your ticket is free.")
        else:
            print("Your ticket is $" + str(ticket_cost) + ".")
