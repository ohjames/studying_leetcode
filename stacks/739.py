''' 
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

# https://leetcode.com/problems/daily-temperatures/

import unittest

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result

class TestDailyTemperatures(unittest.TestCase):
    def test1(self):
        self.assertEqual(dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test2(self):
        self.assertEqual(dailyTemperatures([30,40,50,60]), [1,1,1,0])

    def test3(self):
        self.assertEqual(dailyTemperatures([30,60,90]), [1,1,0])

if __name__ == '__main__':
    unittest.main()