import unittest

"""
Binary Tree Nodes

We have two lists _N and _P, where _N represents the value of a node in Binary
Tree, and _P is the parent of _N.

N	P
1	2
3	2
6	8
9	8
2	5
8	5
5	-1
Write a function to find the node type of the node within this Binary Tree,
ordered by the value of the node. Output one of the following:

* Root: If node is root node.
* Leaf: If node is leaf node.
* Inner: If node is neither root nor leaf node.
* Not exist: If node not exist.

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"

(Binary Tree Example) [https://edabit-challenges.s3.amazonaws.com/binary-tree-example.png]

Notes
All values of _N list are unique.
"""


def node_type(_N, _P, n):


class BinaryTreeNodes(unittest.TestCase):
    def test_node_type(self):
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 1), "Leaf")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 2), "Inner")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 3), "Leaf")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 5), "Root")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 6), "Leaf")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 8), "Inner")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 9), "Leaf")
        self.assertEqual(node_type([1, 3, 6, 9, 2, 8, 5], [
                         2, 2, 8, 8, 5, 5, -1], 10), "Not exist")
        self.assertEqual(node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [
                         3, 1, 6, 1, 2, 3, 8, -1, 6], 8), "Inner")
        self.assertEqual(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [
                         8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 11), "Leaf")
        self.assertEqual(node_type(
            [3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 3), "Root")
        self.assertEqual(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [
                         8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 4), "Inner")
        self.assertEqual(node_type(
            [3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 6), "Leaf")
        self.assertEqual(node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [
                         3, 1, 6, 1, 2, 3, 8, -1, 6], 5), "Leaf")
        self.assertEqual(node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [
                         8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 8), "Root")
        self.assertEqual(node_type(
            [3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 10), "Inner")


if __name__ == '__main__':
    unittest.main()
