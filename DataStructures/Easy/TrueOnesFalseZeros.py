import unittest

"""
True Ones, False Zeros

Create a function which returns a list of booleans,
from a given number. Iterating through the number
one digit at a time, append True if the digit is 1
and False if it is 0.

Examples
integer_boolean("100101") ➞ [True, False, False, True, False, True]

integer_boolean("10") ➞ [True, False]

integer_boolean("001") ➞ [False, False, True]

Notes
Expect numbers with 0 and 1 only.
"""

def integer_boolean(n):
        bool_list = []
        while n > 0:
            bool_list.append(bool(n % 10))
            n //= 10

        return bool_list[::-1]


class TrueOnesFalseZeros(unittest.TestCase):
    def test_integer_boolean(self):
        self.assertEqual(integer_boolean(100101), [True, False, False, True, False, True])
        self.assertEqual(integer_boolean(10), [True, False])
        self.assertEqual(integer_boolean(1), [True])
        self.assertEqual(integer_boolean(111), [True, True, True])
        self.assertEqual(integer_boolean(10010110), [True, False, False, True, False, True, True, False])


if __name__ == '__main__':
    unittest.main()
