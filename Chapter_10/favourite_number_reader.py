import json

filename = 'fav_number.json'

with open(filename) as f_obj:
    fav_number = json.load(f_obj)
print("I know your favourite number! It's " + fav_number + ".")