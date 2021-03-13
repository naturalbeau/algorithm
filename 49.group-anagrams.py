#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            key = tuple(sorted(word))
            maps[key] = maps.get(key, []) + [word]
        return maps.values()
# @lc code=end

#hashmap
