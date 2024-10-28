'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
'''

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import unittest
import heapq

# def kth_smallest(matrix, k):
#     def count_less_equal(x):
#         count, n = 0, len(matrix)
#         row, col = n - 1, 0
#         while row >= 0 and col < n:
#             if matrix[row][col] <= x:
#                 count += row + 1
#                 col += 1
#             else:
#                 row -= 1
#         return count

#     n = len(matrix)
#     left, right = matrix[0][0], matrix[n - 1][n - 1]
    
#     while left < right:
#         mid = (left + right) // 2
#         if count_less_equal(mid) < k:
#             left = mid + 1
#         else:
#             right = mid
    
#     return left

def kth_smallest(matrix, k): # time complexity is O(klogn) and space complexity is O(n)
    n = len(matrix)
    min_heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(min_heap)
    for _ in range(k):
        num, row, col = heapq.heappop(min_heap)
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    return num



class TestKthSmallestElementInASortedMatrix(unittest.TestCase):
    def test_example1(self):
        matrix = [[1,5,9],[10,11,13],[12,13,15]]
        k = 8
        expected = 13
        # Call the function that solves the problem
        result = kth_smallest(matrix, k)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        matrix = [[-5]]
        k = 1
        expected = -5
        # Call the function that solves the problem
        result = kth_smallest(matrix, k)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()