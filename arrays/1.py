'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

# Link: https://leetcode.com/problems/two-sum/

import unittest

def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
            
# def two_sum(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        # Call the function that solves the problem
        result = two_sum(nums, target)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        # Call the function that solves the problem
        result = two_sum(nums, target)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        # Call the function that solves the problem
        result = two_sum(nums, target)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()