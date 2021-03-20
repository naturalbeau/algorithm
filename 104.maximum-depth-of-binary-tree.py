#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            queue = []
            depth += 1
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue
        return depth

# @lc code=end

#1 recursive
# def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
#2 BFS

#3 iterative
# def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         depth = 0
#         stack = [(root, 1)]
#         while stack:
#             root, current_depth = stack.pop()
#             if root:
#                 depth = max(depth, current_depth)
#                 stack.append((root.right, current_depth + 1))
#                 stack.append((root.left, current_depth + 1))
#         return depth
