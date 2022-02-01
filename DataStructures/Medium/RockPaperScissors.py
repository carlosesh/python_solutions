import unittest

"""
Rock, Paper, Scissors

Create a function which takes two strings (p1 and p2 ⁠— which represent player 1
and 2) as arguments and returns a string stating the winner in a game of Rock,
Paper, Scissors.

Each argument will contain a single string: "Rock", "Paper", or "Scissors".
Return the winner according to the following rules:

Rock beats Scissors
Scissors beats Paper
Paper beats Rock
If p1 wins, return the string "The winner is p1". If p2 wins, return the string
"The winner is p2" and if p1 and p2 are the same, return "It's a draw".

Examples
rps("Rock", "Paper") ➞ "The winner is p2"

rps("Scissors", "Paper") ➞ "The winner is p1"

rps("Paper", "Paper") ➞ "It's a draw"

Notes
All inputs will be valid strings.
"""

def rps(p1, p2):
    if p1 == "Rock" and p2 == "Scissors":
        return "The winner is p1"
    elif p1 == "Scissors" and p2 == "Rock":
        return "The winner is p2"
    elif p1 == "Scissors" and p2 == "Paper":
        return "The winner is p1"
    elif p1 == "Paper" and p2 == "Scissors":
        return "The winner is p2"
    elif p1 == "Paper" and p2 == "Rock":
        return "The winner is p1"
    elif p1 == "Rock" and p2 == "Paper":
        return "The winner is p2"
    else:
        return "It's a draw"


class RockPaperScissors(unittest.TestCase):
    def test_rps(self):
        self.assertEqual(rps("Rock", "Paper"), "The winner is p2")
        self.assertEqual(rps("Scissors", "Rock"), "The winner is p2")
        self.assertEqual(rps("Scissors", "Paper"), "The winner is p1")
        self.assertEqual(rps("Paper", "Rock"), "The winner is p1")
        self.assertEqual(rps("Paper", "Paper"), "It's a draw")
        self.assertEqual(rps("Rock", "Rock"), "It's a draw")


if __name__ == '__main__':
    unittest.main()
