'''
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import unittest

def find_all_anagrams_in_a_string(s, p):
    result = []
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
    left = 0
    right = 0
    count = len(p)
    while right < len(s):
        if s[right] in p_count:
            p_count[s[right]] -= 1
            if p_count[s[right]] >= 0:
                count -= 1
        if count == 0:
            result.append(left)
        if right - left == len(p) - 1:
            if s[left] in p_count:
                p_count[s[left]] += 1
                if p_count[s[left]] > 0:
                    count += 1
            left += 1
        right += 1
    return result

class TestFindAllAnagramsInAString(unittest.TestCase):
    def test_example1(self):
        s = "cbaebabacd"
        p = "abc"
        expected = [0, 6]
        result = find_all_anagrams_in_a_string(s, p)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "abab"
        p = "ab"
        expected = [0, 1, 2]
        result = find_all_anagrams_in_a_string(s, p)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "aaaaaaaaaa"
        p = "aaaaaaaaaaaaa"
        expected = []
        result = find_all_anagrams_in_a_string(s, p)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()