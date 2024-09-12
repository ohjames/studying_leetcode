'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"] 

Constraints:

1 <= n <= 8
'''

# https://leetcode.com/problems/generate-parentheses/

import unittest

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    result = []
    backtrack('', 0, 0)
    return result

class TestGenerateParentheses(unittest.TestCase):
    def test_example1(self):
        n = 3
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        # Call the function that solves the problem
        result = generate_parentheses(n)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        n = 1
        expected = ["()"]
        # Call the function that solves the problem
        result = generate_parentheses(n)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()