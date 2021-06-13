class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val, None, None)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
