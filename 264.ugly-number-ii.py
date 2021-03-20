#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(res) < n:
            next2 = res[i2] * 2
            next3 = res[i3] * 3
            next5 = res[i5] * 5
            next = min(next2, next3, next5)
            if next == next2:
                i2 += 1
            if next == next3:
                i3 += 1
            if next == next5:
                i5 += 1
            res.append(next)
        return res[n-1]
# @lc code=end

