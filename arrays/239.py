'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

# https://leetcode.com/problems/sliding-window-maximum/

import unittest

def max_sliding_window(nums, k):
    if not nums:
        return []
    if k == 1:
        return nums
    result = []
    deque = []
    for i in range(len(nums)):
        while deque and nums[i] > nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
            if deque[0] == i - k + 1:
                deque.pop(0)
    return result

class TestMaxSlidingWindow(unittest.TestCase):
    def test_example1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        result = max_sliding_window(nums, k)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [1]
        k = 1
        expected = [1]
        result = max_sliding_window(nums, k)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()