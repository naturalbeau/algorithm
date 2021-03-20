#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
# @lc code=end
# 1.newton method
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r * r > x:
    #         r = (r + x/r)//2
    #     return int(r)
# 2. Binary search
