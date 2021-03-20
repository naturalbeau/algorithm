#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax < rmax:
                res += lmax - height[l]
                lmax = max(lmax, height[l+1])
                l += 1
            else:
                res += rmax - height[r]
                rmax = max(rmax, height[r - 1])
                r -= 1
        return res 

# @lc code=end

# brute force O(N^2) O(1)
# def trap(self, height: List[int]) -> int:
#         res = 0
#         n = len(height)
#         for i in range(n ):
#             lmax = max(height[: i+1])
#             rmax = max(height[i :])
#             res += min(lmax, rmax) - height[i]
#         return res
# dp O(N) O(N)
# def trap(self, height: List[int]) -> int:
#         res = 0
#         n = len(height)
#         if n == 0:
#             return 0
#         l = [0] * n
#         r = [0] * n
#         for i in range(n):
#             if i == 0:
#                 l[i] = height[i]
#             else:
#                 l[i] = max(l[i-1], height[i])
#         for i in range(n-1,-1,-1):
#             if i == n-1:
#                 r[i] = height[i]
#             else:
#                 r[i] = max(r[i+1],height[i])
#         for i in range(n):
#             res += min(l[i],r[i]) - height[i]
#         return res


# two pointer O(N), O(1)