import unittest
import random
import heapq

"""
Return Two Highest Values in List

In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []
"""


def two_highest(arg1):
    if len(arg1) == 0:
        return []
    else:
        largest = 0
        second_largest = 0
        for item in arg1:
            if item > largest:
                second_largest = largest  # NEW!
                largest = item
            elif largest > item > second_largest:
                second_largest = item

        return arg1 if len(arg1) <= 2 else [largest, second_largest]


def two_highest_cw_solution(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False


class ReturnTwoHighestValuesInList(unittest.TestCase):
    def test_two_highest(self):
        self.assertEqual(two_highest([15, 20, 20, 17]), [20, 17])
        self.assertEqual(two_highest([]), [])
        self.assertEqual(two_highest([15]), [15])

    def test_random_input(self):
        for i in range(200):
            a = random.sample(range(100000), random.randint(1, 50))
            result = heapq.nlargest(2, sorted(a))
            self.assertEqual(two_highest_cw_solution(a), result)


if __name__ == '__main__':
    unittest.main()
