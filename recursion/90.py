'''
Given an integer array nums that may contain duplicates, return all possible subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

# https://leetcode.com/problems/subsets-ii/

import unittest

def subsets_with_duplicates(nums):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            backtrack(i + 1, path + [nums[i]])
    
    result = []
    nums.sort()
    backtrack(0, [])
    return result

class TestSubsetsWithDuplicates(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 2]
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        result = subsets_with_duplicates(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [0]
        expected = [[], [0]]
        result = subsets_with_duplicates(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()