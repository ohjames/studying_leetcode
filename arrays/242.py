'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

# https://leetcode.com/problems/valid-anagram/

import unittest

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    return s_dict == t_dict

class TestValidAnagram(unittest.TestCase):
    def test_example1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        # Call the function that solves the problem
        result = is_anagram(s, t)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "rat"
        t = "car"
        expected = False
        # Call the function that solves the problem
        result = is_anagram(s, t)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
