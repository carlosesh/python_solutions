import unittest

"""
Sales by Match

Given a list of integers representing the color of each sock, determine how many
pairs of socks with matching colors there are. For example, there are 7 socks
with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching
pairs of socks that are available.

Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0
"""


def sock_merchant(lst):
    seen = dict()
    for num in lst:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    return sum([x for x in seen.values() if x > 1]) // 2


class SalesByMatch(unittest.TestCase):
    def test_sock_merchant(self):
        self.assertEqual(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)
        self.assertEqual(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]), 4)
        self.assertEqual(sock_merchant([90, 20, 30, 40, 40, 20, 30, 20, 90]), 4)
        self.assertEqual(sock_merchant([10, 40, 40, 40, 40, 20, 10, 10, 10]), 4)
        self.assertEqual(sock_merchant([50, 40, 30, 10, 60, 60, 90, 80, 10]), 2)
        self.assertEqual(sock_merchant([50, 40, 30, 100, 60, 65, 90, 80, 10]), 0)


if __name__ == '__main__':
    unittest.main()
