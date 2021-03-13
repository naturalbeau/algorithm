#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
# @lc code=end
# recursive
#iteratively
# def inorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         self.helper(root.left)
#         self.res.append(root.val)
#         self.helper(root.right)
