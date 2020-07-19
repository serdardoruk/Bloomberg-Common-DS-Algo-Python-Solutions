'''
Longest Substring Without Repeating Characters
Medium

9181

556

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = collections.defaultdict(int)
        start = 0
        longest = 0
        for i, letter in enumerate(s):
            if letter in letters:
                start = max(start, letters[letter] + 1)
            letters[letter] = i
            longest = max(longest, i - start + 1)
            
        return longest