#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p1 = [0] * n
        p2 = [0] * n
        low = prices[0]
        high = prices[-1]
        res = 0
        for i in range(1, n):
            low = min(prices[i], low)
            p1[i] = max(prices[i] - low, p1[i - 1])
        for i in range(n-2, -1, -1):
            high = max(prices[i], high)
            p2[i] = max(high - prices[i], p2[i+1])
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res
# @lc code=end

#1. one pass O(N)
    # def maxProfit(self, prices: List[int]) -> int:
    #     cost1 = float('inf')
    #     cost2 = float('inf')
    #     profit1 = 0
    #     totalprofit = 0
    #     for price in prices:
    #         cost1 = min(cost1, price)
    #         profit1 = max(profit1, price-cost1)
    #         cost2 = min(cost2, price - profit1)
    #         totalprofit = max(totalprofit, price - cost2)
    #     return totalprofit
#2. two pass O(N)