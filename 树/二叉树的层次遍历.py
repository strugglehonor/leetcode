# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root) :
        if not root:
            return []
        queue = []
        queue.append(root)
        L = []
        while queue:
            node = queue.pop(0)
            L.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return L