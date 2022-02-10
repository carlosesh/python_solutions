import unittest
"""
The Karaca's Encryption Algorithm

Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a: 0
e: 1
i: 2
o: 2
u: 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"

Notes
All inputs are strings, no uppercases and all output must be strings.
"""


def encrypt(word):
    encryption = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 2,
        'u': 3
    }
    seen = []
    for i in range(len(word)):
        if word[i] in encryption.keys() and word[i] not in seen:
            word = word.replace(word[i], str((encryption.get(word[i]))))
            seen.append(word[i])

    return word[::-1] + "aca"


class TheKaracasEncryptionAlgorithm(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("karaca"), "0c0r0kaca")
        self.assertEqual(encrypt("burak"), "k0r3baca")
        self.assertEqual(encrypt("banana"), "0n0n0baca")
        self.assertEqual(encrypt("alpaca"), "0c0pl0aca")
        self.assertEqual(encrypt("hello"), "2ll1haca")


if __name__ == '__main__':
    unittest.main()
