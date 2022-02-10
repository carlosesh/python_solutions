import unittest

"""
Two Product Problem (Part 2)

Create a function that takes a list lst and a number n and returns a list of two
integers whose product is that of the number n.

Examples
two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]

two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]

two_product([100, 12, 4, 1, 2], 15) ➞ None
Notes
No duplicates.
Sort the number.
Try doing this with 0(n) time complexity.
The list can have multiple solutions, so return the first match you find.
"""


def two_product(lst, n):
    num_list = []
    for num in lst:
        complement = n // num
        if complement * num == n and complement in num_list:
            return [num, complement] if num < complement else [complement, num]
        else:
            num_list.append(num)

    return None


class TwoProductProblemPart2(unittest.TestCase):

    def test_two_product(self):
        self.assertEqual(two_product([100, 12, 4, 1, 2], 15), None)
        self.assertEqual(two_product([11, 2, 7, 3, 5, 0], 55), [5, 11])
        self.assertEqual(two_product([1, 2, 3, 4, 13, 5], 39), [3, 13])
        self.assertEqual(two_product([1, 2, -1, 4, 5], 20), [4, 5])
        self.assertEqual(two_product([1, 2, 3, 4, 5], 10), [2, 5])


if __name__ == '__main__':
    unittest.main()
