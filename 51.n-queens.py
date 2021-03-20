#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def helper(current_state, xy_diff, xy_sum):
            row = len(current_state)
            if row == n:
                res.append(current_state)
                return
            for col in range(n):
                if col in current_state or row + col in xy_sum or row - col in xy_diff:
                    continue
                helper(current_state+[col], xy_diff + [row - col], xy_sum + [row + col])
        helper([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]


# @lc code=end
#backtrack
