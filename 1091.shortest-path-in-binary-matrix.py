#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        queue = collections.deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            i, j, path = queue.popleft()
            if i == n-1 and j == n-1:
                return path
            for x, y in directions:
                if 0 <= i+x < n and 0 <= j+y < n and grid[i+x][j+y] == 0:
                    grid[i+x][j+y] = 1
                    queue.append((i+x,j+y, path+1))
        return -1

# @lc code=end

