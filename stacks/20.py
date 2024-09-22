'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# https://leetcode.com/problems/valid-parentheses/

import unittest

def is_valid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets:
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

class TestValidParentheses(unittest.TestCase):
    def test_example1(self):
        s = "()"
        expected = True
        # Call the function that solves the problem
        result = is_valid(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "()[]{}"
        expected = True
        # Call the function that solves the problem
        result = is_valid(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "(]"
        expected = False
        # Call the function that solves the problem
        result = is_valid(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example4(self):
        s = "([])"
        expected = True
        # Call the function that solves the problem
        result = is_valid(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()