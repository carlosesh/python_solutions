import unittest
from itertools import chain, cycle, islice
from random import choice, randint, shuffle
"""
Removing Elements

Take an array and remove every second element from the array. Always keep the
first element and start removing with the next element.

Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_other(my_list):
    return [my_list[x] for x in range(len(my_list)) if x % 2 == 0]


def remove_every_other_improved(my_list):
    return my_list[::2]


class RemovingElements(unittest.TestCase):
    def test_remove_every_other(self):
        self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                         ['Hello', 'Hello Again'])
        self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         [1, 3, 5, 7, 9])
        self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])
        self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                         [['Goodbye']])

    def test_random_input(self):
        def solution(seq):
            return seq[::2]

        def random_element(seq):
            element = choice(seq)
            return choice((element, [element], {element: choice(seq)}))

        n = randint(20, 50)
        all_of_them = list(chain(
            islice(cycle((True, False)), n),
            (a * 1.75 for a in range(1, n + 1)),
            range(n),
            islice(cycle(('Hello', 'Goodbye', 'Yes', 'No')), n)
        ))
        shuffle(all_of_them)

        for _ in range(100):
            test_seq = [random_element(all_of_them)
                        for __ in range(randint(1, 30))]
            sol = solution(test_seq)
            self.assertEqual(remove_every_other(test_seq), sol)


if __name__ == '__main__':
    unittest.main()
