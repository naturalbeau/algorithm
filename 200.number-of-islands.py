#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                count += 1
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop()
                    grid[x][y] = '0'
                    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        newx = x + xx
                        newy = y + yy
                        if newx < 0 or newx >= m or newy < 0 or newy >= n or \
                            grid[newx][newy] == '0':
                            continue
                        queue.append((newx, newy))
        return count
                    
# @lc code=end
# 1. DFS O(M*N) O(1)
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     res = 0
    #     def helper(i, j):
    #         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
    #             return
    #         if grid[i][j] == '1':
    #             grid[i][j] = 0
    #             helper(i - 1, j)
    #             helper(i + 1, j)
    #             helper(i, j + 1)
    #             helper(i, j - 1)
    #         return 
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == '1':
    #                 helper(i, j)
    #                 res += 1
    #     return res
# 2. BFS O(M*N), O(min(M,N))
# 3. union find O(M*N), O(M*N)
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     parent = {x : x for x in range(m * n)}
    #     self.count = sum(1 for i in range(m) for j in range(n) if grid[i][j] == '1')
    #     def find(parent, x):
    #         while parent[x] != x:
    #             x = parent[x]
    #         return parent[x]
    #     def union(parent, x, y):
    #         p1 = find(parent, x)
    #         p2 = find(parent, y)
    #         if p1 != p2:
    #             parent[p1] = p2
    #             self.count -= 1
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '0':
    #                 continue
    #             index = i * n + j
    #             if j < n - 1 and grid[i][j + 1] == '1':
    #                 union(parent, index, index + 1)
    #             if i < m - 1 and grid[i + 1][j] == '1':
    #                 union(parent, index, index + n)
    #     return self.count
