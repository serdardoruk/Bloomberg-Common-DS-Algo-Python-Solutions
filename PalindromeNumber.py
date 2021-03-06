'''
https://leetcode.com/problems/palindrome-number/

Palindrome Number
Easy

2256

1539

Add to List

Share
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        src = num = abs(x)
        dest = 0
        
        while num>0:
            dest = dest*10+(num%10)
            num = num//10
        
        if x == src and src == dest:
            return True
        else:
            return False
        