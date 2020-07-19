'''
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution:
    def backtrack(self, s, res, i_start, j_start, opener, closer):
        pairs = 0
        for i in range(i_start, len(s)):
            if s[i] == opener:
                pairs += 1
            elif s[i] == closer:
                pairs -= 1
            if pairs < 0:
                # invalid string, remove extra closers
                for j in range(j_start, i + 1):
                    if s[j] == closer:
                        if j > j_start and s[j - 1] == s[j]:
                            continue
                        self.backtrack(s[:j] + s[j + 1:], res, i, j, opener, closer)
                # don't proceed with this function call bc invalid string already
                return
        reverse = s[::-1]
        if opener == "(":
            self.backtrack(reverse, res, 0, 0, closer, opener)
        else:
            res.append(reverse)

    def removeInvalidParentheses(self, s):
        res = []
        self.backtrack(s, res, 0, 0, "(", ")")
        return res

s = "()())()"
sol = Solution()
print(sol.removeInvalidParentheses(s))