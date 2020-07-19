'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self,a,b):
        c=d=0
        for i in range(len(a)):
            c=c*10+int(a[i])
        for j in range(len(b)):
            d=d*10+int(b[j])
        return str(c+d)


# class Solution(object):
#     def addStrings(self, num1, num2):
#         res = ''
#         plus_one = 0
#         max_len = max(len(num1), len(num2))
        
#         for i in range(1, max_len + 1):
#             n1 = ord(num1[-i]) - ord('0') if i <= len(num1) else 0
#             n2 = ord(num2[-i]) - ord('0') if i <= len(num2) else 0
            
#             cur = n1 + n2 + plus_one
#             res = str(cur % 10) + res
#             plus_one = cur // 10
            
#         return '1' + res if plus_one else res
    