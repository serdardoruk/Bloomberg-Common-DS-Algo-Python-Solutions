'''
https://leetcode.com/problems/valid-anagram/

Valid Anagram


Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter = collections.defaultdict(int)
        for c in s:
            letter[c] += 1
        for c in t:
            letter[c] -= 1
        
        return False if any(i > 0 for i in letter.values()) else True