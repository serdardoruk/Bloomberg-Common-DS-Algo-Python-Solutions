'''
 Add Two Numbers II
 https://leetcode.com/problems/add-two-numbers-ii/

 You are given two non-empty linked lists representing two non-negative integers. 
 The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    s1 = ""
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
        
    s2 = ""
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    
    newNum = int(s1) + int(s2)
    newNum = str(newNum)
    dummy = point = ListNode()
    i = 0
    while i < len(newNum):
        dummy.next = ListNode(newNum[i])
        i += 1
        dummy = dummy.next
    
    return point.next