#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stack = [(0, 0)]
        stones_set = set(stones)
        visited = set()
        while stack:
            stone, jump = stack.pop()
            for j in [jump - 1, jump, jump + 1]:
                s = stone + j
                if j > 0 and s in stones_set and (s, j) not in visited:
                    if s ==  stones[-1]:
                        return True
                    stack.append((s,j))
            visited.add((stone, jump))
        return False


# @lc code=end
# DFS  O(N), O(N)
