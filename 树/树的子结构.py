# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:return False
        def recur(A, B):
            # 匹配完成
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
