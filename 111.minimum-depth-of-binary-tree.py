#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = float('inf')
        while stack:
            root, level = stack.pop()
            if root and not root.left and not root.right:
                res = min(res, level)
            if root:
                stack.append((root.left, level + 1))
                stack.append((root.right, level + 1))
        return res

# @lc code=end

# recursive
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     if root.left and root.right:
    #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    #     else:
    #         return self.minDepth(root.left or root.right) + 1
# iterative