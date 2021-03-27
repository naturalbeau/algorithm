#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0] * (n + 1) for _ in range(m+1)]  # max size that can achieve at x,y as bottom right
        for i in range(1, m+1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j]*dp[i][j])
        return res
# @lc code=end
# O(MN), O(MN)

