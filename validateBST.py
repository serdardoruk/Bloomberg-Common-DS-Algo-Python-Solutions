def isValidBST(self, root):
    
    
    def validator(root, left, right):
        if not root:
            return True
        
        if root.val > right or root.val < left:
            return False

        return validator(root.left, left, root.val - 1) and validator(root.right , root.val + 1, right)
    
    return validator(root, float("-inf"), float("inf"))