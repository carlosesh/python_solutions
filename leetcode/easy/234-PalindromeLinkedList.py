"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:
* The number of nodes in the list is in the range [1, 105].
* 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    Complexity Analysis

    Time complexity : O(n), where nn is the number of nodes in the Linked List.
        In the first part, we're copying a Linked List into an Array List. Iterating down a Linked List in sequential
        order is O(n), and each of the n writes to the ArrayList is O(1). Therefore, the overall cost is O(n).

    Space complexity : O(n), where nn is the number of nodes in the Linked List.
        We are making an Array List and adding nn values to it.
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current, result = head, []
        while current is not None:
            result.append(current.val)
            current = current.next

        return result == result[::-1]
