'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# https://leetcode.com/problems/contains-duplicate/

import unittest

def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

class TestContainsDuplicate(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 1]
        expected = True
        result = contains_duplicate(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [1, 2, 3, 4]
        expected = False
        result = contains_duplicate(nums)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        result = contains_duplicate(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()