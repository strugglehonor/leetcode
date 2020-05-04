def deepSearch(root):
    if root == None:
        return 
    print(root)
    deepSearch(root.left)
    deepSearch(root.right)

