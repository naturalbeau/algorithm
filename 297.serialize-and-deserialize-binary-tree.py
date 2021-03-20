#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(res)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        root_val = data_list.pop(0)
        if root_val == '#':
            return None
        root = TreeNode(root_val)
        queue = [root]
        while queue:
            node = queue.pop(0)
            left_val = data_list.pop(0)
            right_val = data_list.pop(0)
            if left_val != '#':
                node.left = TreeNode(str(left_val))
                queue.append(node.left)
            if right_val != '#':
                node.right = TreeNode(str(right_val))
                queue.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

# preorder DFS recursive traverse
#  def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []
#         def helper(root):
#             if not root:
#                 res.append('#')
#                 return
#             res.append(str(root.val))
#             helper(root.left)
#             helper(root.right)
#         helper(root)
#         return ','.join(res)
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         def helper(data):
#             node_val = data.pop(0)
#             if node_val == '#':
#                 return None
#             root = TreeNode(node_val)
#             root.left = helper(data)
#             root.right = helper(data)
#             return root
#         data_list = data.split(',')
#         return helper(data_list)

# BFS iterative traverse

