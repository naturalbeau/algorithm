#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
# @lc code=end

# binary search O(logN)