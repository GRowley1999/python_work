import json

filename = 'fav_number.json'

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    favourite_number = input("\nEnter your favourite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(favourite_number, f_obj)
else:
    print("I know your favourite number! It's " + fav_number + ".")