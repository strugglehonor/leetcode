class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(level)
        return res
