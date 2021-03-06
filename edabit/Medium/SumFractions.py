import unittest

"""
Sum Fractions

Create a function that takes a list containing nested lists as an argument.
Each sublist has 2 elements. The first element is the numerator and the second
element is the denominator. Return the sum of the fractions rounded to the
nearest whole number.

Examples
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11

Notes
Your result should be a number not string.
"""


def sum_fractions(lst):
    sum = 0
    for numerator, denominator in lst:
        sum += numerator / denominator

    return round(sum)


def sum_fractions_list_comprehension(lst):
    return round(sum([x / y for x, y in lst]))


class SumFractions(unittest.TestCase):
    def test_sum_fractions(self):
        self.assertEqual(sum_fractions([[36, 4], [22, 60]]), 9)
        self.assertEqual(sum_fractions([[-11, 12], [18, 13], [4, 5]]), 1)
        self.assertEqual(sum_fractions([[11, 12], [18, 13], [4, 5]]), 3)
        self.assertEqual(sum_fractions([[18, 13], [4, 5]]), 2)
        self.assertEqual(sum_fractions([[41, 14], [10, 91]]), 3)
        self.assertEqual(sum_fractions(
            [[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]), 11)

    def test_sum_fractions_list_comprehension(self):
        self.assertEqual(sum_fractions_list_comprehension(
            [[36, 4], [22, 60]]), 9)
        self.assertEqual(sum_fractions_list_comprehension(
            [[-11, 12], [18, 13], [4, 5]]), 1)
        self.assertEqual(sum_fractions_list_comprehension(
            [[11, 12], [18, 13], [4, 5]]), 3)
        self.assertEqual(
            sum_fractions_list_comprehension([[18, 13], [4, 5]]), 2)
        self.assertEqual(sum_fractions_list_comprehension(
            [[41, 14], [10, 91]]), 3)
        self.assertEqual(sum_fractions_list_comprehension(
            [[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]), 11)


if __name__ == '__main__':
    unittest.main()
