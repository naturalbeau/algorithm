#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 3
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2 # P,L
        dp[2] = 4# PP, LL, PL, LP
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%mod
        res = dp[n]
        for i in range(1, n+1):
            res += (dp[i-1] * dp[n-i]) % mod
        return res%mod
# @lc code=end

#DP
# without A end with  P , PL, PLL
# with A, *** A *****
# O(N), O(N)