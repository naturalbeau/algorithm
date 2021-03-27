#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = [([], 1)]
        while stack:
            subset, index = stack.pop()
            if len(subset) == k:
                res.append(subset)
            else:
                for i in range(n, index-1, -1):
                    stack.append((subset+[i], i+1))
        return res
# @lc code=end

# DFS
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     res = []
    #     def helper(subset, index):
    #         if len(subset) == k:
    #             res.append(subset)
    #             return
    #         for i in range(index, n+1):
    #             helper(subset+[i], i+1)
    #     helper([], 1)
    #     return res
# iterative