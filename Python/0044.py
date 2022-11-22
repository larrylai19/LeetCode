# ref: https://www.cnblogs.com/grandyang/p/4401196.html

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 表 s[:i] 和 p[:j] 能否匹配
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True # 空字串是匹配的
        
        # 若 p 前面有一段連續星號，都是可以匹配
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
                
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # dp[i][j-1]: * 視為空字串, dp[i-1][j]: * 視為任意字符串
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]