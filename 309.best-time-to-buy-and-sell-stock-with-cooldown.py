#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        rest = 0
        hold = float('-inf')
        for price in prices:
            pre_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, pre_sold) 
        return max(sold, rest)
# @lc code=end

# DP O(N) O(1)