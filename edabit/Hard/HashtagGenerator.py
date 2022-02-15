import unittest

"""
Hashtag Generator

Create a function that is a Hashtag Generator by using the following rules:

* The output must start with a hashtag (#).
* Each word in the output must have its first letter capitalized.
* If the final result, a single string, is longer than 140 characters, the
function should return false.
* If either the input (str) or the result is an empty string, the function should
return false.

Examples
generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"

generate_hashtag("") ➞ false, "Expected an empty string to return false"

generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."
"""


def generate_hashtag(txt):
    def hashtag_it(str):
        return "#" + "".join([x.title() for x in txt])

    if txt is None or len(txt) == 0:
        return False
    else:
        txt = txt.split()
        hashtaged = hashtag_it(txt)
        return False if len(txt) == 0 else (False if len(hashtaged) >= 140 else hashtaged)


class HashtagGenerator(unittest.TestCase):
    def test_generate_hashtag(self):
        self.assertEqual(generate_hashtag(""), False,
                         "Expected an empty string to return False")
        self.assertEqual(generate_hashtag(" " * 100),
                         False, "Still an empty string")
        self.assertEqual(generate_hashtag("Do We have A Hashtag"),
                         "#DoWeHaveAHashtag", "Expected a Hashtag (#) at the beginning.")
        self.assertEqual(generate_hashtag("Edabit"), "#Edabit",
                         "Should handle a single word.")
        self.assertEqual(generate_hashtag("Edabit Is Great"),
                         "#EdabitIsGreat", "Should remove spaces.")
        self.assertEqual(generate_hashtag("Edabit is great"), "#EdabitIsGreat",
                         "Should capitalize first letters of all words.")
        self.assertEqual(generate_hashtag("eda" + " " * 140 + "bit"), "#EdaBit")
        self.assertEqual(generate_hashtag("Smmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaalllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll Dog"),
                         False, "Should return False if the final word is longer than 140 chars.")
        self.assertEqual(generate_hashtag("e" * 121),
                         "#E" + "e" * 120, "Should work")
        self.assertEqual(generate_hashtag("e" * 140), False, "Too long")
        self.assertEqual(generate_hashtag(
            "    Hello     World   "), "#HelloWorld")


if __name__ == '__main__':
    unittest.main()
