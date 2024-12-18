'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
'''

# https://leetcode.com/problems/meeting-rooms/

import unittest

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

class TestCanAttendMeetings(unittest.TestCase):
    def test1(self):
        self.assertEqual(canAttendMeetings([[0,30],[5,10],[15,20]]), False)

    def test2(self):
        self.assertEqual(canAttendMeetings([[7,10],[2,4]]), True)

if __name__ == '__main__':
    unittest.main()