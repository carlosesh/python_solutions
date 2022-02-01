import unittest

"""
Sum of Even Pairs in List

Given a list with an even amount of numbers,
return True if the sum of two numbers in the list
is even and False if the sum of two numbers in the list is odd.

To illustrate:

11, 15, 6, 8, 9, 10
11 + 15 = 26 = True
15 + 6 = 21 = False
6 + 8 = 14 = True
Examples
odd_sum_list([11, 15, 6, 8, 9, 10])
➞ [True, False, True, False, False]

odd_sum_list([12, 21, 5, 9, 65, 32])
➞ [False, True, True, True, False]

oddSumArr([1, 2, 3, 4, 5, 6])
➞ [False, False, False, False, False]

Notes
* Remember that the length of all the lists will be an even number, so it is not necessary to measure lengths.
* If you are stuck, look in the Resources tab.
"""


def odd_sum_list(lst):
    result = []
    for i in range(1, len(lst)):
        result.append(True if (lst[i - 1] + lst[i]) % 2 == 0 else False)

    return result


class SumOfEvenPairsInList(unittest.TestCase):
    def test_odd_sum_list(self):
        self.assertEqual(odd_sum_list([11, 15, 6, 8, 9, 10]), [
                         True, False, True, False, False])
        self.assertEqual(odd_sum_list([12, 21, 5, 9, 65, 32]), [
                         False, True, True, True, False])
        self.assertEqual(odd_sum_list([12, 21, 5, 9, 65, 32]), [
                         False, True, True, True, False])
        self.assertEqual(odd_sum_list([1, 2, 3, 4, 5, 6]), [
                         False, False, False, False, False])
        self.assertEqual(odd_sum_list([4, 5, 6, 7, 9, 45, 12, 32, 65, 49, 45, 840]), [
                         False, False, False, True, True, False, True, False, True, True, False])
        self.assertEqual(odd_sum_list([88, 45, 654, 123]), [
                         False, False, False])
        self.assertEqual(odd_sum_list([98, 4, 12, 565, 798, 465, 13, 1, 365, 14, 89, 565]), [
                         True, True, False, False, False, True, True, True, False, False, True])


if __name__ == '__main__':
    unittest.main()
