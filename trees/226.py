'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# https://leetcode.com/problems/invert-binary-tree/

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

class TestInvertBinaryTree(unittest.TestCase):
    def tree_to_list(self, root):
        if not root:
            return []
        return self.tree_to_list(root.left) + [root.val] + self.tree_to_list(root.right)

    def assertTreeEqual(self, root1, root2):
        self.assertEqual(self.tree_to_list(root1), self.tree_to_list(root2))

    def test_example1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
        result = invert_tree(root)
        self.assertTreeEqual(result, expected)

    def test_example2(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        expected = TreeNode(2, TreeNode(3), TreeNode(1))
        result = invert_tree(root)
        self.assertTreeEqual(result, expected)

    def test_example3(self):
        root = None
        expected = None
        result = invert_tree(root)
        self.assertTreeEqual(result, expected)

if __name__ == '__main__':
    unittest.main()