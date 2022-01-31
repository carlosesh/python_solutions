import unittest

"""
Which One Is Your Type?

Python has three main types of data structures formed by
smaller objects:

* Lists, written with [] square brackets, such as [1, 2, 4, 8].
* Tuples, written with () parentheses, such as (7, 8, 9).
* Sets, written with{} curly brackets, such as {2, 3, 5, 7, 11, 13}.

Each of these types has its own special properties and
peculiarities that are worth knowing, but this challenge
is only about transforming these data types into each other.

This can be done as in the following:

* tuple([1,2,4,8]) returns (1,2,4,8)
* list({2,3,5,7,11}) returns [2, 3, 5, 7, 11, 13]
* set((1,2,4)) returns {1,2,4}

Given two data structures, data1 and data2, return data2
converted to the type of data1.

Examples
convert([1, 2, 4, 8], (7, 8, 9)) ➞ [7, 8, 9]

convert((7, 8, 9), [1, 2, 4, 8]) ➞ (1, 2, 4, 8)

convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) ➞ [2, 3, 5, 7, 11, 13]

convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]) ➞ {8, 1, 2, 4}

Notes
* You might have noticed that the last example gives {8, 1, 2, 4}
rather than{1, 2, 4, 8}. This has to do with the fact that in
sets order doesn't matter, so that Python considers {8, 1, 2, 4}
and {1, 2, 4, 8} to be the same set.

* In the test cases you won't have to worry about orders:
the answers will always have the order given by applying the list(),
tuple(), set() functions.
"""
def convert(data1, data2):
    if type(data1) == type(data2):
        return data2
    elif isinstance(data1, list):
        return list(data2)
    elif isinstance(data1, tuple):
        return tuple(data2)
    else:
        return set(data2)

class WhichOneIsYourType(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert([1, 2, 4, 8], [1, 2, 4, 8]), [1, 2, 4, 8])
        self.assertEqual(convert([1, 2, 4, 8], (7, 8, 9)), [7, 8, 9])
        self.assertEqual(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}), [2, 3, 5, 7, 11, 13])
        self.assertEqual(convert((7, 8, 9), (7, 8, 9)), (7, 8, 9))
        self.assertEqual(convert((7, 8, 9), [1, 2, 4, 8]), (1, 2, 4, 8))
        self.assertEqual(convert((7, 8, 9), {2, 3, 5, 7, 11, 13}), (2, 3, 5, 7, 11, 13))
        self.assertEqual(convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]), {8, 1, 2, 4})
        self.assertEqual(convert({2, 3, 5, 7, 11, 13}, (7, 8, 9)), {8, 9, 7})
        self.assertEqual(convert({2, 3, 5, 7, 11, 13}, {2, 3, 5, 7, 11, 13}), {2, 3, 5, 7, 11, 13})


if __name__ == '__main__':
    unittest.main()
