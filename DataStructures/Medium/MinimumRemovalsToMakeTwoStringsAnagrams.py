import unittest

"""
Minimum Removals to Make Two Strings Anagrams
Create a function that returns the smallest number of letter removals so that
two strings are anagrams of each other.

Examples
min_removals("abcde", "cab") ➞ 2
# Remove "d", "e" to make "abc" and "cab".

min_removals("deafk", "kfeap") ➞ 2
# Remove "d" and "p" from the first and second word, respectively.

min_removals("acb", "ghi") ➞ 6
# Remove all letters from both words to get "" and "".

Notes
* An anagram is any string that can be formed by shuffling the characters of the
original string. For example: baedc is an anagram of abcde.
* An empty string can be considered an anagram of itself.
* Characters won't be used more than once per string.
"""


def remove_non_repeating_characters_from_lists(list1, list2):
    removals = []
    for char in range(len(list1)):
        if list1[char] not in list2:
            removals.append(list1[char])
    return removals


def remove_non_repeating_characters_from_lists_using_list_comprehension(list1, list2):
    return [x for x in range(len(list1)) if list1[x] not in list2]


def min_removals(txt1, txt2):
    return len(remove_non_repeating_characters_from_lists(txt1, txt2) + remove_non_repeating_characters_from_lists(txt2, txt1))


def min_removals_list_comprehension(txt1, txt2):
    return len(remove_non_repeating_characters_from_lists_using_list_comprehension(txt1, txt2) + remove_non_repeating_characters_from_lists_using_list_comprehension(txt2, txt1))


class MinimumRemovalsToMakeTwoStringsAnagrams(unittest.TestCase):
    def test_min_removals(self):
        self.assertEqual(min_removals("abcde", "cab"), 2)
        self.assertEqual(min_removals("deafk", "kfeap"), 2)
        self.assertEqual(min_removals("abc", "ghi"), 6)
        self.assertEqual(min_removals("abcxyz", "ghixytz"), 7)
        self.assertEqual(min_removals("aaaaaa", "bbbbbb"), 12)
        self.assertEqual(min_removals("", "bbbbbb"), 6)
        self.assertEqual(min_removals("aaaaaa", ""), 6)
        self.assertEqual(min_removals("", ""), 0)

    def test_min_removals_list_comprehension(self):
        self.assertEqual(min_removals_list_comprehension("abcde", "cab"), 2)
        self.assertEqual(min_removals_list_comprehension("deafk", "kfeap"), 2)
        self.assertEqual(min_removals_list_comprehension("abc", "ghi"), 6)
        self.assertEqual(min_removals_list_comprehension("abcxyz", "ghixytz"), 7)
        self.assertEqual(min_removals("aaaaaa", "bbbbbb"), 12)
        self.assertEqual(min_removals("", "bbbbbb"), 6)
        self.assertEqual(min_removals("aaaaaa", ""), 6)
        self.assertEqual(min_removals("", ""), 0)


if __name__ == '__main__':
    unittest.main()
