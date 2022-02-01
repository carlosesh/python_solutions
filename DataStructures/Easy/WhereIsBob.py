import unittest

"""
Where is Bob!?!

Write a function that searches a list of names (unsorted)
for the name "Bob" and returns the location in the list.
If Bob is not in the list, return -1.

Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2

find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0

find_bob(["Jimmy", "Layla", "James"]) ➞ -1

Notes
Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
"""


def find_bob(names):
    return names.index("Bob") if "Bob" in names else -1


class WhereIsBob(unittest.TestCase):
    def test_find_bob(self):
        self.assertEqual(find_bob(["Jimmy", "Layla", "Mandy"]), -1)
        self.assertEqual(find_bob(["Bob", "Nathan", "Hayden"]), 0)
        self.assertEqual(find_bob(["Paul", "Layla", "Bob"]), 2)
        self.assertEqual(
            find_bob(["Garry", "Maria", "Bethany", "Bob", "Pauline"]), 3)


if __name__ == '__main__':
    unittest.main()
