import unittest

"""
Length of Number

Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1

Notes
The use of the len() function is prohibited.
"""

def number_length(num):
	if num == 0:
		return 1
	else:
		count = 0
		while num > 0:
			count += 1
			num //= 10
		return count

class LengthOfNumber(unittest.TestCase):
	def test_number_length(self):
		self.assertEqual(number_length(10), 2)
		self.assertEqual(number_length(5000), 4)
		self.assertEqual(number_length(0), 1)
		self.assertEqual(number_length(4039182), 7)
		self.assertEqual(number_length(9999999999999999), 16)
		self.assertEqual(number_length(1), 1)
		self.assertEqual(number_length(777777777777777777777777777777), 30)


if __name__ == '__main__':
	unittest.main()
