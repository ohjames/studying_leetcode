'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# https://leetcode.com/problems/maximum-depth-of-binary-tree/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = 3
        result = max_depth(root)
        self.assertEqual(result, expected)

    def test_example2(self):
        root = TreeNode(1, None, TreeNode(2))
        expected = 2
        result = max_depth(root)
        self.assertEqual(result, expected)

    def test_example3(self):
        root = None
        expected = 0
        result = max_depth(root)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()