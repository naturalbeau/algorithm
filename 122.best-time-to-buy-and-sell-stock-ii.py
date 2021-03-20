#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold = float('-inf')
        cur_not_hold = 0
        for price in prices:
            pre_hold = cur_hold
            pre_not_hold = cur_not_hold
            cur_hold = max(pre_hold, pre_not_hold - price)
            cur_not_hold = max(pre_not_hold, pre_hold + price)
        return cur_not_hold

# @lc code=end

# 1 Greedy O(N)
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] > prices[i - 1]:
    #             profit += prices[i] - prices[i - 1]
    #     return profit
# 2 DP O(N)