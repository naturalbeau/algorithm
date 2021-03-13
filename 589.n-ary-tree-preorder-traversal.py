#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                for i in root.children[::-1]:
                    stack.append(i)
        return res

# @lc code=end

# recursive
#iterative
#  def preorder(self, root: 'Node') -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         self.res.append(root.val)
#         for i in  root.children:
#             self.helper(i)