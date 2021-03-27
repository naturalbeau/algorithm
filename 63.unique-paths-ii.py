#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]
        return dp[n - 1]

# @lc code=end

#1. DP O(MN), O(MN)
# def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[0] *  n for _ in range(m)]
#         if obstacleGrid[0][0] == 0:
#             dp[0][0] = 1
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     if i > 0:
#                         dp[i][j] += dp[i - 1][j]
#                     if j > 0:
#                         dp[i][j] += dp[i][j - 1]
#         return dp[m - 1][n - 1]
#2 DP O(MN), O(N) 