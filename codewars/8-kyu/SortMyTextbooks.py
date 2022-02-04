import unittest
import random

"""
Sort My Textbooks

HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

The sorting should NOT be case sensitive
"""


def sorter(textbooks):
    textbooks.sort(key=str.lower)
    return textbooks


def sorter_improved(textbooks):
    return sorted(textbooks, key=str.lower)


class SortMyTextbooks(unittest.TestCase):

    def test_sorter(self):
        self.assertEqual(sorter(['Algebra', 'History', 'Geometry', 'English']), sorted(
            ['Algebra', 'History', 'Geometry', 'English'], key=lambda t: t.lower()), 'Does not sort strings')
        self.assertEqual(sorter(['Algebra', 'history', 'Geometry', 'english']), sorted(
            ['Algebra', 'history', 'Geometry', 'english'], key=lambda t: t.lower()), 'Does not handle capitalization')
        self.assertEqual(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']), sorted(
            ['Alg#bra', '$istory', 'Geom^try', '**english'], key=lambda t: t.lower()), 'Does not handle symbols')

    def test_random_input(self):
        for i in range(1, 51):
            words = []
            for j in range(random.randint(5, 15)):
                strng = ''
                for k in range(random.randint(5, 15)):
                    strng += chr(45 + int(random.random() * 80))
                words.append(strng)

            self.assertEqual(sorter(words[:]), sorted(
                words, key=lambda t: t.lower()), "Random test " + str(i))

            self.assertEqual(sorter_improved(words[:]), sorted(
                words, key=lambda t: t.lower()), "Random test " + str(i))


if __name__ == '__main__':
    unittest.main()
