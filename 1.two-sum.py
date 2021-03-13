#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, v in enumerate(nums):
            com = target - v
            if com in maps:
                return [i, maps[com]]
            maps[v] = i
        return []
# @lc code=end

#brute force O(N^2) O(1)
# hashmap O(N)
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return  [i ,j]
#         return []