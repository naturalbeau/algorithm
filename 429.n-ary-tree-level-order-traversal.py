#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res = []
        self.helper(root, 1)
        return self.res

    def helper(self, root, level):
        if not root:
            return
        if len(self.res) < level:
            self.res.append([])
        self.res[level-1].append(root.val)
        for child in root.children:
            self.helper(child, level+1)
            
# @lc code=end

#recursive
#iterative
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     if not root:
    #         return []
    #     res = []
    #     queue = [root]
    #     while queue:
    #         level = []
    #         for i in range(len(queue)):
    #             node = queue.pop(0)
    #             level.append(node.val)
    #             for child in node.children:
    #                 queue.append(child)
    #         res.append(level)
    #     return res