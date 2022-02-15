import unittest
import re

"""
Sum of Negative Integers

Create a function that takes a string containing integers as well as other
characters and return the sum of the negative integers only.

Examples
negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23

negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33

Notes
There is at least one negative integer.
"""


def negative_sum(chars):
    chars = re.findall(r"(-[0-9]*)", chars)
    return sum(int(x) for x in chars)


class SumOfNegativeIntegers(unittest.TestCase):
    def test_negative_sum(self):
        self.assertEqual(negative_sum("-12 13%14&-11"), -23)
        self.assertEqual(negative_sum("-12 13%14&-2 0 12 -4"), -18)
        self.assertEqual(negative_sum("33%14&-1 12 a 21 -2 b c"), -3)
        self.assertEqual(negative_sum("22 13%14&-11-22 13 12"), -33)
        self.assertEqual(negative_sum("-12 -8"), -20)


if __name__ == '__main__':
    unittest.main()
