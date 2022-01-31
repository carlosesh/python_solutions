
import unittest
"""
Create a function that takes two arguments:
the original price and the discount percentage
as integers and returns the final price after the discount.

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25

Notes
Your answer should be rounded to two decimal places.
"""
def discount(price, discount):
    result = price - (price*(discount/100))
    return round(result, 2)

class FindTheDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEquals(discount(100, 75), 25)
        self.assertEquals(discount(211, 50), 105.5)
        self.assertEquals(discount(593, 61), 231.27)
        self.assertEquals(discount(1693, 80), 338.6)
        self.assertEquals(discount(700, 10), 630)


if __name__ == '__main__':
    unittest.main()
