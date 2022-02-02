import unittest

"""
The List Twins

Create a function that given a list, it returns the index where if split in two-subarrays (last element of the first array has index of (foundIndex-1)), the sum of them are equal.

Examples
twins([10, 20, 30, 5, 40, 50, 40, 15]) ➞ 5
# foundIndex 5 : [10+20+30+5+40]=[50+40+15]

twins([1, 2, 3, 4, 5, 5]) ➞ 4
# [1, 2, 3, 4] [5, 5]

twins([3, 3]) ➞ 1

Notes
Return only the foundIndex, not the divided list.
"""
def twins(lst):


class TheListTwins(unittest.TestCase):
    def test_twins(self):
        Test.assert_equals(twins([1, 2, 3, 4, 5, 5]), 4)
        Test.assert_equals(twins([3, 3]), 1)
        Test.assert_equals(twins([10, 20, 30, 5, 40, 50, 40, 15]), 5)
        Test.assert_equals(twins([3, 4, 6, 7, 6]), 3)


if __name__ == '__main__':
    unittest.main()
