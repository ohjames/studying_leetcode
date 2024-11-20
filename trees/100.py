'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

# https://leetcode.com/problems/same-tree/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

class TestIsSameTree(unittest.TestCase):
    def test1(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(isSameTree(p, q), True)

    def test2(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertEqual(isSameTree(p, q), False)

    def test3(self):
        p = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(1, TreeNode(2)))
        q = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
        self.assertEqual(isSameTree(p, q), False)

if __name__ == '__main__':
    unittest.main()