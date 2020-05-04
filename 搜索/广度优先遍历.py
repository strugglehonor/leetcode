def widthSearch(root):
    queue = []
    queue.append(root)
    while queue:
        print(queue.pop(0))
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)
