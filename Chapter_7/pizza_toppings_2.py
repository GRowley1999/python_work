prompt = "\nPlease enter a pizza topping:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(topping.title() + " will be added to your pizza.")