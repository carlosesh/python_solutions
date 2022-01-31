import unittest
import sys

"""
Find the Highest Integer in the List Using Recursion
Create a function that finds the highest integer in
the list using recursion.

Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8

Notes
Please use the recursion to solve this (not the max() method).
"""
def find_highest(lst):
    max = -sys.maxsize - 1
    return find_highest_recursive(lst, 0, max)

def find_highest_recursive(lst, iteration, max):
    if iteration == len(lst):
        return max
    else:
        max = lst[iteration] if  lst[iteration] > max else max
        return find_highest_recursive(lst, iteration+1, max)



class FindTheHighestIntegerInTheListUsingRecursion(unittest.TestCase):
    def test_find_highest(self):
        self.assertEqual(find_highest([8]), 8)
        self.assertEqual(find_highest([-1, 3, 5, 6, 99, 12, 2]), 99)
        self.assertEqual(find_highest([0, 12, 4, 87]), 87)


if __name__ == '__main__':
    unittest.main()
