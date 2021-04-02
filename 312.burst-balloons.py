#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for k in range(left+1, right):
                    dp[left][right] = max(dp[left][right],
                                        nums[left]*nums[k]* nums[right]+ dp[left][k]+dp[k][right])
        return dp[0][n-1]
# @lc code=end

# O(N^3) O(N^2)