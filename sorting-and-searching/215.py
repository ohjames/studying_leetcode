'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# https://leetcode.com/problems/kth-largest-element-in-an-array/

import unittest

def findKthLargest(nums, k):
    def quick_select(nums, left, right, k):
        if left == right:
            return nums[left]
        pivot_index = partition(nums, left, right)
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quick_select(nums, left, pivot_index - 1, k)
        else:
            return quick_select(nums, pivot_index + 1, right, k)
    
    def partition(nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    return quick_select(nums, 0, len(nums) - 1, len(nums) - k)

class TestFindKthLargest(unittest.TestCase):
    def test1(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 2), 5)

    def test2(self):
        self.assertEqual(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)

if __name__ == '__main__':
    unittest.main()