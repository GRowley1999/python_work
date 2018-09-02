prompt = "\nPlease enter a pizza topping:"
prompt += "\n(Enter 'quit' when you are finished.) "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(topping.title() + " will be added to your pizza.")