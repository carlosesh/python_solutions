import unittest
from random import randint

"""
Your start-up's BA has told marketing that your website has a large audience in
Scandinavia and surrounding countries. Marketing thinks it would be great to
welcome visitors to the site in their own language. Luckily you already use an
API that detects the user's location, so this is an easy win.

- Think of a way to store the languages as a database (eg an object).
The languages are listed below so you can copy and paste!
- Write a 'welcome' function that takes a parameter 'language' (always a string),
and returns a greeting - if you have it in your database. It should default to
English if the language is not in the database, or in the event of an invalid input.
"""


def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')


class Welcome(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet('english'), 'Welcome')
        self.assertEqual(greet('dutch'), 'Welkom')
        self.assertEqual(greet('IP_ADDRESS_INVALID'), 'Welcome')
        self.assertEqual(greet(''), 'Welcome')
        self.assertEqual(greet(2), 'Welcome')

    def test_random_input(self):
        def sol(l): return {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst', 'dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 'flemish': 'Welgekomen', 'french': 'Bienvenue',
                            'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}.get(l, 'Welcome')
        base = ['english', 'czech', 'IP_ADDRESS_INVALID', 'danish', 'IP_ADDRESS_NOT_FOUND', 'dutch',
                'estonian', 'IP_ADDRESS_NOT_FOUND', 'finnish', 'flemish', 'french', 'german', 'irish', 'italian',
                'IP_ADDRESS_REQUIRED', 'latvian', 'IP_ADDRESS_REQUIRED', 'lithuanian', 'polish', 'IP_ADDRESS_NOT_FOUND',
                'spanish', 'swedish', 'IP_ADDRESS_NOT_FOUND', 'welsh', 'IP_ADDRESS_NOT_FOUND', 'IP_ADDRESS_INVALID']

        for _ in range(40):
            l = base[randint(0, len(base) - 1)]
            self.assertEqual(greet(l), sol(
                l), "It should work for random inputs too")


if __name__ == '__main__':
    unittest.main()
