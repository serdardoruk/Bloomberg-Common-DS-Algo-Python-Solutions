'''
https://leetcode.com/problems/word-search/


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(i, j, word):
            if len(word) == 0:
                return True
            
            tmp = board[i][j]
            board[i][j] = '#'
            
            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for x, y in neighbors:
                x += i
                y += j
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0]:
                    if explore(x, y, word[1:]):
                        return True

            board[i][j] = tmp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and explore(i, j, word[1:]):
                    return True
                
        return False