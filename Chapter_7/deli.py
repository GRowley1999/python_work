# Starts with a list of sandwich orders
# and an empty list to hold completed sandwich orders.
sandwich_orders = ['ham', 'cheese', 'chicken', 'ham and pickle']
finished_sandwiches = []

# Move each sandwich order to the list of finished sandwiches and
# print a message infomeing the user that their sandwich has been made.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I have made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())