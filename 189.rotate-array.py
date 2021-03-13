#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            pre = nums[-1]
            for j in range(len(nums)):
                pre, nums[j] = nums[j], pre
                 
# @lc code=end
#reverse O(N), O(1)
# construct O(N), O(1)
# pop and insert O(K), O(1) not sure it is ok
# rorate by NK times but LTE

# def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= len(nums)
#         self.reverse(nums, 0, len(nums) - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, len(nums) - 1)
#     def reverse(self, nums, start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1

#  def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
#         nums[:] = nums[n-k:] + nums[:n-k]

#    def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             nums.insert(0, nums.pop())