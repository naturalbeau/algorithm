#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num/x) // 2
        return x * x == num
# @lc code=end
# 1 . binary search O(logN)
# def isPerfectSquare(self, num: int) -> bool:
#         low = 0
#         high = num
#         while low <= high:
#             mid = low + (high - low) // 2
#             if mid * mid == num:
#                 return True
#             elif mid * mid > num:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return False

# 2 . newton method O(logN) O(1)
