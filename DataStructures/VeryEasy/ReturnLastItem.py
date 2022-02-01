import unittest

"""
Create a function that returns the last value of
the last item in a list or string.

Examples
last_ind([0, 4, 19, 34, 50, -9, 2]) ➞ 2

last_ind("The quick brown fox jumped over the lazy dog") ➞ "g"

last_ind([]) ➞ None

Notes
Lists/strings will be of varying size.
Return None if list/string is empty.
"""


def last_ind(lst):
    return lst[-1] if lst else None


class ReturnLastItem(unittest.TestCase):
    def test_last_ind(self):
        self.assertEqual(last_ind([0, 4, 19, 34, 50, -9, 2]), 2)
        self.assertEqual(
            last_ind(["Hello", "There", "Python", "User"]), "User")
        self.assertEqual(last_ind([]), None)
        self.assertEqual(last_ind([True, False, False, True]), True)
        self.assertEqual(last_ind(
            [(5, 0), (0, 5, 6, 7), (3, 5, 67, 7), (0, -9, 3, 45, 5)]), (0, -9, 3, 45, 5))
        self.assertEqual(
            last_ind("Python is a great programming langauge."), ".")
        self.assertEqual(last_ind(["H", "E", "L", "L", "O"]), "O")
        self.assertEqual(
            last_ind("The quick brown fox jumped over the lazy dog"), "g")
        self.assertEqual(last_ind([{"name": "batman"}, {"kids": "none"}, {
                         "parents": "also none"}]), {"parents": "also none"})
        self.assertEqual(last_ind(""), None)


if __name__ == '__main__':
    unittest.main()
