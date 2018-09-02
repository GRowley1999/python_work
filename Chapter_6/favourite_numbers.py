favourite_numbers = {
    'Patrick' : [1, 2],
    'Fiona' : [2, 3],
    'Gregor' : [3, 4],
    'Erin' : [4, 5],
    'Freya' : [5, 6],
}

for person, numbers in favourite_numbers.items():
    print("\n" + person.title() + "'s favourite numbers are:")
    for number in numbers:
        print("\t" + str(number))