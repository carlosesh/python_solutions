import unittest

"""
String to Dictionary

Create a function that takes a list of strings and returns a dictionary.

Examples
str_to_dict(["1=one", "2=two", "3=three", "4=four"])
➞ {"1": "one", "2": "two", "3": "three", "4": "four"}

str_to_dict(["dog=bark", "cat=meow", "cow=moo"])
➞ {"dog": "bark", "cat": "meow", "cow": "moo"}

str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"])
➞ {"bob": "human", "lola": "dog", "mittens": "cat", "todd": "frog"}

Notes
* Key and value with be separated with =.
* Input list will be of various lengths.
* The key will be the first element in the string and the value with be the second.
"""


def str_to_dict(lst):
    dictionary = dict()
    for items in lst:
        item = items.split('=')
        if item[0] not in dictionary:
            dictionary[item[0]] = item[1]

    return dictionary


class StringToDictionary(unittest.TestCase):
    def test_str_to_dict(self):
        self.assertEqual(str_to_dict(["name=bob", "balance=500", "salary=10000", "friends=0"]), {
                         "name": "bob", "balance": "500", "salary": "10000", "friends": "0"})
        self.assertEqual(str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]), {
                         "bob": "human", "lola": "dog", "mittens": "cat", "todd": "frog"})
        self.assertEqual(str_to_dict(["greeting=Hello There!", "dismissal=Goodbye!", "thanks=Thank you!"]), {
                         "greeting": "Hello There!", "dismissal": "Goodbye!", "thanks": "Thank you!"})
        self.assertEqual(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]), {
                         "dog": "bark", "cat": "meow", "cow": "moo"})
        self.assertEqual(str_to_dict(["1=one", "2=two", "3=three", "4=four"]), {
                         "1": "one", "2": "two", "3": "three", "4": "four"})
        self.assertEqual(str_to_dict(["1=one", "1=one", "1=one", "1=one"]), {
                         "1": "one"})


if __name__ == '__main__':
    unittest.main()
