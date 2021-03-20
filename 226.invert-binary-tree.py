#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

# @lc code=end

# recursively O(N)
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return None
    #     root.left, root.right = root.right, root.left
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     return root
# BFS

# DFS
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             stack.append(node.right)
    #             stack.append(node.left)
    #     return root