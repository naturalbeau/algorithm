#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parents = {x:x for x in range(n)}

    def find(self, x):
        while self.parents[x] != x:
            x = self.parents[x]
        return self.parents[x]

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        self.parents[p2] = p1

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        uf = UnionFind(m * n + 1)
        dummy = m * n 
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        uf.union(dummy, i * n + j)
                        continue
                    for x, y in [(0,1),(0, -1), (1, 0),(-1, 0)]:
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O': 
                            uf.union(i * n + j, nx * n + ny)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if uf.find(i*n+j) != uf.find(dummy):
                        board[i][j] = 'X'


                    
        
# @lc code=end

#1 DFS O(M*N) O(1)
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     m = len(board)
    #     n = len(board[0])
    #     def dfs(i ,j):
    #         if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
    #             board[i][j] = 'G'
    #             dfs(i + 1, j)
    #             dfs(i - 1, j)
    #             dfs(i, j - 1)
    #             dfs(i, j + 1)
    #     for i in range(n):
    #         dfs(0, i)
    #         dfs(m - 1, i)
    #     for i in range(m):
    #         dfs(i, 0)
    #         dfs(i, n - 1)
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 'O':
    #                 board[i][j] = 'X'
    #             elif board[i][j] == 'G':
    #                 board[i][j] = 'O'
#2 BFS O(MN), O(MN)
#    def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m = len(board)
#         n = len(board[0])
#         queue = collections.deque()
#         for i in range(m):
#             queue.extend([(i,0),(i, n-1)])
#         for j in range(n):
#             queue.extend([(0, j),(m-1,j)])
#         while queue:
#             x, y = queue.popleft()
#             if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != 'O':
#                 continue
#             board[x][y] = 'G'
#             queue.extend([(x, y+1),(x, y-1), (x+1, y), (x-1, y)])
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'G':
#                     board[i][j] = 'O'
#                 elif board[i][j] == 'O':
#                     board[i][j] = 'X'
#3 union find