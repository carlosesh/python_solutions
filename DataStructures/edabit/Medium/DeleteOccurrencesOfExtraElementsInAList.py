import unittest

"""
Delete Occurrences of Extra Elements in a List

Create a function that takes two arguments: a list lst and a number num. If an
element occurs in lst more than num times, remove the extra occurrence(s) and
return the result.

Examples
delete_occurrences([1, 1, 1, 1], 2) ➞ [1, 1]

delete_occurrences([13, True, 13, None], 1) ➞ [13, True, None]

delete_occurrences([True, True, True], 3) ➞ [True, True, True]

Notes
Do not alter the order of the original list.
"""


def delete_occurrences(lst, num):
    ocurrences = []
    for i in lst:
        if ocurrences.count(i) < num:
            ocurrences.append(i)

    return ocurrences


class DeleteOccurrencesOfExtraElementsInAList(unittest.TestCase):
    def test_delete_occurrences(self):
        self.assertEqual(delete_occurrences([1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(delete_occurrences(
            [True, True, True], 3), [True, True, True])
        self.assertEqual(delete_occurrences(
            [13, True, 13, None], 1), [13, True, None])
        self.assertEqual(delete_occurrences([], 100), [])
        self.assertEqual(delete_occurrences(
            ["John", "John", "Marry", "Marry"], 1), ["John", "Marry"])
        self.assertEqual(delete_occurrences(["Marry", "John", None, "John", False, "John", 0, "John", "Marry", "Marry", "John"], 3), [
                         "Marry", "John", None, "John", False, "John", 0, "Marry", "Marry"])
        self.assertEqual(delete_occurrences([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_occurrences(
            [1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertEqual(delete_occurrences([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3), [
                         1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
