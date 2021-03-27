#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] *  (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for k in coins:
                if i >= k:
                    dp[i] = min(dp[i], dp[i - k] + 1)
        return dp[amount] if dp[amount] <= amount else -1
# @lc code=end

