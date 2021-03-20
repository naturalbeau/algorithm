#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, temp, index):
            res.append(temp[:])
            for i in range(index, len(nums)):
                #temp.append(nums[i])
                dfs(nums, temp+[nums[i]], i + 1)
                #temp.pop()
        dfs(nums, [], 0)
        return res

# @lc code=end

# iterative
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for i in nums:
    #         newset = [subset + [i] for subset in res]
    #         res.extend(newset)
    #     return res

# recursive