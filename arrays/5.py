'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

# https://leetcode.com/problems/longest-palindromic-substring/

import unittest

def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if len(s) < 1:
        return ""
    longest = ""
    for i in range(len(s)):
        odd = expand_around_center(i, i)
        even = expand_around_center(i, i + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest

class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_example1(self):
        s = "babad"
        expected = "bab"
        result = longest_palindromic_substring(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "cbbd"
        expected = "bb"
        result = longest_palindromic_substring(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()