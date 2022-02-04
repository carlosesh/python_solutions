import unittest
import random

"""
Game Hit the target

given a matrix n x n (2-7), determine if the arrow is directed to the target (x).
There will be only 1 arrow '>' and 1 target 'x'
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
Examples:
given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' '], --> return true
[' ', '>', ' ', 'x'],
[' ', ' ', ' ', ' ']
]
given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', '>', ' ', ' '], --> return false
[' ', ' ', ' ', 'x'],
[' ', ' ', ' ', ' ']
]
given matrix 4x4:
[
[' ', ' ', ' ', ' '],
[' ', 'x', '>', ' '], --> return false
[' ', '', ' ', ' '],
[' ', ' ', ' ', ' ']
]

In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7
Happy hacking as they say!
"""


def solution(mtrx):
    for row in range(len(mtrx)):
        arrow_idx = 0
        target_idx = 0
        for column in range(len(mtrx[row])):
            if '>' in mtrx[row] and 'x' in mtrx[row]:
                if mtrx[row][column] == '>':
                    arrow_idx = [row] + [column]
                elif mtrx[row][column] == 'x':
                    target_idx = [row] + [column]
        if arrow_idx < target_idx:
            return True

    return False


def solution_improved(mtrx):
    for row in mtrx:
        if ">" in row and "x" in row:
            return row.index(">") < row.index("x")
    return False


def createArr(n):
    import random
    ar = [[' '] * n for i in range(n)]
    n -= 1
    firstIndex = [random.randint(0, n), random.randint(0, n)]
    secIndex = [random.randint(0, n), random.randint(0, n)]

    while secIndex == firstIndex:
        secIndex = [random.randint(0, n), random.randint(0, n)]

    ar[firstIndex[0]][firstIndex[1]] = '>'
    ar[secIndex[0]][secIndex[1]] = 'x'

    return ar


class GameHitTheTarget(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([
            ['>', ' '],
            [' ', 'x']
        ]), False)

        self.assertEqual(solution([
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', '>', ' ', 'x'],
            [' ', ' ', '', ' ', ' ']
        ]), True)

        self.assertEqual(solution([
            [' ', ' ', ' ', ' '],
            ['>', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            ['x', ' ', ' ', ' ']
        ]), False)

        self.assertEqual(solution([
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            ['x', '>', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]), False)

        self.assertEqual(solution([
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', '>', 'x', ' ']
        ]), True)

    def test_random_input(self):
        for i in range(100):
            ar = createArr(random.randint(2, 7))
            self.assertEqual(solution(ar.copy()), solution_improved(ar))


if __name__ == '__main__':
    unittest.main()
