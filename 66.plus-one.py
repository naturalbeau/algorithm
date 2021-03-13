#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
# @lc code=end

#basic way
# early stop way

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     carry = 1
    #     for i in range(len(digits) - 1, -1, -1):
    #         newsum = digits[i] + carry
    #         carry = newsum // 10
    #         digits[i] = newsum % 10
    #     if carry == 1:
    #         digits.insert(0,  1)
    #     return digits