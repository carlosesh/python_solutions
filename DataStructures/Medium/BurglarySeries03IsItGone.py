import unittest

"""
Burglary Series (03): Is It Gone?
Your spouse is not concerned with the loss of material possessions but rather
with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lower cases representing
the name of the pet (e.g. "rambo"), return:

"Rambo is gone..." if the name is on the list.
"Rambo is here!" if the name is not on the list.

Note that the first letter of the name in the return statement is capitalized.

Examples
 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.


 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.


items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary.
"""


def find_it(items, name):
    name_title = name.title()
    if not items:
        return f"{name_title} is here!"
    return f"{name_title} is gone..." if name in items.keys() else f"{name_title} is here!"


class BurglarySeries03IsItGone(unittest.TestCase):
    def test_find_it(self):
        self.assertEqual(find_it({}, "rambo"), "Rambo is here!")
        self.assertEqual(find_it({}, "heman"), "Heman is here!")

        self.assertEqual(find_it({
            "tv": 30,
            "stereo": 50,
        }, "rocky"), "Rocky is here!")

        self.assertEqual(find_it({
            "tv": 30,
            "stereo": 50,
        }, "spiderman"), "Spiderman is here!")

        self.assertEqual(find_it({
            "tv": 30,
            "stereo": 50,
            "julius": 100,
        }, "julius"), "Julius is gone...")

        self.assertEqual(find_it({
            "tv": 30,
            "stereo": 50,
            "batman": 200,
        }, "batman"), "Batman is gone...")

        self.assertEqual(find_it({}, "batman"), "Batman is here!")


if __name__ == '__main__':
    unittest.main()
