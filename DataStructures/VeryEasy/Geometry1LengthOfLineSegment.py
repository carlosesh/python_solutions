import unittest
import math

"""
Write a function that takes coordinates of two points
on a two-dimensional plane and returns the length of
the line segment connecting those two points.

Examples
line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41

Notes
The order of the given numbers is X, Y.
This challenge is easier than it looks.
Round your result to two decimal places.
"""
def line_length(dot1, dot2):
    return round(math.sqrt(pow(dot2[0] - dot1[0], 2) + pow(dot2[1] - dot1[1], 2)), 2)


class GeometryLengthOfLineSegment(unittest.TestCase):
    def test_line_length(self):
        self.assertEqual(line_length([15, 7], [22, 11]), 8.06)
        self.assertEqual(line_length([0, 0], [0, 0]), 0)
        self.assertEqual(line_length([0, 0], [1, 1]), 1.41)
        self.assertEqual(line_length([30, 10], [13, -5]), 22.67)


if __name__ == '__main__':
    unittest.main()
