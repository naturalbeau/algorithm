#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return res

# @lc code=end

#iteratively
#recursive
# def preorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         self.res.append(root.val)
#         self.helper(root.left)
#         self.helper(root.right)