import unittest
import random

"""
Lario and Muigi Pipe Problem

Issue
Looks like some hoodlum plumber and his brother has been running around and
damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you
receive any more complaints. Each pipe should be connecting, since the levels
ascend, you can assume every number in the sequence after the first index will
be greater than the previous and that there will be no duplicates.

Task
Given the a list of numbers, return the list so that the values increment
by 1 for each index up to the maximum value.

Example
Input: 1,3,5,6,7,8

Output: 1,2,3,4,5,6,7,8
"""


def pipe_fix(nums):
    return [x for x in range(nums[0], nums[-1] + 1)]


class LarioAndMuigiPipeProblem(unittest.TestCase):
    def test_pipe_fix(self):
        self.assertEqual(pipe_fix([1, 2, 3, 5, 6, 8, 9]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(pipe_fix([1, 2, 3, 12]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(pipe_fix([6, 9]), [6, 7, 8, 9])
        self.assertEqual(pipe_fix([-1, 4]), [-1, 0, 1, 2, 3, 4])
        self.assertEqual(pipe_fix([1, 2, 3]), [1, 2, 3])

    def test_random_input(self):
        def check(indata, expected):
            lambda: self.assertEqual(pipe_fix(indata), expected)

        for _ in range(100):
            question = sorted(
                random.sample(range(0, 1000), random.randint(50, 100))
            )
            answer = list(range(min(question), max(question) + 1))
            check(question, answer)


if __name__ == '__main__':
    unittest.main()
