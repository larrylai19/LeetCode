# ref: https://medium.com/@bill800227/leetcode-97-interleaving-string-18b1202fb0ea

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1) + 1, len(s2) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
            
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[-1][-1]