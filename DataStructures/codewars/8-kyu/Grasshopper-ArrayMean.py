import unittest
from random import randint

"""
Grasshopper - Array Mean

Find Mean
Find the mean (average) of a list of numbers in an array.

Information
To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.

For an example list of 1, 3, 5, 7

1. Add all of the numbers

1+3+5+7 = 16
2. Divide by the number of values in the list. In this example there are 4 numbers in the list.

16/4 = 4
3. The mean (or average) of this list is 4
"""


def find_average(nums):
    return sum(nums) / len(nums) if nums else 0


class GrasshopperArrayMean(unittest.TestCase):
    def test_find_average(self):
        self.assertEqual(find_average([1]), 1)
        self.assertEqual(find_average([1, 3, 5, 7]), 4)
        self.assertEqual(find_average([-1, 3, 5, -7]), 0)
        self.assertEqual(find_average([5, 7, 3, 7]), 5.5)
        self.assertEqual(find_average([]), 0)

    def test_random_input(self):
        def find_sol(nums): return 1.0 * sum(nums) / len(nums)

        for _ in range(40):
            nums = [randint(-10, 100) for x in range(randint(1, 20))]
            expected = find_sol(nums)

            def test_case():
                test.assert_equals(find_average(nums), expected)


if __name__ == '__main__':
    unittest.main()
