'''
Valid Parentheses
4
nmt64's avatar
nmt64
9
Last Edit: September 15, 2019 1:04 PM

1.9K VIEWS

Question:
https://leetcode.com/problems/valid-parentheses/

Follow-up:
What if we add single quotations marks?

Example 1:

Input: {'}'
Output: false
Explanation: Because we only have 1 quotation after bracket.
Example 2:

Input: {''}
Output: true
Explanation: Dont have any quotation after bracket.
Example 3:

Input: {''}''
Output: true
Explanation: number of quotation % 2 == 0
'''

def isValid(s):
    opening = "({["
    matching = {'(' : ')', '{' : '}', '[':']'}
    stack = []
    '''
    when stack empty onlt openings can get in
    '''
    
    for p in s:
        if p in opening:
            stack.append(p)
        
        else:
            if not stack:
                return False
            
            else:
                curP = stack.pop()
                if matching[curP] != p:
                    return False
    return len(stack) == 0
            
            