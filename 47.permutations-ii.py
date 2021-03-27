#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def helper(subset):
            if len(subset) == len(nums):
                res.append(subset)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and used[i-1]:
                    continue
                used[i] = True
                helper(subset+[nums[i]])
                used[i] = False
        helper([])
        return res
# @lc code=end

