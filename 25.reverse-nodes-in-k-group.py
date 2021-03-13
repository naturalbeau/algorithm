#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        pre = dummy
        dummy.next = head
        current = head
        while current:
            tail = current
            index = 0
            while index < k and current:
                index += 1
                current = current.next
            if index != k:
                pre.next = tail
            else:
                pre.next = self.reverseLinkedList(tail, k)
                pre = tail
        return dummy.next

    def reverseLinkedList(self, head, k):
        pre = None
        while k:
            tempNext = head.next
            head.next = pre
            pre = head
            head = tempNext
            k -= 1
        return pre 


        
# @lc code=end

