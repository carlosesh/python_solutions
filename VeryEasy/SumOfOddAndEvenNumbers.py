import unittest
"""
Write a function that takes a list of numbers and returns
a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.

Example

sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])

Notes
Count 0 as an even number.
"""

def sum_odd_and_even(lst):
    even = 0
    odd = 0
    for i in range(len(lst)):
        if(lst[i] % 2 == 0):
            even += lst[i]
        else:
            odd += lst[i]

    return [even, odd]

class SumOfOddAndEvenNumbers(unittest.TestCase):
    def test_sum_odd_and_even(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])
        self.assertEqual(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
        self.assertEqual(sum_odd_and_even([0, 0]), [0, 0])
        self.assertEqual(sum_odd_and_even([]), [0, 0])


if __name__ == '__main__':
    unittest.main()
