"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
[0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
[0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
[0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

* n == nums.length
* 1 <= n <= 104
* 0 <= nums[i] <= n
* All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity?
"""


class Solution:
    """
    Gauss' Formula
    Time complexity O(n)
    Space complexity O(1)
    """

    def missingNumber(self, nums):
        nums_length = len(nums)
        expected_sum = nums_length * (nums_length + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    """
    Time complexity O(nlgn)
    Space complexity O(1)
    """

    def missingNumber(self, nums):
        nums.sort()
        for index, num in enumerate(nums):
            if index != num:
                return index
        return len(nums)

    """
    Gauss' Formula
    Time complexity O(n): Because the set allows for \mathcal{O}(1)O(1)
    containment queries, the main loop runs in \mathcal{O}(n)O(n) time.
    Creating num_set costs \mathcal{O}(n)O(n) time, as each set insertion runs
    in amortized O(1) time, so the overall runtime is O(n + n) = O(n)

    Space complexity O(n): nums contains n-1n−1 distinct elements, so it costs
    O(n) space to store a set containing all of them.
    """

    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    """
    Time complexity O(n)
    Space complexity O(1)

    Because we know that nums contains nn numbers and that it is missing exactly
    one number on the range [0..n-1][0..n−1], we know that nn definitely replaces
    the missing number in nums. Therefore, if we initialize an integer to nn and
    XOR it with every index and value, we will be left with the missing number.
    Consider the following example (the values have been sorted for intuitive
    convenience, but need not be):
    """

    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
