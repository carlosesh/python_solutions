import unittest

"""
Histogram Function

Build a function that creates histograms. Every bar needs to be on a new line
and its length corresponds to the numbers in the list passed as an argument.
The second argument of the function represents the character that needs to be used.

histogram(lst, char) -> str
Examples
histogram([1, 3, 4], "#") ➞ "#\n###\n####"

#
###
####

histogram([6, 2, 15, 3], "=") ➞ "======\n==\n===============\n==="

======
==
===============
===

histogram([1, 10], "+") ➞ "+\n++++++++++"

+
++++++++++

Notes
For better understanding try printing out the result.
"""

def histogram(lst, char):
    histogram_string = ""
    separator = "\n"
    for num in range(len(lst)):
        histogram_string += char * lst[num]
        if num != len(lst) - 1:
            histogram_string += separator

    return histogram_string

def histogram_list_comprehension(lst, char):
    return "\n".join(char * x for x in lst)


class HistogramFunction(unittest.TestCase):
    def test_histogram(self):
        self.assertEqual(histogram([2,4,5,6], "o"), 'oo\noooo\nooooo\noooooo')
        self.assertEqual(histogram([4,2], "*"), '****\n**')
        self.assertEqual(histogram([20,1,12], "H"), 'HHHHHHHHHHHHHHHHHHHH\nH\nHHHHHHHHHHHH')
        self.assertEqual(histogram([2,1,2,4,5,2,3], "#"), '##\n#\n##\n####\n#####\n##\n###')

    def test_histogram_list_comprehension(self):
        self.assertEqual(histogram_list_comprehension([2,4,5,6], "o"), 'oo\noooo\nooooo\noooooo')
        self.assertEqual(histogram_list_comprehension([4,2], "*"), '****\n**')
        self.assertEqual(histogram_list_comprehension([20,1,12], "H"), 'HHHHHHHHHHHHHHHHHHHH\nH\nHHHHHHHHHHHH')
        self.assertEqual(histogram_list_comprehension([2,1,2,4,5,2,3], "#"), '##\n#\n##\n####\n#####\n##\n###')


if __name__ == '__main__':
    unittest.main()
