#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        nmax = nums[0]
        nmin = nums[0]
        for i in range(1, len(nums)):
            nmax, nmin = max(nmax * nums[i], nmin*nums[i], nums[i]), min(
                nmax * nums[i], nmin*nums[i], nums[i])
            res = max(res, nmax)
        return res
# @lc code=end

# 1 DP O(N) O(N)
    # def maxProduct(self, nums: List[int]) -> int:
    #     dp = [[0, 0] for _ in range(len(nums))]
    #     dp[0] = [nums[0], nums[0]]
    #     res = nums[0]
    #     for i in range(1, len(nums)):
    #         dp[i][0] = max(dp[i-1][0] * nums[i], dp[i-1][1]*nums[i], nums[i])
    #         dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1]*nums[i], nums[i])
    #         res = max(res, dp[i][0])
    #     return res
# 2 Dp O(N) O(1)