#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next
            first_node.next = second_node.next
            second_node.next = first_node
            pre_node.next = second_node
            pre_node = first_node
            head = first_node.next
        return dummy.next
# @lc code=end

#1 recursive
#2 iterative