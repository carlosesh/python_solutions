import unittest
from random import randint

"""
Count the Monkeys

Description:
You take your son to the forest to see the monkeys. You know that there are a
certain number there (n), but your son is too young to just appreciate the full
number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n),
populate an array with all numbers up to and including that number,
but excluding zero.

For example:

monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]
"""


def monkey_count(n):
    return [x + 1 for x in range(n)]


class CountTheMonkeys(unittest.TestCase):
    def test_monkey_count(self):
        self.assertEqual(monkey_count(5), [1, 2, 3, 4, 5])
        self.assertEqual(monkey_count(3), [1, 2, 3])
        self.assertEqual(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(monkey_count(
            20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])\


    def test_random_input(self):
        def sol_count(n): return list(range(1, n + 1))

        for _ in range(40):
            n = randint(1, 100)

            def test_case():
                test.assert_equals(monkey_count(n), sol_count(
                    n), "It should work for random inputs too")


if __name__ == '__main__':
    unittest.main()
