#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        start = 0
        end = 0
        target_len = len(t)
        target_count = collections.Counter(t)
        for end in range(len(s)):
            if target_count[s[end]] > 0:
                target_len -= 1
            target_count[s[end]] -= 1
            while target_len == 0:
                window_len = end - start + 1
                if not res or window_len < len(res):
                    res = s[start: end+1]
                
                target_count[s[start]] += 1
                if target_count[s[start]] > 0:
                    target_len += 1
                start += 1
        return res
# @lc code=end

# sliding winodw, 2 pointers, hashmap O(s+t) O(s+t)