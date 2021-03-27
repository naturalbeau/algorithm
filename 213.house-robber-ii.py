#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        def helper(l, r):
            first, second = 0, 0
            for i in range(l, r+1):
                third = max(first + nums[i], second)
                first = second
                second = third
            return second
        return max(helper(0, m-2), helper(1, m-1))
# @lc code=end

#DP O(N) ,O(1), break into two no cycle problem
#  def rob(self, nums: List[int]) -> int:
#         m = len(nums)
#         if m == 0:
#             return 0
#         if m == 1:
#             return nums[0]
#         def helper(nums):
#             first, second = 0, 0
#             for i in range(len(nums)):
#                 third = max(first + nums[i], second)
#                 first = second
#                 second = third
#             return second
#         return max(helper(nums[:-1]), helper(nums[1:]))