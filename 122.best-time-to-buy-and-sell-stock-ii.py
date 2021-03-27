#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy = float('-inf')
        cur_sold = 0
        for price in prices:
            pre_buy = cur_buy
            pre_sold = cur_sold
            cur_buy = max(pre_buy, pre_sold - price)
            cur_sold = max(pre_sold, pre_buy+ price)
        return cur_sold

# @lc code=end

# 1 Greedy O(N)
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] > prices[i - 1]:
    #             profit += prices[i] - prices[i - 1]
    #     return profit
# 2 DP O(N)