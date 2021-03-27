#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def helper(l, r):
            ans = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                ans += 1
                l -= 1
                r += 1
            return ans
        for i in range(len(s)):
            res += helper(i, i)
            res += helper(i, i+1)
        return res
# @lc code=end

#1 O(N^2)