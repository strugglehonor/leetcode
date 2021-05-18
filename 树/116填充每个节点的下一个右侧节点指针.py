class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        self.addTwoNode(root.left, root.right)
        return root
    def addTwoNode(self, node1, node2):
        if node1 == None or node2 == None:
            return
        # 把这两个节点连接起来
        node1.next = node2
        self.addTwoNode(node1.left, node1.right)
        self.addTwoNode(node2.left, node2.right)
        # 连接父节点不同的两个节点
        self.addTwoNode(node1.right, node2.left)
