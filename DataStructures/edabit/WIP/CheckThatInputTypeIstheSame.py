import unittest

"""
Check That Input Type Is the Same

Create a function that checks if the given arguments are of the same type.
Return True if they are and False if they're not.

Examples
compare_data(1, 6, 5, 3, 7, 9) ➞ True

compare_data(1, 6, 5, 3, "7", 9) ➞ False

compare_data([]) ➞ True

compare_data([1], (1)) ➞ False
Notes
If no input is given or only one input, return True.
Use the (*args) construct to enter an undefined number of function arguments.

"""

# not solved yet


def compare_data(*args):
    if args is None:
        return True
    else:
        args_list = []
        for arg in args:
            if (isinstance(arg, list) or isinstance(arg, dict) or isinstance(arg, dict)) and len(arg) == 0:
                continue
            else:
                args_list.append(arg)

        print(args_list)
        print(all(args_list))
        return all(args_list)


class CheckThatInputTypeIstheSame(unittest.TestCase):
    def test_compare_data(self):
        self.assertEqual(compare_data(), True, "It's no data, expected True")
        self.assertEqual(compare_data('T', 'e', 's', 't'),
                         True, "All is string, expected True")
        self.assertEqual(compare_data([]), True, "It's emply list expected True")
        self.assertEqual(compare_data(2, 5, 7, 9, 0, 1, 2, 4, 6),
                         True, "It's multiple integers expected True")
        self.assertEqual(compare_data(2, 5, 7, '9', 0, 1, 2, 4, 6),
                         False, "It's multiple integers  and string expected False")
        self.assertEqual(compare_data(True, False), True,
                         "It's bool, expected True")
        self.assertEqual(compare_data(True, 'False'), False,
                         "It's bool and string, expected False")
        self.assertEqual(compare_data((i for i in range(
            10)), (j**2 for j in range(8))), True, "It's 'generator', expected True")


if __name__ == '__main__':
    unittest.main()
