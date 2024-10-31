'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import unittest

def findMedianSortedArrays(nums1, nums2):
    def findKthElement(nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2
        if mid1 + mid2 < k:
            if nums1[mid1] > nums2[mid2]:
                return findKthElement(nums1, nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return findKthElement(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return findKthElement(nums1[:mid1], nums2, k)
            else:
                return findKthElement(nums1, nums2[:mid2], k)

    total_length = len(nums1) + len(nums2)
    if total_length % 2 == 0:
        return (findKthElement(nums1, nums2, total_length // 2 - 1) + findKthElement(nums1, nums2, total_length // 2)) / 2
    else:
        return findKthElement(nums1, nums2, total_length // 2)
    
class TestFindMedianSortedArrays(unittest.TestCase):
    def test1(self):
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2.00000)

    def test2(self):
        self.assertEqual(findMedianSortedArrays([1,2], [3,4]), 2.50000)

if __name__ == '__main__':
    unittest.main()