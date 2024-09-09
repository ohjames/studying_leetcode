'''
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import unittest

def longest_substring_without_repeating_characters(s):
    start = 0
    max_length = 0
    used_characters = {}
    for i, char in enumerate(s):
        if char in used_characters and start <= used_characters[char]:
            start = used_characters[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used_characters[char] = i
    return max_length

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_example1(self):
        s = "abcabcbb"
        expected = 3
        # Call the function that solves the problem
        result = longest_substring_without_repeating_characters(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "bbbbb"
        expected = 1
        # Call the function that solves the problem
        result = longest_substring_without_repeating_characters(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "pwwkew"
        expected = 3
        # Call the function that solves the problem
        result = longest_substring_without_repeating_characters(s)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()