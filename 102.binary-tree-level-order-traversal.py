#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = [root]
        while queue:
            level = []
            newqueue = []
            for node in queue:
                if node:
                    level.append(node.val)
                    newqueue.extend([node.left, node.right])
            if level:
                res.append(level)
            queue = newqueue
        return res
# @lc code=end

# 1 recursive
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     res = []
    #     def helper(root, level):
    #         if not root:
    #             return
    #         if level > len(res):
    #             res.append([])
    #         res[level - 1].append(root.val)
    #         helper(root.left, level + 1)
    #         helper(root.right, level + 1)
    #     helper(root, 1)
    #     return res
# 2 iterative