'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

# https://leetcode.com/problems/product-of-array-except-self/

import unittest

def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    left = 1
    right = 1
    for i in range(n):
        output[i] *= left
        left *= nums[i]
        output[n - 1 - i] *= right
        right *= nums[n - 1 - i]
    return output

class TestProductExceptSelf(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        # Call the function that solves the problem
        result = product_except_self(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        # Call the function that solves the problem
        result = product_except_self(nums)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
