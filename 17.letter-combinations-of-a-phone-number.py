#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {'1':'',
                '2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        def helper(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return [i for i in maps[digits]]
            prev = helper(digits[:-1])
            last = [i for i in maps[digits[-1]]]
            return [p + l for p in prev for l in last]
        return helper(digits)
# @lc code=end
#1. recursive
#2. iterative
    # def letterCombinations(self, digits: str) -> List[str]:
    #     maps = {'1':'',
    #             '2':'abc',
    #             '3':'def',
    #             '4':'ghi',
    #             '5':'jkl',
    #             '6':'mno',
    #             '7':'pqrs',
    #             '8':'tuv',
    #             '9':'wxyz'}
    #     if not digits:
    #         return []
    #     res = ['']
    #     for n in digits:
    #         level = []
    #         for subset in res:
    #             level.extend([subset+i for i in maps[n]])
    #         res = level
    #     return res
