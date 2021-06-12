class Solution:
    def Mirror(self , pRoot):
        # write code here
        if pRoot == None:
            return pRoot
        
        tmp = pRoot.left 
        pRoot.left = pRoot.right
        pRoot.right = tmp
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot
