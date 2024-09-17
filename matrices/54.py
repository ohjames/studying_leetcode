'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

1 -> 2 -> 3
          |
4 -> 5    6
|         |
7 <- 8 <- 9

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

1 -> 2 -> 3 ->   4
                 |
5 -> 6 -> 7      8
|                |
9 <- 10 <- 11 <- 12

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

# https://leetcode.com/problems/spiral-matrix/

import unittest

def spiral_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, cols - 1, 0, rows - 1
    result = []
    while left <= right and top <= bottom:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])
        if left < right and top < bottom:
            for j in range(right - 1, left, -1):
                result.append(matrix[bottom][j])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return result

class TestSpiralMatrix(unittest.TestCase):
    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        # Call the function that solves the problem
        result = spiral_order(matrix)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        # Call the function that solves the problem
        result = spiral_order(matrix)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()