'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

# https://leetcode.com/problems/subsets/

import unittest

def subsets(nums):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    result = []
    backtrack(0, [])
    return result


class TestSubsets(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3]
        expected = [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
        # Call the function that solves the problem
        result = subsets(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [0]
        expected = [[],[0]]
        # Call the function that solves the problem
        result = subsets(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__': 
    unittest.main()