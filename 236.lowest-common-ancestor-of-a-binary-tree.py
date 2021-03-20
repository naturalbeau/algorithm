#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        queue = [root]
        while p not in parents or q not in parents:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node
        lca = set()
        while p:
            lca.add(p)
            p = parents[p]
        while q not in lca:
            q = parents[q]
        return q
# @lc code=end

#1 recurisve
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return root
    #     if p == root or q == root:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if left and right:
    #         return root
    #     return left if left else right
#2 iterative using parents map