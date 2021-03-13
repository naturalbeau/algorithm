#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# @lc code=end

# sort
# hashmap

    # def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)/\