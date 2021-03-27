#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        res = float('-inf')
        for i in range(len(nums)):
            pre = max(pre+nums[i], nums[i])
            res = max(res, pre)
        return res
# @lc code=end

#1. brute force O(n^2) two loop  TLE
    #  def maxSubArray(self, nums: List[int]) -> int:
    #     res = nums[0]
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             res = max(res, sum(nums[i:j+1]))
    #     return res
#2 DP O(N), O(N)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     dp = [float('-inf')] * len(nums)
    #     dp[0] = nums[0]
    #     for i in range(1, len(nums)):
    #         dp[i] = max(dp[i-1]+nums[i], nums[i])
    #     return max(dp)

# 3 DP O(N), O(1)