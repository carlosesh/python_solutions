import unittest
"""
NothingIsNothing

Given any number of parameters (which is signified using *args syntax)
return True if none of the variables are falsy/empty.

Examples
nothing_is_nothing(0, False, [], {}) ➞ False

nothing_is_nothing(33, "Hello", (True, True, 3)) ➞ True

nothing_is_nothing(True, None) ➞ False

Notes
*args allows a function to take any number of parameters.
Falsy refers to values which evaluate to False in a boolean context. This includes (but is not limited to) variables such as 0, False, None, empty sets, lists and tuples.
"""
def nothing_is_nothing_all(*args):
    return all(args)


def nothing_is_nothing(*args):
    for i in args:
        if not i:
            return False
    return True


class NothingIsNothing(unittest.TestCase):

    def test_nothing_is_nothing_all(self):
        self.assertEqual(nothing_is_nothing_all(0, False, [], {}), False)
        self.assertEqual(nothing_is_nothing_all(33, 'Hello', (True, True, 3)), True)
        self.assertEqual(nothing_is_nothing_all(True, None), False)
        self.assertEqual(nothing_is_nothing_all(None, None), False)
        self.assertEqual(nothing_is_nothing_all(None, True), False)
        self.assertEqual(nothing_is_nothing_all(221), True)
        self.assertEqual(nothing_is_nothing_all(221, 0, 0, 0), False)
        self.assertEqual(nothing_is_nothing_all([221, 0, 0, 0]), True)

    def test_nothing_is_nothing(self):
        self.assertEqual(nothing_is_nothing(0, False, [], {}), False)
        self.assertEqual(nothing_is_nothing(33, 'Hello', (True, True, 3)), True)
        self.assertEqual(nothing_is_nothing(True, None), False)
        self.assertEqual(nothing_is_nothing(None, None), False)
        self.assertEqual(nothing_is_nothing(None, True), False)
        self.assertEqual(nothing_is_nothing(221), True)
        self.assertEqual(nothing_is_nothing(221, 0, 0, 0), False)
        self.assertEqual(nothing_is_nothing([221, 0, 0, 0]), True)


if __name__ == '__main__':
    unittest.main()
