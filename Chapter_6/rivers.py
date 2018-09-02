rivers = {
    'nile' : 'egypt',
    'thames' : 'england',
    'clyde' : 'scotland',
}

for river in rivers.keys():
    print("The " + river.title() + " runs through " + rivers[river].title() + ".")

for river in rivers:
    print("\n" + river)

for country in rivers.values():
    print("\n" + country)