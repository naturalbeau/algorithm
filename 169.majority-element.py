#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(low, high):
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            left = helper(low, mid)
            right = helper(mid + 1, high)
            if left == right:
                return left
            left_count = sum(1 for i in range(low, mid+1) if nums[i] == left)
            right_count = sum(1 for i in range(mid+1, high+1) if nums[i] == right)
            return left if left_count > right_count else right 
        return helper(0, len(nums) - 1)




        # @lc code=end

# 1.sort O(NlogN) O(1)
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return nums[len(nums)//2]

# 2.hashmap O(N), O(N)
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         freq = Counter(nums)
#         return max(freq.keys(), key=freq.get)
# 3.counting O(N),O(1)
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 0
    #     candidate = nums[0]
    #     for n in nums:
    #         if n == candidate:
    #             count += 1
    #         else:
    #             count -= 1
    #             if count == 0:
    #                 candidate = n
    #                 count = 1
    #     return candidate
# 4.diver and conquer