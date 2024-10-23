'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import unittest

def letter_combinations(digits):
    if not digits:
        return []
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        for letter in mapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    combinations = []
    backtrack(0, [])
    return combinations

class TestLetterCombinations(unittest.TestCase):
    def test_example1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = letter_combinations(digits)
        self.assertEqual(result, expected)

    def test_example2(self):
        digits = ""
        expected = []
        result = letter_combinations(digits)
        self.assertEqual(result, expected)

    def test_example3(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = letter_combinations(digits)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()