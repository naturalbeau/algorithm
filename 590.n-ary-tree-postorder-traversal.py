#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                for i in root.children:
                    stack.append(i)
        return res[::-1]


# @lc code=end

#recursive
#iterative

# def postorder(self, root: 'Node') -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         for i in root.children:
#             self.helper(i)
#         self.res.append(root.val)
        