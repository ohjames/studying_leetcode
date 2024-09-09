'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# https://leetcode.com/problems/valid-palindrome/

import unittest

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

class TestValidPalindrome(unittest.TestCase):
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        # Call the function that solves the problem
        result = is_palindrome(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "race a car"
        expected = False
        # Call the function that solves the problem
        result = is_palindrome(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        s = " "
        expected = True
        # Call the function that solves the problem
        result = is_palindrome(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
