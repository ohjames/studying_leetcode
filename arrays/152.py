'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

# https://leetcode.com/problems/maximum-product-subarray/

import unittest

def max_product_subarray(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)
    return result

class TestMaximumProductSubarray(unittest.TestCase):
    def test_example1(self):
        nums = [2, 3, -2, 4]
        expected = 6
        result = max_product_subarray(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [-2, 0, -1]
        expected = 0
        result = max_product_subarray(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()