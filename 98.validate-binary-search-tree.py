#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return None
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            if root.val >= high or root.val <= low:
                return False
            stack.append((root.left, low, root.val))
            stack.append((root.right, root.val, high))
        return True
# @lc code=end

# 1. iterative inorder traverse
    # def isValidBST(self, root: TreeNode) -> bool:
    #     stack = []
    #     pre = -float('inf')
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         if pre >= root.val:
    #             return False
    #         pre = root.val
    #         root = root.right
    #     return True

# 2. recursive inorder traverse
    # def isValidBST(self, root: TreeNode) -> bool:
    #     self.prev = float('-inf')
    #     return self.helper(root)

    # def helper(self, root):
    #     if not root:
    #         return True
    #     if not self.helper(root.left):
    #         return False
    #     if self.prev >= root.val:
    #         return False
    #     self.prev = root.val
    #     return self.helper(root.right)

# 3. iterative range compare

# 4. recursive range compage
    #  def isValidBST(self, root: TreeNode) -> bool:
    #     return self.helper(root, float('-inf'), float('inf'))

    # def helper(self, root, low, high):
    #     if not root:
    #         return True
    #     if root.val <= low or root.val >= high:
    #         return False
    #     return self.helper(root.left, low, root.val) and\
    #          self.helper(root.right,  root.val, high)