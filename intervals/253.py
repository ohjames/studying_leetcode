'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
'''

# https://leetcode.com/problems/meeting-rooms-ii/

import unittest
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)

class TestMinMeetingRooms(unittest.TestCase):
    def test1(self):
        self.assertEqual(minMeetingRooms([[0,30],[5,10],[15,20]]), 2)

    def test2(self):
        self.assertEqual(minMeetingRooms([[7,10],[2,4]]), 1)

if __name__ == '__main__':
    unittest.main()