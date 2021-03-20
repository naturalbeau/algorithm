#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def helper(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == '1':
                grid[i][j] = 0
                helper(i - 1, j)
                helper(i + 1, j)
                helper(i, j + 1)
                helper(i, j - 1)
            return 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    helper(i, j)
                    res += 1
        return res
# @lc code=end
# recursive
