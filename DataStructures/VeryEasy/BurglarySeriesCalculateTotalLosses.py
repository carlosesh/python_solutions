import unittest

"""
Burglary Series (01): Calculate Total Losses
You just returned home to find your mansion
has been robbed! Given a dictionary of the
stolen items, return the total amount of the
burglary (number). If nothing was robbed,
return the string "Lucky you!".

Examples
calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}) ➞ 100

calculate_losses({
  "painting" : 20000,
}) ➞ 20000

calculate_losses({}) ➞ "Lucky you!"

Notes
The item value is always positive.
"""


def calculate_losses(items):
    return sum(items.values()) if items else "Lucky you!"


class BurglarySeriesCalculateTotalLosses(unittest.TestCase):
    def test_calculate_losses(self):
        self.assertEqual(calculate_losses({
            "tv": 30,
            "skate": 20,
            "stereo": 50,
        }), 100)
        self.assertEqual(calculate_losses({
            "ring": 30000,
            "painting": 20000,
            "bust": 1,
        }), 50001)
        self.assertEqual(calculate_losses({
            "chair": 3500,
        }), 3500)
        self.assertEqual(calculate_losses({}), "Lucky you!")


if __name__ == '__main__':
    unittest.main()
