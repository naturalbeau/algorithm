#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r - l)* min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
# @lc code=end

