import unittest
import string
import random

"""
Counting Duplicates Across Multiple Lists

Given multiple lists (name, age, height), each of size n :

An entry contains one name, one age and one height. The attributes corresponding
to each entry are determined by the index of each list, for example entry 0 is
made up of name[0], age[0], height[0].

A duplicate entry is one in which the name, age and height are ALL the same.

Write a function which takes in the attributes for each entry and returns an
integer for the number of duplicated entries. For a set of duplicates, the
original entry should not be counted as a duplicate.
"""


def count_duplicates(name, age, height):
    if len(name) == len(age) and len(age) == len(height):
        people_tuple = []
        count = 0
        for i in range(len(name)):
            temp = (name[i], age[i], height[i])
            if temp not in people_tuple:
                people_tuple.append(temp)
            elif temp in people_tuple:
                count += 1

        return count
    else:
        return -1


def count_duplicates_improved(*args):
    return len(args[0]) - len(set(zip(*args)))


class CountingDuplicatesAcrossMultipleLists(unittest.TestCase):
    def test_no_duplicates(self):
        name = ['John', 'Beth', 'Beth', 'Bill']
        age = [37, 23, 30, 46]
        height = [183, 170, 165, 175]
        self.assertEqual(count_duplicates(name, age, height), 0)

    def test_one_entry_duplicate(self):
        name = ['John', 'Beth', 'Beth', 'Beth', 'Bill']
        age = [37, 23, 23, 23, 46]
        height = [183, 170, 170, 170, 175]
        self.assertEqual(count_duplicates(name, age, height), 2)

    def test_multi_entry_duplicates(self):
        name = ['Jack', 'Ben', 'Jack', 'Ben', 'Jack', 'Jack']
        age = [25, 25, 34, 25, 25, 34]
        height = [180, 180, 200, 180, 180, 200]
        self.assertEqual(count_duplicates(name, age, height), 3)

    def test_no_entries(self):
        name = []
        age = []
        height = []
        self.assertEqual(count_duplicates(name, age, height), 0)

    def test_all_duplicates(self):
        name = ['a', 'a', 'a', 'a', 'a']
        age = [1, 1, 1, 1, 1]
        height = [1, 1, 1, 1, 1]
        self.assertEqual(count_duplicates(name, age, height), 4)

    def test_large_input(self):
        name = ['2fr43'] * 1000000
        age = [4531] * 1000000
        height = [321] * 1000000
        self.assertEqual(count_duplicates(name, age, height), 999999)

        name = ['2fr43'] * 1000000
        name += ['4hjk32'] * 1000000
        age = [4531] * 1000000
        age += [341432] * 1000000
        height = [321] * 1000000
        height += [432143] * 1000000
        self.assertEqual(count_duplicates(name, age, height), 1999998)

    def test_random_input(self):
        names = '!?#£$'
        for i in range(1, 101):
            name = [''.join(random.choice(names) for _ in range(2))
                    for _ in range(i)]
            age = [random.randint(0, 10) for i in range(i)]
            height = [random.randint(0, 10) for i in range(i)]
            lstItems = list(zip(name, age, height))
            setItems = set(lstItems)
            answer = len(lstItems) - len(setItems)
            self.assertEqual(count_duplicates(name, age, height), answer)


if __name__ == '__main__':
    unittest.main()
