#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(l, r):
            if l + 1 >= r:
                return min(nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r - l) // 2
            return min(helper(l, mid), helper(mid+1, r))
        return helper(0 ,len(nums) - 1)
# @lc code=end

# one pass O(N)
# sort O(NlogN)
# 1. binary search O(logN)
# def findMin(self, nums: List[int]) -> int:
#         l = 0
#         r = len(nums) - 1
#         while l < r:
#             mid = l + (r - l) // 2
#             if nums[mid] < nums[r]:
#                 r = mid
#             else:
#                 l = mid + 1
#         return nums[l]
# 2. diver and conquer O(logN)