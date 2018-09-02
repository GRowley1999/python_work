pizzas = ['margherita', 'pepperoni', 'vegetarian']
friend_pizzas = pizzas[:]

pizzas.append('meat feast')
friend_pizzas.append('hawaiian')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())