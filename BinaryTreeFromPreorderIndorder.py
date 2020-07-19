'''
Construct Binary Tree from Preorder and Inorder Traversal
Medium

3203

92

Add to List

Share
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indices = { val : idx for idx, val in enumerate(inorder)}
        cur = 0
        
        def rec(left, right):
            nonlocal  cur
            if left == right:
                return 
            
            rootVal = preorder[cur]
            root = TreeNode(rootVal)
            
            bound = indices[rootVal]
            
            cur += 1
            
            root.left = rec(left, bound)
            root.right = rec(bound + 1, right)
            
            return root
        
        return rec(0, len(preorder))