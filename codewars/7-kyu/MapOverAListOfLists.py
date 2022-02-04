import unittest

"""
Map over a list of lists


Write a function which maps a function over the lists in a list:

def grid_map(inp, op)
    # which performs op(element) for all elements of inp

Example 1:

x = [[1,2,3],
     [4,5,6]]

grid_map(x, lambda x: x + 1)
-- returns [[2,3,4],[5,6,7]]

grid_map(x, lambda x: x ** 2)
-- returns [[1,4,9],[16,25,36]]
Example 2

x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
grid_map(x, lambda x: x.upper())
-- returns [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
"""


def grid_map_list_comprehension(lst, op):
    return [[*map(op, x)] for x in lst]


def grid_map_using_map(inp, op):
    lst_copy = inp.copy()
    res = []
    for c in range(len(lst_copy)):
        res.append(list(map(op, inp[c])))

    return res


class MapOverAListOfLists(unittest.TestCase):

    num_grid = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 2, 4]]
    char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

    def test_case2(self):
        self.assertEqual(grid_map_using_map(self.num_grid, lambda x: x * 2),
                         [[2, 4, 6, 8], [10, 12, 14, 16, 18], [0, 4, 8]])

    def test_case3(self):
        self.assertEqual(grid_map_using_map(self.num_grid, lambda x: x ** 2),
                         [[1, 4, 9, 16], [25, 36, 49, 64, 81], [0, 4, 16]])

    def test_case4(self):
        self.assertEqual(grid_map(self.char_grid, lambda x: x.upper()),
                         [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])

    def test_case5(self):
        self.assertEqual(grid_map(self.char_grid, lambda x: x.lower()),
                         [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']])


if __name__ == '__main__':
    unittest.main()
