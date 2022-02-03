import unittest

"""
Count the Letters and Digits

Write a function that takes a string and calculates
the number of letters and digits within it.
Return the result in a dictionary.

Examples
count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

Notes
* Tests contain only alphanumeric characters.
* Spaces are not letters.
* All tests contain valid strings.
"""


def count_all(txt):
    letters, digits = 0, 0

    for char in range(len(txt)):
        if str.isalpha(txt[char]):
            letters += 1
        elif str.isdigit(txt[char]):
            digits += 1

    return {
        "LETTERS": letters,
        "DIGITS": digits
    }


class CountTheLettersAndDigits(unittest.TestCase):
    def test_count_all(self):
        self.assertEqual(count_all("Hello"), {"LETTERS": 5, "DIGITS": 0})
        self.assertEqual(count_all("137"), {"LETTERS": 0, "DIGITS": 3})
        self.assertEqual(count_all("H3LL0"), {"LETTERS": 3, "DIGITS": 2})
        self.assertEqual(count_all("149990"), {"LETTERS": 0, "DIGITS": 6})
        self.assertEqual(count_all("edabit 2018"), {
                         "LETTERS": 6, "DIGITS": 4}, "Spaces are not letters.")
        self.assertEqual(count_all("    "), {"LETTERS": 0, "DIGITS": 0})


if __name__ == '__main__':
    unittest.main()
