import unittest

"""
The objective of Duck, duck, goose is to walk in a circle, tapping on each
player's head until one is chosen.

Given an array of Player objects and an index (1-based), return the name of the
chosen Player(name is a property of Player objects, e.g Player.name)

Example:

duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name

"""


def duck_duck_goose(players, goose):
    count = 0
    players_length = len(players)

    if goose <= players_length:
        return players[goose - 1].name
    else:
        i = 0
        while i < players_length:
            if i == (players_length - 1):
                if count == goose - 1:
                    break
                i = 0
                count += 1
                continue
            elif count == goose - 1:
                break
            else:
                count += 1
                i += 1
        return players[i].name


def duck_duck_goose_improved(players, goose):
    return players[(goose % len(players)) - 1].name


class Player:
    def __init__(self, name):
        self.name = name


class DuckDuckGoose(unittest.TestCase):
    ex_names = ["a", "b", "c", "d", "c", "e", "f", "g", "h", "z"]
    players = list(map((lambda x: Player(x)), ex_names))

    def test_duck_duck_goose(self):
        self.assertEqual(duck_duck_goose(self.players, 1),  "a")
        self.assertEqual(duck_duck_goose(self.players, 3),  "c")
        self.assertEqual(duck_duck_goose(self.players, 10), "z")
        self.assertEqual(duck_duck_goose(self.players, 20), "z")
        self.assertEqual(duck_duck_goose(self.players, 30), "z")
        self.assertEqual(duck_duck_goose(self.players, 18), "g")
        self.assertEqual(duck_duck_goose(self.players, 28), "g")
        self.assertEqual(duck_duck_goose(self.players, 12), "b")
        self.assertEqual(duck_duck_goose(self.players, 2),  "b")
        self.assertEqual(duck_duck_goose(self.players, 7),  "f")

    def test_duck_duck_goose_improved(self):
        self.assertEqual(duck_duck_goose_improved(self.players, 1),  "a")
        self.assertEqual(duck_duck_goose_improved(self.players, 3),  "c")
        self.assertEqual(duck_duck_goose_improved(self.players, 10), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 20), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 30), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 18), "g")
        self.assertEqual(duck_duck_goose_improved(self.players, 28), "g")
        self.assertEqual(duck_duck_goose_improved(self.players, 12), "b")
        self.assertEqual(duck_duck_goose_improved(self.players, 2),  "b")
        self.assertEqual(duck_duck_goose_improved(self.players, 7),  "f")


if __name__ == '__main__':
    unittest.main()
