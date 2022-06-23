"""
Approach: 2 pointers
Use two pointers, keep low pointer at 1st index, and keep moving high pointer
from 2nd index onward, at each step calculating profit. If profit is more that
maxProfit so far, update the maxProfit.
If at any point prices[h] < prices[l], then only update the low pointer to high
as we have found new minimum.

TC: O(n)
SC: O(1)
Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,h = 0, 1  # buy,sell pointers
        maxP = 0 # maxProfit
        while h < len(prices):
            if prices[l] < prices[h]:
                profit = prices[h] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = h
            h += 1
        return maxP