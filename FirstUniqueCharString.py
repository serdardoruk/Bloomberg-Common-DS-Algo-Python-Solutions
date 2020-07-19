'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

# (But, return type is the char, also some extra cases like string has numbers, special chars, upper and lower alphabets. \
# He told me to not consider numbers and special characters for the process and then expected to return the character itself, 
# so A and a are different characters for returning but same while counting the frequency.

import collections
def firstUniqChar(s):

    count = collections.Counter(s)
    
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return ch     
    return -1


s = "leetcode"
s = "loveleetcode"
print(firstUniqChar(s))