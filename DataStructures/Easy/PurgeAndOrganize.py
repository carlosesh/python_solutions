import unittest

"""
Purge and Organize

Given a list of numbers, write a function that returns a list that...

Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]

unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]

unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
"""

def unique_sort(lst):
    return sorted(set(lst))


class PurgeAndOrganize(unittest.TestCase):
    def test_unique_sort(self):
        self.assertEqual(
          unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]),
          [1, 2, 3, 4, 5, 8, 10]
        )
        self.assertEqual(
        	unique_sort([1, 2, 5, 4, 7, 7, 7]),
          [1, 2, 4, 5, 7]
        )
        self.assertEqual(
        	unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]),
          [0, 1, 2, 3, 4, 5, 6, 7]
        )
        self.assertEqual(
        	unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]),
          [1, 3, 4, 5, 6, 27, 100]
        )
        self.assertEqual(
        	unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]),
          [-87, -9, -4.323827, -3.1415, -3.1414, 8]
        )


if __name__ == '__main__':
    unittest.main()
