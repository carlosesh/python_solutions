import unittest

"""
Using Lambda Functions
Create a function that returns its given argument, but by using a lambda function.

A lambda function is constructed like so:

lambda_func=lambda "parameters":#code here
Examples
lambda_func(3) ➞ 3

lambda_func("3") ➞ "3"

lambda_func(True) ➞ True

Notes
Check the Resources tab for more information on lambda functions.

https://www.w3schools.com/python/python_lambda.asp
https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
https://www.guru99.com/python-lambda-function.html
"""
# this shouldn't be done as a lambda function is an anonymous function, so,
# there's no need to define a function due to the nature of lambda functions
def lambda_func_method(parameter):
    return (lambda parameter : parameter) (parameter)

lambda_func = lambda n : n

class UsingLambdaFunctions(unittest.TestCase):

    def test_lambda_func(self):
        self.assertEqual(lambda_func(3),3)
        self.assertEqual(lambda_func("3"),"3")
        self.assertEqual(lambda_func(True),True)
        self.assertEqual(lambda_func("test"),"test")

    def test_lambda_func_method(self):
        self.assertEqual(lambda_func_method(3),3)
        self.assertEqual(lambda_func_method("3"),"3")
        self.assertEqual(lambda_func_method(True),True)
        self.assertEqual(lambda_func_method("test"),"test")


if __name__ == '__main__':
    unittest.main()
