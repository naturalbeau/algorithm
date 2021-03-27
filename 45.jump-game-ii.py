#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                continue
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[-1]
# @lc code=end
# 1. greedy O(N) O(1)
# def jump(self, nums: List[int]) -> int:
#         start = 0 
#         step = 0
#         end = 0
#         maxend = 0
#         n = len(nums)
#         while end < n - 1:
#             step += 1
#             for i in range(start, end + 1):
#                 if i + nums[i] >= n - 1:
#                     return step
#                 maxend = max(maxend, i + nums[i])
#             start = end + 1
#             end = maxend
#         return step
# 2.DP O(N^2),O(N)