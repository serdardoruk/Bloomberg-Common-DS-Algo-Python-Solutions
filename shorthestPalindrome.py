'''
https://leetcode.com/problems/shortest-palindrome/
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''
def shortestPalindrome(s):

    i = 0
    
    for j in reversed(range(len(s))):
        if s[i] == s[j]:
            i+=1
            
    if i == len(s): 
        return s
    
    remain_rev = s[i:][::-1]
    
    return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]
