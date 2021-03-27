#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(subset):
            if len(subset) == len(nums):
                res.append(subset)
                return
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                helper(subset+[nums[i]])

        helper([])
        return res
# @lc code=end

