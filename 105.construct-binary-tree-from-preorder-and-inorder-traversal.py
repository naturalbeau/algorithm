#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preStart, inStart, inEnd):
            if preStart > len(preorder) - 1 or inEnd < inStart:
                return None
            root = TreeNode(preorder[preStart])
            index = inorder.index(root.val)
            root.left = helper(preStart+1, inStart, index - 1)
            root.right = helper(preStart + 1 + index - inStart, index + 1, inEnd)
            return root
        return helper(0, 0, len(preorder) - 1)
# @lc code=end

# 1. recursive
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if inorder:
    #         index = inorder.index(preorder.pop(0))
    #         root = TreeNode(inorder[index])
    #         root.left = self.buildTree(preorder, inorder[:index])
    #         root.right = self.buildTree(preorder, inorder[index+1:])
    #         return root
# 2. recursive more details

