#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)
        res = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if self.helper(mid, nums, m):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res
    def helper(self, target, nums, m):
        groups = 1
        arraySum = 0
        for num in nums:
            if num + arraySum <= target:
                arraySum += num
            else:
                groups += 1
                arraySum = num
        return groups <= m

# @lc code=end

#1 DP TLE O(MN^2) O(MN)
# def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         dp = [[float('inf')] * n for _ in range(m+1)]
#         sums = [0] * n
#         sums[0] = nums[0]
#         for i in range(1, n):
#             sums[i] = sums[i-1] + nums[i]
#         for i in range(n):
#             dp[1][i] = sums[i]
#         for i in range(2, m+1):
#             for j in range(i-1, n):
#                 for k in range(j):
#                     dp[i][j] = min(dp[i][j], max(dp[i-1][k], sums[j] - sums[k]))
#         return dp[-1][-1]

#2 binary search  O(Nlog(sumofArray))