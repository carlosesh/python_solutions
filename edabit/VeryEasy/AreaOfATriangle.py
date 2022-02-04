import unittest

"""
Area of a Triangle
Write a function that takes the base and height of a triangle
and return its area.

Examples
tri_area(3, 2) ➞ 3

tri_area(7, 4) ➞ 14

tri_area(10, 10) ➞ 50

Notes
* The area of a triangle is: (base * height) / 2
* Don't forget to return the result.
* If you get stuck on a challenge, find help in the Resources tab.
* If you're really stuck, unlock solutions in the Solutions tab.
"""


def tri_area(base, height):
    return (base * height) / 2


class AreaOfATriangle(unittest.TestCase):
    def test_tri_area(self):
        self.assertEqual(tri_area(3, 2), 3)
        self.assertEqual(tri_area(5, 4), 10)
        self.assertEqual(tri_area(10, 10), 50)
        self.assertEqual(tri_area(0, 60), 0)
        self.assertEqual(tri_area(12, 11), 66)


if __name__ == '__main__':
    unittest.main()
