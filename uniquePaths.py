class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(m)] for j in range(n)]
        
    #     1 2 3 m
    # 1   
    # 2
    # n   
    
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                dp[i][0] = 1
                dp[0][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[-1][-1]
            
            
        