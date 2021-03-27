#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < i:
                return False
            dp[i] = max(i+nums[i], dp[i-1])
        return dp[len(nums) - 1] >= len(nums) - 1
# @lc code=end

#1 Greedy O(N), O(1)
    # def canJump(self, nums: List[int]) -> bool:
    #     end = len(nums) - 1
    #     for i in range(len(nums)-1, -1, -1):
    #         if nums[i] + i >= end:
    #             end = i
    #     return end == 0
#2 DP O(N), O(N)