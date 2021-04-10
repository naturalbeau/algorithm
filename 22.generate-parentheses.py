#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range( n + 1)]
        dp[0] = ['']
        for i in range(n+1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

# @lc code=end

# dp[0] = ['']
# dp[1] = ['()']
# dp[2]=['(())','()()'] i =3, j =0,1,2
# dp[3]=['()(())','()()()','(())()','(())()','(()())'] dp[3] += dp[0] , dp[2]
#                                     dp[1] dp[1]
#                                     dp[2], dp[0]
# 1. DFS recursive O(2^N)
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

# 2. iterative with stack
# def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         stack = [('(', 1, 0)]
#         while stack:
#             s, l, r = stack.pop(0)
#             if l == r and l == n:
#                 res.append(s)
#                 continue
#             if l < n:
#                 stack.append((s + '(', l + 1, r))
#             if l > r:
#                 stack.append((s + ')', l, r + 1))
#         return res
#3 DP


