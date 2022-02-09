import unittest

"""
Stock Picker

Create a function that takes a list of integers that represent the amount in
dollars that a single stock is worth, and return the maximum profit that could
have been made by buying stock on day x and selling stock on day y where y>x.

If given the following list:

[44, 30, 24, 32, 35, 30, 40, 38, 15]
... your program should return 16 because at index 2 the stock was worth $24 and
at the index 6 the stock was then worth $40, so if you bought the stock at 24
and sold it on 40, you would have made a profit of $16, which is the maximum
profit that could have been made with this list of stock prices.

If there is no profit that could have been made with the stock prices, then your
program should return -1 (e.g. [[10, 9, 8, 2]] should return -1).

Examples
stock_picker([10, 12, 4, 5, 9]) ➞ 5

stock_picker([14, 20, 4, 12, 5, 11]) ➞ 8

stock_picker([80, 60, 10, 8]) ➞ -1
"""


def stock_picker(lst):
    lst_len = len(lst)
    if lst_len == 0 or lst is None:
        return 0
    else:
        profits = []
        for day_x in range(lst_len):
            for day_y in range(day_x + 1, lst_len):
                if lst[day_y] > lst[day_x]:
                    profit = lst[day_y] - lst[day_x]
                    if profit not in profits:
                        profits.append(profit)

        return -1 if len(profits) == 0 else max(profits)


class StockPicker(unittest.TestCase):
    def test_stock_picker(self):
        self.assertEqual(stock_picker([90, 100, 111, 0, 1, 2, 3]), 21)
        self.assertEqual(stock_picker([1, 2, 4, 10, 100, 2, 3]), 99)
        self.assertEqual(stock_picker([10, 1000, 1, 1, 1, 2000, 3]), 1999)
        self.assertEqual(stock_picker([7, 1, 5, 5, 2, 1, 3]), 4)
        self.assertEqual(stock_picker([100, 10, 8, 5]), -1)


if __name__ == '__main__':
    unittest.main()
