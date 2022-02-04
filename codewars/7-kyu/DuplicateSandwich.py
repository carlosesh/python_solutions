import unittest

"""
Duplicate sandwich

Task
In this kata you will be given a list consisting of unique elements except for
one thing that appears twice.

Your task is to output a list of everything inbetween both occurrences of this
element in the list.

Examples:
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
[0, 0] => []
[True, False, True] => [False]
['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
Notes
All elements will be the same datatype.
All used elements will be hashable.
"""


def duplicate_sandwich(arr):
    repeated_dict = dict()
    last_repeated, item = 0, 0
    for i in range(len(arr)):
        if arr[i] not in repeated_dict:
            repeated_dict[arr[i]] = i
        else:
            last_repeated = i
            item = arr[i]
            break

    return arr[repeated_dict.get(item) + 1:last_repeated]


class DuplicateSandwich(unittest.TestCase):
    def test_duplicate_sandwich(self):
        self.assertEqual(duplicate_sandwich(
            [0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
        self.assertEqual(duplicate_sandwich(
            ['None', 'Hello', 'Example', 'hello', 'None', 'Extra']), ['Hello', 'Example', 'hello'])
        self.assertEqual(duplicate_sandwich([0, 0]), [])
        self.assertEqual(duplicate_sandwich([True, False, True]), [False])
        self.assertEqual(duplicate_sandwich(
            ['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])


if __name__ == '__main__':
    unittest.main()
