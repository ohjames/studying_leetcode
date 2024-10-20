'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

# https://leetcode.com/problems/group-anagrams/

import unittest

def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

class TestGroupAnagrams(unittest.TestCase):
    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = group_anagrams(strs)
        self.assertEqual(result, expected)

    def test_example2(self):
        strs = [""]
        expected = [[""]]
        result = group_anagrams(strs)
        self.assertEqual(result, expected)

    def test_example3(self):
        strs = ["a"]
        expected = [["a"]]
        result = group_anagrams(strs)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()