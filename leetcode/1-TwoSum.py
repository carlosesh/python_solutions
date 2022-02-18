"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    """
    Time complexity O(n):We traverse the list containing nn elements exactly
    twice. Since the hash table reduces the lookup time to O(1), the overall
    time complexity is O(n).

    Space complexity O(n): The extra space required depends on the number of
    items stored in the hash table, which stores exactly nn elements.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        nums_iterator = range(len(nums))

        for i in nums_iterator:
            hashmap[nums[i]] = i

        for i in nums_iterator:
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    """
    Time complexity O(n + m):We traverse the list containing n elements exactly
    once but we also lookup the value in the dictionary.

    Space complexity O(n): The extra space required depends on the number of
    items stored in the hash table, which stores exactly nn elements.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement + nums[i] == target and complement in seen:
                return [seen.get(complement), i]
            seen[nums[i]] = i

        return "No two sum solution"
