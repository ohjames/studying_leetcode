'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if not node:
            return None
        if node == p or node == q:
            return node
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            return node
        return left or right

    return dfs(root)

class TestLowestCommonAncestor(unittest.TestCase):
    def test1(self):
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.right
        self.assertEqual(lowestCommonAncestor(root, p, q), root)

    def test2(self):
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.left.right.right
        self.assertEqual(lowestCommonAncestor(root, p, q), p)

    def test3(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        p = root.left
        q = root.right
        self.assertEqual(lowestCommonAncestor(root, p, q), root)

if __name__ == '__main__':
    unittest.main()