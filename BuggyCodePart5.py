import unittest
"""
Mubashir created an infinite loop! Help him by fixing
the code in the code tab to pass this challenge.
Look at the examples below to get an idea of what
the function should do.

Examples
print_list(1) ➞ [1]

print_list(3) ➞ [1, 2, 3]

print_list(6) ➞ [1, 2, 3, 4, 5, 6]

Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""

def print_list(n):
    result, i = [], 1

    while i<=n:
        result += [i]
        i += 1

    return result


class BuggyCodePart5(unittest.TestCase):

    def test_print_list(self):
        self.assertEqual(print_list(1), [1])
        self.assertEqual(print_list(2), [1,2])
        self.assertEqual(print_list(3), [1,2,3])
        self.assertEqual(print_list(4), [1,2,3,4])
        self.assertEqual(print_list(5), [1,2,3,4,5])
        self.assertEqual(print_list(6), [1,2,3,4,5,6])
        self.assertEqual(print_list(7), [1,2,3,4,5,6,7])
        self.assertEqual(print_list(8), [1,2,3,4,5,6,7,8])
        self.assertEqual(print_list(9), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(print_list(10), [1,2,3,4,5,6,7,8,9,10])


if __name__ == '__main__':
    unittest.main()
