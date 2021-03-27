#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                length = i - stack[-1]        
                res = max(res, length)
        return res
# @lc code=end

# 1 DP O(N) O(N)
    # def longestValidParentheses(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     dp = [0] * len(s)
    #     for i in range(len(s)):
    #         if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
    #             dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
    #     return max(dp)
#2 stack O(N), O(N)

#3 bidirection pass O(N)
    # def longestValidParentheses(self, s: str) -> int:
    #     left = 0
    #     right = 0
    #     res = 0
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             left += 1
    #         elif s[i] == ')':
    #             right += 1
    #         if right == left:
    #             res = max(res, right * 2)
    #         elif right > left:
    #             right = 0
    #             left = 0
    #     left = 0
    #     right = 0
    #     for i in range(len(s)-1, -1, -1):
    #         if s[i] == '(':
    #             left += 1
    #         elif s[i] == ')':
    #             right += 1
    #         if right == left:
    #             res = max(res, right * 2)
    #         elif left > right:
    #             right = 0
    #             left = 0
    #     return res