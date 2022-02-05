import unittest

"""
Some but not all
Description
Your task is to create a function that given a sequence and a predicate, returns True if only some (but not all) the
elements in the sequence are True after applying the predicate

Examples
some('abcdefg&%$', str.isalpha)
>>> True

some('&%$=', str.isalpha)
>>> False

some('abcdefg', str.isalpha)
>>> False

some([4, 1], lambda x: x>3)
>>> True

some([1, 1], lambda x: x>3)
>>> False

some([4, 4], lambda x: x>3)
>>> False
"""


def some_but_not_all(seq, pred):
    flag_list = []
    for item in seq:
        flag_list.append(pred(item))

    return False if all(flag_list) else any(flag_list)


class SomeButNotAll(unittest.TestCase):
    def test_some_but_not_all(self):
        self.assertEqual(some_but_not_all('abcdefg&%$', str.isalpha), True)
        self.assertEqual(some_but_not_all('&%$=', str.isalpha), False)
        self.assertEqual(some_but_not_all('abcdefg', str.isalpha), False)
        self.assertEqual(some_but_not_all([4, 1], lambda x: x > 3), True)
        self.assertEqual(some_but_not_all([1, 1], lambda x: x > 3), False)
        self.assertEqual(some_but_not_all([4, 4], lambda x: x > 3), False)


if __name__ == '__main__':
    unittest.main()
