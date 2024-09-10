'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

# https://leetcode.com/problems/ransom-note/

import unittest

def can_construct(ransomNote, magazine):
    magazine_dict = {}
    for char in magazine:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1
    for char in ransomNote:
        if char in magazine_dict and magazine_dict[char] > 0:
            magazine_dict[char] -= 1
        else:
            return False
    return True

class TestRansomNote(unittest.TestCase):
    def test_example1(self):
        ransomNote = "a"
        magazine = "b"
        expected = False
        # Call the function that solves the problem
        result = can_construct(ransomNote, magazine)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        ransomNote = "aa"
        magazine = "ab"
        expected = False
        # Call the function that solves the problem
        result = can_construct(ransomNote, magazine)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        ransomNote = "aa"
        magazine = "aab"
        expected = True
        # Call the function that solves the problem
        result = can_construct(ransomNote, magazine)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()