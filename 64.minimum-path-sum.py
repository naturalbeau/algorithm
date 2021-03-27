#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * n 
        dp[0] = 0
        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
# @lc code=end

#1 DP 2D
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     dp = [[float('inf')] * n for _ in range(m)]
    #     dp[0][0] = grid[0][0]
    #     for i in range(m):
    #         for j in range(n):
    #             if i >= 0:
    #                 dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
    #             if j >= 0:
    #                 dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    #     return dp[-1][-1]
#2 DP 1D