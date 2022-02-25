"""
938. Range Sum of BST -> https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a
value in the inclusive range [low, high].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, low, high, sum_of_nodes):
            stack = [root]
            while stack:
                node = stack.pop()
                val = node.val
                sum_of_nodes = sum_of_nodes + val if low <= val <= high else sum_of_nodes
                if node.left is not None and low < val:
                    stack.append(node.left)
                if node.right is not None and val < high:
                    stack.append(node.right)

            return sum_of_nodes

        return helper(root, low, high, 0)