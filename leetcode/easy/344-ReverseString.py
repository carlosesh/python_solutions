"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:
* 1 <= s.length <= 105
* s[i] is a printable ascii character.
"""


class Solution:

    """
    Complexity Analysis

    Time complexity : O(N) to swap N/2 element.

    Space complexity : O(1), it's a constant space solution.
    """
    def reverseString(self, s: List[str]) -> None:
        s_length = len(s)
        for i in range(s_length // 2):
            temp = s[i]
            s[i] = s[s_length - 1 - i]
            s[s_length - 1 - i] = temp
