# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 前序遍历第一个节点是根节点，根据根节点的值找到这个值在中序遍历里面的索引，
    # 然后划分为左右子树，递归重复这个过程
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        # 这里是root.left，不是left
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1: ], inorder[mid+1: ])
        return root
