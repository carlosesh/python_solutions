import unittest

"""
C*ns*r*d Str*ngs

Someone has attempted to censor my strings by replacing every vowel with a *,
l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original
uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes
The vowels are given in the correct order.
The number of vowels will match the number of * characters in the censored string.
"""


def uncensor(txt, vowels):
    txt_list, vowels_list = list(txt), list(vowels)
    i = len(txt_list) - 1
    while i >= 0:
        if txt_list[i] == '*':
            vowel = vowels_list.pop()
            txt_list[i] = vowel
        i -= 1

    return "".join(txt_list)


class CensoredStrings(unittest.TestCase):
    def test_uncensor(self):
        self.assertEqual(uncensor('Wh*r* d*d my v*w*ls g*?',
                                  'eeioeo'), 'Where did my vowels go?')
        self.assertEqual(uncensor('abcd', ''), 'abcd', 'Works with no vowels.')
        self.assertEqual(uncensor('*PP*RC*S*', 'UEAE'),
                         'UPPERCASE', 'Works with uppercase')
        self.assertEqual(uncensor('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee'),
                         'Cheese, Grommit -- cheese', 'Works with * at the end')
        self.assertEqual(uncensor('*l*ph*nt', 'Eea'),
                         'Elephant', 'Works with * at the start')


if __name__ == '__main__':
    unittest.main()
