#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        current = head
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre
# @lc code=end

# iterative

# recursive 
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     p = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return p