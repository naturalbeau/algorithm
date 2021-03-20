#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [('(', 1, 0)]
        while stack:
            s, l, r = stack.pop(0)
            if l == r and l == n:
                res.append(s)
                continue
            if l < n:
                stack.append((s + '(', l + 1, r))
            if l > r:
                stack.append((s + ')', l, r + 1))
        return res
# @lc code=end

# DFS recursive O(2^N)
    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []
    #     def helper(left, right, s):
    #         if left == right and left == n:
    #             res.append(s)
    #             return
    #         if left < n:
    #             helper(left + 1, right, s + '(')
    #         if left > right:
    #             helper(left, right + 1, s + ')')
    #     helper(0, 0, '')
    #     return res

# iterative with stack