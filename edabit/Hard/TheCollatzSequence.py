import unittest

"""
The Collatz Sequence

The Collatz sequence is as follows:

* Start with some given integer n.
* If it is even, the next number will be n divided by 2.
* If it is odd, multiply it by 3 and add 1 to make the next number.
* The sequence stops when it reaches 1.

According to the Collatz conjecture, it will always reach 1. If that's true, you
can construct a finite sequence following the aforementioned method for any
given integer.

Write a function that takes in an integer n and returns the highest integer in
the corresponding Collatz sequence.

Examples
max_collatz(10) ➞ 16
# Collatz sequence: 10, 5, 16, 8, 4, 2, 1

max_collatz(32) ➞ 32
# Collatz sequence: 32, 16, 8, 4, 2, 1

max_collatz(85) ➞ 256
# Collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1
"""


def max_collatz(num):
    def max_collatz_recursive(num, max):
        if num == 1:
            return max
        else:
            max = num if num > max else max
            return max_collatz_recursive(num / 2, max) if num % 2 == 0 else max_collatz_recursive((num * 3) + 1, max)

    return max_collatz_recursive(num, num)


class TheCollatzSequence(unittest.TestCase):
    def test_max_collatz(self):
        self.assertEqual(max_collatz(161), 9232)
        self.assertEqual(max_collatz(23), 160)
        self.assertEqual(max_collatz(48), 48)
        self.assertEqual(max_collatz(1), 1)
        self.assertEqual(max_collatz(70), 160)
        self.assertEqual(max_collatz(908), 1024)
        self.assertEqual(max_collatz(369), 1108)
        self.assertEqual(max_collatz(3500), 3940)
        self.assertEqual(max_collatz(33), 100)
        self.assertEqual(max_collatz(715), 3220)


if __name__ == '__main__':
    unittest.main()
