import unittest

"""
Penultimate

Description:
Find the second-to-last element of a list.

Example:

penultimate([1,2,3,4])            # => 3
penultimate(["Python is dynamic"]) # => 'i'
"""


def penultimate(a):
    return a[-2]


class Penultimate(unittest.TestCase):
    def test_penultimate(self):
        self.assertEqual(penultimate([1, 2, 3, 4]), 3)
        self.assertEqual(penultimate("hello"), 'l')


if __name__ == '__main__':
    unittest.main()
