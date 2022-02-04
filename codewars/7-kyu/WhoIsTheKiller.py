import unittest
from random import randint, choice
from string import ascii_letters

"""
Who is the killer?
Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know
every person who those suspects have seen on the day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they
have seen on that day which may look like this:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and also a list of the names of the dead people:

['Lucas', 'Bill']

return the name of the one killer, in our case 'James' because he is the only
person that saw both 'Lucas' and 'Bill'
"""


def killer(suspect_info, dead):
    for suspect, persons in suspect_info.items():
        if all(name in persons for name in dead):
            return suspect


class WhoIsTheKiller(unittest.TestCase):
    def test_killer(self):
        self.assertEqual(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': [
                         'David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James')
        self.assertEqual(
            killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')

    def test_random_input(self):
        def name_maker():
            s, length = '', randint(3, 12)
            for loop in range(length):
                s += choice(ascii_letters)
            return s

        def info_maker():
            amount_of_suspects = randint(1, 50)
            innocent = {name_maker(): [name_maker() for name in range(
                randint(1, 100))] for suspect in range(amount_of_suspects)}
            murderer = name_maker()
            killed = [name_maker() for loop in range(1, 25)]
            innocent[murderer] = list(set(killed) | set(
                [name_maker() for name in range(0, 10)]))
            return [innocent, killed, murderer]

        for loop in range(250):
            inps = info_maker()
            suspects = inps[0]
            killed = inps[1]
            murderer = inps[2]
            self.assertEqual(killer(suspects, killed), murderer)


if __name__ == '__main__':
    unittest.main()
