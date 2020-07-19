'''
Input: k1 = 10 and k2 = 22
Output: 12, 20 and 22.
Explanation: The keys are 4, 8, 12, 20, and 22.
So keys in range 10 to 22 is 12, 20 and 22.

Input: k1 = 1 and k2 = 10
Output: 4 and 8
Explanation: The keys are 4, 8, 12, 20, and 22.
So keys in range 1 to 10 is 4 and 8.
'''

class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  

def Print(root, k1, k2): 

    if root is None: 
        return 
    if k1 < root.data : 
        print(root.left, k1, k2) 
  
    if k1 <= root.data and k2 >= root.data: 
        print(root.data)

    if k2 > root.data: 
        print(root.right, k1, k2) 
  

k1 = 10 ; k2 = 25 ; 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
  
print(root, k1, k2) 
