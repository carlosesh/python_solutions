"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
* 1 <= n <= 45
"""

class Solution:

    """
    Complexity Analysis

    Time complexity : O(n). Single loop upto nn.

    Space complexity : O(n). dp array of size nn is used.
    """

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            fib = [1, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
        return fib[n]


    """
    Complexity Analysis
    
    Time complexity : O(n). Single loop upto n is required to calculate n^th fibonacci number.
    
    Space complexity : O(1). Constant space is used.
    """
    def climbStairsConstant(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second