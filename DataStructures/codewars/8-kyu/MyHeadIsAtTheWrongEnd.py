import unittest
from random import shuffle

"""
My head is at the wrong end!

You're at the zoo... all the meerkats look weird. Something has gone terribly
wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. You will be given an array which will
have three values (tail, body, head). It is your job to re-arrange the array so
that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: you
have to change the element positions with the same exact logics

Simples!
"""


def fix_the_meerkat(arr):
    return arr[::-1]


class MyHeadIsAtTheWrongEnd(unittest.TestCase):
    def test_fix_the_meerkat(self):
        self.assertEqual(fix_the_meerkat(["tail", "body", "head"]), [
                         "head", "body", "tail"])
        self.assertEqual(fix_the_meerkat(["tails", "body", "heads"]), [
                         "heads", "body", "tails"])
        self.assertEqual(fix_the_meerkat(["bottom", "middle", "top"]), [
                         "top", "middle", "bottom"])
        self.assertEqual(fix_the_meerkat(["lower legs", "torso", "upper legs"]), [
                         "upper legs", "torso", "lower legs"])
        self.assertEqual(fix_the_meerkat(["ground", "rainbow", "sky"]), [
                         "sky", "rainbow", "ground"])

    def test_random_input(self):
        def sol(a): return a[::-1]

        base = ["Kenshiro", "Raoh", "Kaiou", "Toki", "Hyo", "Jagi", "Han", "Souther",
                "Falco", "Rei", "Shoki", "Juda", "Taiga", "Shin", "Boltz", "Shin", "Soria"]

        for _ in range(40):
            shuffle(base)
            arr = base[:3]
            expected = sol(arr)

            def test_case():
                test.assert_equals(fix_the_meerkat(arr), expected)


if __name__ == '__main__':
    unittest.main()
