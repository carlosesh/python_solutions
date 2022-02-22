"""
You are in charge of the cake for a child's birthday. You have decided the cake
will have one candle for each year of their total age. They will only be able to
blow out the tallest of the candles. Count how many candles are tallest.

https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    biggest_candle = max(candles)
    return len([x for x in candles if x == biggest_candle])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
