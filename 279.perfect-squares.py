#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        square = [i * i for i in range(1, int(sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            for k in square:
                if i >= k:
                    dp[i] = min(dp[i], dp[i-k] + 1)
        return dp[-1]
# @lc code=end

