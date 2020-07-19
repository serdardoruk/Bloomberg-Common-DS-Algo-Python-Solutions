'''


'''


def levelOrder(root):
    if not root:
        return
    
    queue = [root]
    levels = []
    
    while queue:
        newQueue = []
        level = []
        for node in queue:
            level.append(node.val)
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
        levels.append(level)
        queue = newQueue
    return levels