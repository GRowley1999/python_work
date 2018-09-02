cities = {
    'glasgow' : {
        'country' : 'scotland',
        'population' : 5.988e5,
        'fact' : "It is Scotland's largest city.",
    },
    'london' : {
        'country' : 'england',
        'population' : 8.136e6,
        'fact' : 'There are more people in London than in all of Scotland.'
    }
}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("Population: " + str(city_info['population']))
    print("Fact: " + city_info['fact'])