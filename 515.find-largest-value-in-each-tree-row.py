#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root, level):
            if not root:
                return
            if level > len(res):
                res.append(float('-inf'))
            res[level - 1] = max(res[level - 1], root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        helper(root, 1)
        return res

# @lc code=end

# BFS
# def largestValues(self, root: TreeNode) -> List[int]:
#         res = []
#         queue = [root]
#         while queue:
#             maxv = float('-inf')
#             level = []
#             for node in queue:
#                 if node:
#                     maxv = max(maxv, node.val)
#                     level.extend([node.left, node.right])
#             queue = level
#             if maxv != float('-inf'):
#                 res.append(maxv)
#         return res
# DFS preorder
