'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

# https://leetcode.com/problems/permutations/

import unittest

def permute(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output

class TestPermutations(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,3]
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
        # Call the function that solves the problem
        result = permute(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [0,1]
        expected = [[0,1],[1,0]]
        # Call the function that solves the problem
        result = permute(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [1]
        expected = [[1]]
        # Call the function that solves the problem
        result = permute(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()