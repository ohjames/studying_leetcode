'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''

# https://leetcode.com/problems/basic-calculator/

import unittest

def calculate(s):
    stack = []
    result = 0
    num = 0
    sign = 1
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    result += sign * num
    return result

class TestCalculate(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculate("1 + 1"), 2)

    def test2(self):
        self.assertEqual(calculate(" 2-1 + 2 "), 3)

    def test3(self):
        self.assertEqual(calculate("(1+(4+5+2)-3)+(6+8)"), 23)

if __name__ == '__main__':
    unittest.main()