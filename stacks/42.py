'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

# https://leetcode.com/problems/trapping-rain-water/

import unittest

def trap(height):
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    result = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                result += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                result += right_max - height[right]
            right -= 1
    return result

class TestTrap(unittest.TestCase):
    def test1(self):
        self.assertEqual(trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def test2(self):
        self.assertEqual(trap([4,2,0,3,2,5]), 9)

if __name__ == '__main__':
    unittest.main()