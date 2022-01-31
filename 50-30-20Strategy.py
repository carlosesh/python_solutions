import unittest
"""
50-30-20 Strategy
The 50-30-20 strategy is a simple way to budget,
which involves spending 50% of after-tax income on needs,
30% after tax income on wants, and 20% after-tax income on
savings or paying off debt.

Given the after-tax income as ati, what you are supposed
to do is to make a function that will return a dictionary
that shows how much a person needs to spend on needs, wants,
and savings.

Examples
fifty_thirty_twenty(10000) ➞
{ "Needs": 5000, "Wants": 3000, "Savings": 2000 }

fifty_thirty_twenty(50000) ➞
{ "Needs": 25000, "Wants": 15000, "Savings": 10000 }

fifty_thirty_twenty(13450) ➞
{ "Needs": 6725, "Wants": 4035, "Savings": 2690 }

Notes
Check the Resources tab if you want to learn more about the 50-30-20 budget strategy.
"""
def fifty_thirty_twenty(ati):
    return {
        "Needs": ati / 2,
        "Wants": ati * 0.3,
        "Savings": ati * 0.2,
    }


class FiftyThirtyTwentyStrategy(unittest.TestCase):
    def test_fifty_thirty_twenty(self):
        self.assertEqual(fifty_thirty_twenty(10000), {"Needs": 5000, "Wants": 3000, "Savings": 2000})
        self.assertEqual(fifty_thirty_twenty(50000), {"Needs": 25000, "Wants": 15000, "Savings": 10000})
        self.assertEqual(fifty_thirty_twenty(13450), {"Needs": 6725, "Wants": 4035, "Savings": 2690})
        self.assertEqual(fifty_thirty_twenty(27800), {"Needs": 13900, "Wants": 8340, "Savings": 5560})
        self.assertEqual(fifty_thirty_twenty(19000), {"Needs": 9500, "Wants": 5700, "Savings": 3800})
        self.assertEqual(fifty_thirty_twenty(17610), {"Needs": 8805, "Wants": 5283, "Savings": 3522})
        self.assertEqual(fifty_thirty_twenty(25000), {"Needs": 12500, "Wants": 7500, "Savings": 5000})
        self.assertEqual(fifty_thirty_twenty(100000), {"Needs": 50000, "Wants": 30000, "Savings": 20000})
        self.assertEqual(fifty_thirty_twenty(347100), {"Needs": 173550, "Wants": 104130, "Savings": 69420})


if __name__ == '__main__':
    unittest.main()
