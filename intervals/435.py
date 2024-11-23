'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''

# https://leetcode.com/problems/non-overlapping-intervals/

import unittest

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count

class TestEraseOverlapIntervals(unittest.TestCase):
    def test1(self):
        self.assertEqual(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)

    def test2(self):
        self.assertEqual(eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)

    def test3(self):
        self.assertEqual(eraseOverlapIntervals([[1,2],[2,3]]), 0)

if __name__ == '__main__':
    unittest.main()