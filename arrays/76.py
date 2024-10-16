'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

# https://leetcode.com/problems/minimum-window-substring/

import unittest

def minimum_window_substring(s, t):
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    left = 0
    right = 0
    count = len(t)
    min_length = float('inf')
    min_start = 0
    while right < len(s):
        if s[right] in t_count:
            t_count[s[right]] -= 1
            if t_count[s[right]] >= 0:
                count -= 1
        while count == 0:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left
            if s[left] in t_count:
                t_count[s[left]] += 1
                if t_count[s[left]] > 0:
                    count += 1
            left += 1
        right += 1
    return "" if min_length == float('inf') else s[min_start:min_start + min_length]

class TestMinimumWindowSubstring(unittest.TestCase):
    def test_example1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        result = minimum_window_substring(s, t)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "a"
        t = "a"
        expected = "a"
        result = minimum_window_substring(s, t)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "a"
        t = "aa"
        expected = ""
        result = minimum_window_substring(s, t)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()