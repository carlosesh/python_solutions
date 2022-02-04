import unittest
import random

"""
Count Of Positives Sum Of Negatives
Given an array of integers.

Return an array, where the first element is the count of positives numbers and
the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should
return [10, -65].
"""


def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0]), sum([x for x in arr if x < 0])] if arr else []


class CountOfPositivesSumOfNegatives(unittest.TestCase):
    def test_count_positives_sum_negatives(self):
        self.assertEqual(count_positives_sum_negatives(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
        self.assertEqual(count_positives_sum_negatives(
            [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
        self.assertEqual(count_positives_sum_negatives([1]), [1, 0])
        self.assertEqual(count_positives_sum_negatives([-1]), [0, -1])
        self.assertEqual(count_positives_sum_negatives(
            [0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
        self.assertEqual(count_positives_sum_negatives([]), [])

    def test_random_input(self):
        def sol(arr): return reduce(lambda a, b: [
            a[0] + 1 if b > 0 else a[0], a[1] + b if b < 0 else a[1]], arr, [0, 0])

        for _ in range(40):
            arr = [randint(-100, 100) for q in range(randint(1, 100))]

            def test_case():
                expected = sol(arr)
                test.assert_equals(count_positives_sum_negatives(
                    arr), expected, "It should work for random inputs too")
