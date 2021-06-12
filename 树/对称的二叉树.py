class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.recur(root.left, root.right)
    def recur(self, rootA, rootB):
        if rootA == None and rootB == None:
            return True
        if rootA == None or rootB == None:
            return False
        if rootA.val != rootB.val:
            return False
        return self.recur(rootA.left, rootB.right) and self.recur(rootA.right, rootB.left)
