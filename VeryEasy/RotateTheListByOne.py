import unittest

"""
Rotate the List by One

Given a list, rotate the values clockwise by one
(the last value is sent to the first position).

Check the examples for a better understanding.

Examples
rotate_by_one([1, 2, 3, 4, 5]) ➞ [5, 1, 2, 3, 4]

rotate_by_one([6, 5, 8, 9, 7]) ➞ [7, 6, 5, 8, 9]

rotate_by_one([20, 15, 26, 8, 4]) ➞ [4, 20, 15, 26, 8]

Notes
All lists are the same size, so it's not necessary
to use loops or to think much about complex solutions.
"""
def rotate_by_one(lst):
    last = [lst[-1]]
    return last + lst[:-1]


class RotateTheListByOne(unittest.TestCase):
    def test_rotate_by_one(self):
        self.assertEqual(rotate_by_one([1,2,3,4,5]), [5, 1, 2, 3, 4])
        self.assertEqual(rotate_by_one([6,5,8,9,7]), [7, 6, 5, 8, 9])
        self.assertEqual(rotate_by_one([20,15,26,8,4]), [4, 20, 15, 26, 8])
        self.assertEqual(rotate_by_one([7,8,6,4,5]), [5, 7, 8, 6, 4])
        self.assertEqual(rotate_by_one([5,9,45,1,2]), [2, 5, 9, 45, 1])

if __name__ == '__main__':
    unittest.main()
