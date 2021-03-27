#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        sx = -1
        sy = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    count += 1
                    sx = i
                    sy = j
        def helper(sx, sy, count):
            if sx < 0 or sy < 0 or sx == m or sy == n or \
                 grid[sx][sy] == -1:
                return 0
            if grid[sx][sy] == 2:
                return 1 if count == 0 else 0
            grid[sx][sy] = -1
            paths = helper(sx + 1, sy, count - 1) + \
                    helper(sx - 1, sy, count -1 ) + \
                    helper(sx, sy + 1, count - 1) + \
                    helper(sx, sy - 1, count - 1)
            grid[sx][sy] = 0
            return paths

        return helper(sx, sy, count)
# @lc code=end

# DFS time 4^NM, space O(M*N)