#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            res.append(count)
        return res
        
# @lc code=end

