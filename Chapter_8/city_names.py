def city_country(name, country):
    """Prints the name of a city and the country in which it is found."""
    return name.title() + ", " + country.title()

place = city_country("glasgow", "scotland")
print(place)

place = city_country("london", "england")
print(place)

place = city_country("new york", "USA")
print(place)