import unittest

"""
Calculate the Profit
You work for a manufacturer, and have been asked to calculate the total profit
made on the sales of a product. You are given a dictionary containing the cost
price per unit (in dollars), sell price per unit (in dollars), and the starting
inventory. Return the total profit made, rounded to the nearest dollar.

Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030

Notes
Assume all inventory has been sold.
Profit = Total Sales - Total Cost
"""

def profit(info):
    return 0 if not info or info.get("inventory") == 0 else round(
        (info.get("inventory") * info.get("sell_price") -
        info.get("inventory") * info.get("cost_price"))
    )


class CalculateTheProfit(unittest.TestCase):
    def test_profit(self):
        self.assertEqual(profit({'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200}), 14796)
        self.assertEqual(profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800}), 20784)
        self.assertEqual(profit({'cost_price': 185.00, 'sell_price': 299.99, 'inventory': 300}), 34497)
        self.assertEqual(profit({'cost_price': 378.11, 'sell_price': 990.00, 'inventory': 99}), 60577)
        self.assertEqual(profit({'cost_price': 4.67, 'sell_price': 5.00, 'inventory': 78000}), 25740)
        self.assertEqual(profit({'cost_price': 19.87, 'sell_price': 110.00, 'inventory': 350}), 31546)
        self.assertEqual(profit({'cost_price': 2.91, 'sell_price': 4.50, 'inventory': 6000}), 9540)
        self.assertEqual(profit({'cost_price': 68.01, 'sell_price': 149.99, 'inventory': 500}), 40990)
        self.assertEqual(profit({'cost_price': 1.45, 'sell_price': 8.50, 'inventory': 10000}), 70500)
        self.assertEqual(profit({'cost_price': 10780, 'sell_price': 34999, 'inventory': 10}), 242190)
        self.assertEqual(profit({'cost_price': 10780, 'sell_price': 34999, 'inventory': 0}), 0)


if __name__ == '__main__':
    unittest.main()
