#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def dfs(current_states, xy_sum, xy_diff):
            row = len(current_states)
            if row == n:
                self.res += 1
                return
            for col in range(n):
                if col in current_states or row+col in xy_sum or row-col in xy_diff:
                    continue
                dfs(current_states+[col], xy_sum+[row+col], xy_diff+[row-col])
        dfs([],[],[])
        return self.res
# @lc code=end

