class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        depth = 0
        self.dfs(root, res, depth)
        return res

    def dfs(self, root, array, depth):
        if root == None:
            return 
        if depth == len(array):
            array.append(root.val)
        depth += 1
        self.dfs(root.right, array, depth)
        self.dfs(root.left, array, depth)
        
