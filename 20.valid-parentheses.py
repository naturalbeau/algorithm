#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {']':'[', '}':'{', ')':'('}
        for char in s:
            if char not in maps:
                stack.append(char)
            else:
                if not stack or stack.pop() != maps[char]:
                    return False
        return stack == []

        
# @lc code=end

#replace method
# hashmap O(N) time, O(N) space

    # def isValid(self, s: str) -> bool:
    #     while '()' in s or '[]' in s or '{}' in s:
    #         s = s.replace('()','').replace('[]','').replace('{}','')
    #     return s == ''