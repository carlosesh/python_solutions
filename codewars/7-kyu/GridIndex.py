import unittest

"""
Grid index

You are given an n by n ( square ) grid of characters, for example:

[['m', 'y', 'e'],
 ['x', 'a', 'm'],
 ['p', 'l', 'e']]
You are also given a list of integers as input, for example:

[1, 3, 5, 8]
You have to find the characters in these indexes of the grid if you think of the indexes as:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Remember that the indexes start from one and not zero.

Then you output a string like this:
"meal"

All inputs will be valid.
"""


def grid_index(grid, indexes):
    index_dict = dict()
    current = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            index_dict[current] = grid[row][column]
            current += 1

    return "".join(index_dict.get(i - 1) for i in indexes)


class GridIndex(unittest.TestCase):
    def test_grid_index(self):
        results1 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [
                              1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(results1, 'myexample')
        results2 = grid_index(
            [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6])
        self.assertEqual(results2, 'mam')
        results3 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], [
                              'p', 'l', 'e']], [1, 3, 7, 8])
        self.assertEqual(results3, 'mepl')
        results4 = grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], [
                              'e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']], [5, 7, 9, 3, 6, 6, 8, 8, 16, 13])
        self.assertEqual(results4, 'ooelccddrr')


if __name__ == '__main__':
    unittest.main()
