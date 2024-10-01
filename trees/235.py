'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root

class TestLowestCommonAncestorOfABinarySearchTree(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.right
        expected = root
        result = lowest_common_ancestor(root, p, q)
        self.assertEqual(result, expected)

    def test_example2(self):
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.left.right
        expected = root.left
        result = lowest_common_ancestor(root, p, q)
        self.assertEqual(result, expected)

    def test_example3(self):
        root = TreeNode(2, TreeNode(1), None)
        p = root
        q = root.left
        expected = root
        result = lowest_common_ancestor(root, p, q)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()