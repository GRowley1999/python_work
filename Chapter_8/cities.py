def describe_city(name, country="Scotland"):
    """Displays the name of an entered city and the country it's in."""
    print(name.title() + " is in " + country.title())

describe_city("Edinburgh")
describe_city("Glasgow")
describe_city("London", "England")