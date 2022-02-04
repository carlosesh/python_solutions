import unittest
from random import randint as R

"""
Reverse List Order

In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples
reverse_list([1,2,3,4]) == [4,3,2,1]
reverse_list([3,1,5,4]) == [4,5,1,3]
"""


def reverse_list(l):
    return l[::-1]


class ReverseListOrder(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([3, 1, 5, 4]), [4, 5, 1, 3])
        self.assertEqual(reverse_list([3, 6, 9, 2]), [2, 9, 6, 3])
        self.assertEqual(reverse_list([1]), [1])

    def test_random_input(self):
        for _ in range(100):
            a = [R(-10, 10) for _ in range(R(0, 10))]
            b = a[::-1]

            def test_case():
                test.assert_equals(reverse_list(a), b)


if __name__ == '__main__':
    unittest.main()
