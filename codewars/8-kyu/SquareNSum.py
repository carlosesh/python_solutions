import unittest
from random import randint

"""
Square(n) Sum

Complete the square sum function so that it squares each number passed into it
and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""


def square_sum(numbers):
    return sum([x**2 for x in numbers])


class SquareNSum(unittest.TestCase):
    def test_square_sum(self):
        self.assertEqual(square_sum([1, 2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([-1, -2]), 5)
        self.assertEqual(square_sum([-1, 0, 1]), 2)

    def test_random_input(self):
        def square_sol(n): return sum([x * x for x in n])

        for _ in range(40):
            lst = [randint(0, 40) - 20 for _ in range(randint(2, 10))]

            def test_case():
                expected = square_sol(lst)
                self.assertEqual(square_sum(lst), expected,
                                 "It should work for random inputs too")


if __name__ == '__main__':
    unittest.main()
