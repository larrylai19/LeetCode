# ref: https://www.cnblogs.com/grandyang/p/4299608.html

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] 表當有 i 個數字可形成的子樹個數
        dp = [1] * 2 + [0] * (n - 1)
        
        for i in range(2, n + 1):
            for j in range(i):
                # 左子樹為 j 個 nodes, 右子樹為 i-j-1 個 nodes
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[n]