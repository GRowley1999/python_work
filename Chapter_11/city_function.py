def get_formatted_city_country(city, country, population=''):
    """Returns a formatted city and country."""
    if population:
        formatted_place_name = city + ', ' + country + ' - population ' + population
    else:
        formatted_place_name = city + ', ' + country
    return formatted_place_name.title()
    