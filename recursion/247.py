'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: n = 2
Output: ["11","69","88","96"]

Example 2:
Input: n = 1
Output: ["0","1","8"]

Constraints:
1 <= n <= 14
'''

# https://leetcode.com/problems/strobogrammatic-number-ii/

import unittest

def find_strobogrammatic(n):
    def helper(n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        result = []
        for num in helper(n - 2, m):
            if n != m:
                result.append('0' + num + '0')
            result.append('1' + num + '1')
            result.append('6' + num + '9')
            result.append('8' + num + '8')
            result.append('9' + num + '6')
        return result
    return helper(n, n)

class TestStrobogrammaticNumberII(unittest.TestCase):
    def test_example1(self):
        n = 2
        expected = ["11","69","88","96"]
        # Call the function that solves the problem
        result = find_strobogrammatic(n)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        n = 1
        expected = ["0","1","8"]
        # Call the function that solves the problem
        result = find_strobogrammatic(n)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()