#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or not prices:
            return 0
        if k >= len(prices) // 2:
            totalProfit = 0
            for i in range(1, len(prices)):
                totalProfit += max(0, prices[i] - prices[i-1])
            return totalProfit
        dp = [[0] * len(prices) for i in range(k + 1)]
        for i in range(1, k+1):
            maxPreProfit = 0
            minCost = prices[0]
            for j in range(len(prices)):
                maxPreProfit = max(maxPreProfit, dp[i-1][j])
                minCost = min(minCost, prices[j] - maxPreProfit)
                dp[i][j] = max(dp[i][j-1], prices[j] - minCost)
        return dp[k][-1]
# @lc code=end

# DP O(kM)