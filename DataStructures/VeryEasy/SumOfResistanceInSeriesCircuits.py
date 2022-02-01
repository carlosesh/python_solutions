import unittest

def series_resistance(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return f"{sum} ohm" if sum < 10 else f"{sum} ohms"

def series_resistance_with_sum_function(lst):
    lst_sum = sum(lst)
    return f"{lst_sum} ohm" if lst_sum < 10 else f"{lst_sum} ohms"

class SumOfResistanceInSeriesCircuits(unittest.TestCase):
    def test_series_resistance(self):
        self.assertEqual(series_resistance([1, 5, 6, 3]), "15 ohms")
        self.assertEqual(series_resistance([0.2, 0.3, 0.4]), "0.9 ohm")
        self.assertEqual(series_resistance([10,12, 1, 10]), "33 ohms")
        self.assertEqual(series_resistance([10,13, 3.8, 20, 10]), "56.8 ohms")
        self.assertEqual(series_resistance([0.5, 0.5]), "1.0 ohm")
        self.assertEqual(series_resistance([16, 30, 22.8, 4]), "72.8 ohms")
        self.assertEqual(series_resistance([20, 15, 32.5, 2]), "69.5 ohms")
        self.assertEqual(series_resistance([52, 22, 20, 30]), "124 ohms")
        self.assertEqual(series_resistance([10, 12, 32, 4.9, 5, 6, 71]), "140.9 ohms")

    def test_series_resistance_with_sum_function(self):
        self.assertEqual(series_resistance_with_sum_function([1, 5, 6, 3]), "15 ohms")
        self.assertEqual(series_resistance_with_sum_function([0.2, 0.3, 0.4]), "0.9 ohm")
        self.assertEqual(series_resistance_with_sum_function([10,12, 1, 10]), "33 ohms")
        self.assertEqual(series_resistance_with_sum_function([10,13, 3.8, 20, 10]), "56.8 ohms")
        self.assertEqual(series_resistance_with_sum_function([0.5, 0.5]), "1.0 ohm")
        self.assertEqual(series_resistance_with_sum_function([16, 30, 22.8, 4]), "72.8 ohms")
        self.assertEqual(series_resistance_with_sum_function([20, 15, 32.5, 2]), "69.5 ohms")
        self.assertEqual(series_resistance_with_sum_function([52, 22, 20, 30]), "124 ohms")
        self.assertEqual(series_resistance_with_sum_function([10, 12, 32, 4.9, 5, 6, 71]), "140.9 ohms")

if __name__ == '__main__':
    unittest.main()
