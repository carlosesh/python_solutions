import unittest
"""
Create a function that takes a country's name and its area as
arguments and returns the area of the country's proportion of
the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞
"Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610),
"USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195) ➞
"Iran is 1.11% of the total world's landmass"

Notes
The total world's landmass is 148,940,000 [Km^2]
Round the result to two decimal places.
If you get stuck on a challenge, find help in the Resources tab.
"""

def area_of_country(name, area):
    world_landmass =  148940000
    country_land_mass = round((area * 100) / world_landmass, 2)
    return f"{name} is {country_land_mass}% of the total world's landmass"


class GetTheAreaOfACountry(unittest.TestCase):
    def test_area_of_country(self):
        self.assertEqual(area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass")
        self.assertEqual(area_of_country("Russia", 17098242), "Russia is 11.48% of the total world's landmass")
        self.assertEqual(area_of_country("Iran", 1648195), "Iran is 1.11% of the total world's landmass")
        self.assertEqual(area_of_country("India", 3287590), "India is 2.21% of the total world's landmass")
        self.assertEqual(area_of_country("China", 9706961), "China is 6.52% of the total world's landmass")
        self.assertEqual(area_of_country("Yemen", 527968), "Yemen is 0.35% of the total world's landmass")
        self.assertEqual(area_of_country("Switzerland", 41284), "Switzerland is 0.03% of the total world's landmass")


if __name__ == '__main__':
    unittest.main()
