def flatten(root):
    
    if not root:
        return
    if not root.left and not root.right:
        return root
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            stack.append(cur.right)
            stack.append(cur.left)
            root.right = cur
            root.left = None
            root = root.right