import json

print("What is your favourite number? ")

favourite_number = input("\nEnter your favourite number: ")

filename = 'fav_number.json'

with open(filename, 'w') as f_obj:
    json.dump(favourite_number, f_obj)
