import unittest
from city_function import get_formatted_city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py'"""
    
    def test_city_country(self):
        """Do cities and countries like 'Santiago, Chile' work?"""
        formatted_city_country = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    
    def test_city_country_population(self):
        """
        Do cities and countries and populations like 'Santiago, Chile - 
        population 500000' work?
        """
        formatted_city_country = get_formatted_city_country(
            'Santiago', 'Chile', '500000')
        self.assertEqual(formatted_city_country, 'Santiago, Chile - Population' + 
            ' 500000')

unittest.main()