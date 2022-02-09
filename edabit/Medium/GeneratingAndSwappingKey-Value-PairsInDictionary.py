import unittest

"""
Generating and Swapping Key-Value-Pairs in Dictionary

Create a function that takes:

A list of keys.
A list of values (same size).
True, if key and value should be swapped, else False.
The function returns the constructed dict. Empty lists return an empty dict.

Examples
swap_d([1, 2, 3], ["one", "two", "three"], False)
➞ { 1: "one", 2: "two", 3: "three" }

swap_d([1, 2, 3], ["one", "two", "three"], True)
➞ { "one": 1, "two": 2, "three": 3 }

swap_d(["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True)
➞ { "France": "Paris", "is odd": 3, "is half of 9": 4.5 }

Notes
To make it simple, use only hashable (= immutable) keys.
To make it simple, use only unique keys.
"""


def swap_d(k, v, swapped):
    if k is None or v is None or len(k) != len(v):
        return "No solution, both have to be the same length and/or not be null values"
    else:
        if not swapped:
            return dict(zip(k, v))
        else:
            return dict(zip(v, k))


class GeneratingAndSwappingKeyValuePairsInDictionary(unittest.TestCase):
    def test_swap_d(self):
        self.assertEqual(swap_d(["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True), {
            "France": "Paris", "is odd": 3, "is half of 9": 4.5})
        self.assertEqual(swap_d(["Paris", "Berlin", "Washington"], ["France", "Germany", "USA"], True), {
            "France": "Paris", "Germany": "Berlin", "USA": "Washington"})
        self.assertEqual(swap_d([(1, 2), (3, 4), (5, 6)], ["one_two", "three_four", "five_six"], True), {
            "one_two": (1, 2), "three_four": (3, 4), "five_six": (5, 6)})
        self.assertEqual(swap_d([(1, 2), (3, 4), (5, 6)], ["one_two", "three_four", "five_six"], False), {
            (1, 2): "one_two", (3, 4): "three_four", (5, 6): "five_six"})
        self.assertEqual(swap_d([], [], False), {})
        self.assertEqual(swap_d([1, 2, 3], ["one", "two", "three"], False), {
            1: "one", 2: "two", 3: "three"})
        self.assertEqual(swap_d([1, 2, 3], ["one", "two", "three"], True), {
            "one": 1, "two": 2, "three": 3})
        self.assertEqual(swap_d([1, 2, 3], ["one", "two"], True),
                         "No solution, both have to be the same length and/or not be null values")
        self.assertEqual(swap_d([1], ["one", "two"], True),
                         "No solution, both have to be the same length and/or not be null values")
        self.assertEqual(swap_d([1], None, True),
                         "No solution, both have to be the same length and/or not be null values")
        self.assertEqual(swap_d(None, [1], True),
                         "No solution, both have to be the same length and/or not be null values")


if __name__ == '__main__':
    unittest.main()
