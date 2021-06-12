class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if self.recur(root) == -1:
            return False
        else:
            return True
        
    def recur(self, root):
        # 返回值为-1，说明左子树不是平衡二叉树
        if root == None:
            return 0
        left = self.recur(root.left)
        if left == -1:
            return -1
        
        # 返回值为-1，说明右子树不是平衡二叉树
        right = self.recur(root.right)
        if right == -1:
            return -1
        
        # 是平衡二叉树，返回左右子树中较大高度的
        if abs(left-right) <= 1:
            return max(left, right)+1
        else:
            return -1
