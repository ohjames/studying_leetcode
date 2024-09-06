'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import unittest

def max_profit(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit

class TestMaxProfit(unittest.TestCase):
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        # Call the function that solves the problem
        result = max_profit(prices)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        # Call the function that solves the problem
        result = max_profit(prices)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()