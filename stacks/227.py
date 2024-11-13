'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''

# https://leetcode.com/problems/basic-calculator-ii/

import unittest

def calculate(s):
    stack = []
    num = 0
    sign = '+'
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if char in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            sign = char
    return sum(stack)

class TestCalculate(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculate("3+2*2"), 7)

    def test2(self):
        self.assertEqual(calculate(" 3/2 "), 1)

    def test3(self):
        self.assertEqual(calculate(" 3+5 / 2 "), 5)

if __name__ == '__main__':
    unittest.main()