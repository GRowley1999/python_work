favourite_places = {
    'patrick' : ['glasgow', 'cumbria', 'london'],
    'fiona' : ['glasgow', 'paris', 'lanzarote'],
    'erin' : ['glasgow', 'london', 'amsterdam'],
}

for person, places in favourite_places.items():
    print("\nName: " + person.title())
    print("Favourite places:")
    for place in places:
        print(place.title()) 