print("Enter two numbers to be added together.")
print("(Enter 'q' to quit).")

while True:
    first_number = input("\nEnter the first number: ")
    if first_number == 'q':
        break
    
    second_number = input("\nEnter the second number: ")
    if second_number == 'q':
        break
    
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("\nYou can't add text!")
    else:
        print("\nThe sum of " + first_number + " and " + second_number + " is: " + str(sum))