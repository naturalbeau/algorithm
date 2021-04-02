#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        count = 0
        queue = []
        for i in range(n):
            if i not in visited:
                queue.append(i)
                while queue:
                    s = queue.pop(0)
                    visited.add(s)
                    for j in range(n):
                        if isConnected[s][j] == 1 and j not in visited:
                            queue.append(j)
                count += 1
        return count

 


# @lc code=end

# 1 DFS O(N^2)
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     res = 0
    #     n = len(isConnected)
    #     self.visited = set()
    #     for i in range(n):
    #         if i not in self.visited:
    #             res += 1
    #             self.dfs(isConnected, i)
    #     return res
        
    # def dfs(self, isConnected, i):
    #     for j in range(len(isConnected)):
    #         if isConnected[i][j] == 1 and j not in self.visited:
    #             self.visited.add(j)
    #             self.dfs(isConnected, j)

#2 disjoint set O(N^3)
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     def find(p, i):
    #         root = i
    #         while p[root] != root:
    #             root = p[root]
    #         return root
    #     n = len(isConnected)
    #     p = {x: x for x in range(n)}
    #     for i in range(n):
    #         for j in range(i, n):
    #             if isConnected[i][j] == 1 and p[i] != p[j]:
    #                 p1 = find(p, i)
    #                 p2 = find(p, j)
    #                 if p1 != p2:
    #                     p[p1] = p2
    #     return sum(1 for k, v in p.items() if k == v)

    #3 BFS O(N^2)