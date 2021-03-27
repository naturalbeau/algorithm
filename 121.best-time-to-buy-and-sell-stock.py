#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minx = float('inf')
        for i in range(len(prices)):
            minx = min(prices[i], minx)
            res = max(res, prices[i] - minx)
        return res
# @lc code=end

# 1. brute force O(n^2)
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             res = max(res, prices[j] - prices[i])
    #     return res
# 2. one pass O(n)
   