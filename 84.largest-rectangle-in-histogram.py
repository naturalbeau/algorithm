#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        pstack, hstack = [], []
        area = 0
        for i in range(len(heights)):
            lastwidth = inf
            while hstack and hstack[-1] > heights[i]:
                 lastwidth = pstack[-1]
                 carea = (i - pstack.pop())* hstack.pop()
                 area = max(area, carea)
            if not hstack or hstack[-1] < heights[i]:
                hstack.append(heights[i])
                pstack.append(min(lastwidth, i))
        return area
# @lc code=end

# brute force O(N^2)
# def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         res = 0
#         for i in range(n):
#             minh = height[i]
#             for j in range(i, n):
#                 minh = min(minh, height[j)
#                 res = max(res, minh * (j - i + 1))
#         return res
# two stack