import unittest

"""
Remove Repeated Characters

Create a function that will remove any repeated charcter(s) in a word passed to
the function. Not just consecutive characters, but characters repeating anywhere
in the input.

Examples
unrepeated("hello") ➞ "helo"

unrepeated("aaaaa") ➞ "a"

unrepeated("WWE!!!") ➞ "WE!"

unrepeated("call 911") ➞ "cal 91"

Notes
* No more than two words will be passed in the tests.
* Input includes special characters and numbers.
"""


def unrepeated(txt):
    seen = []
    for character in range(len(txt)):
        if txt[character] not in seen:
            seen.append(txt[character])

    return "".join(seen)


def unrepeated_dict(txt):
    return "".join(dict.fromkeys(txt))


class RemoveRepeatedCharacters(unittest.TestCase):
    def test_unrepeated(self):
        self.assertEqual(unrepeated("hello"), "helo")
        self.assertEqual(unrepeated("aaaaa"), "a")
        self.assertEqual(unrepeated("WWE!!!"), "WE!")
        self.assertEqual(unrepeated("call 911"), "cal 91")
        self.assertEqual(unrepeated("altwaff test"), "altwf es")
        self.assertEqual(unrepeated("Mississippi"), "Misp")
        self.assertEqual(unrepeated("Tennessee"), "Tens")
        self.assertEqual(unrepeated("Massachusetts"), "Maschuet")

    def test_unrepeated_dict(self):
        self.assertEqual(unrepeated_dict("hello"), "helo")
        self.assertEqual(unrepeated_dict("aaaaa"), "a")
        self.assertEqual(unrepeated_dict("WWE!!!"), "WE!")
        self.assertEqual(unrepeated_dict("call 911"), "cal 91")
        self.assertEqual(unrepeated_dict("altwaff test"), "altwf es")
        self.assertEqual(unrepeated_dict("Mississippi"), "Misp")
        self.assertEqual(unrepeated_dict("Tennessee"), "Tens")
        self.assertEqual(unrepeated_dict("Massachusetts"), "Maschuet")


if __name__ == '__main__':
    unittest.main()
