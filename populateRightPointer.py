'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Populating Next Right Pointers in Each Node
Medium

1862

137

Add to List

Share
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root

        leftmost = root

        while leftmost.left:

            head = leftmost
            while head:

                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left
        
        return root 